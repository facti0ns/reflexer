import scipy.stats as sts
import pandas as pd
import math
from .utils import approx_greater_equal_zero, assert_log

import logging

############################################################################################################################################


def p_resolve_eth_price(params, substep, state_history, state):
    eth_price = params["eth_price"](state["timestep"])
    delta_eth_price = eth_price - state_history[-1][-1]["eth_price"]

    return {"delta_eth_price": delta_eth_price}


def s_update_eth_price(params, substep, state_history, state, policy_input):
    eth_price = state["eth_price"]
    delta_eth_price = policy_input["delta_eth_price"]

    return "eth_price", eth_price + delta_eth_price


def s_update_eth_return(params, substep, state_history, state, policy_input):
    eth_price = state["eth_price"]
    delta_eth_price = policy_input["delta_eth_price"]

    return "eth_return", delta_eth_price / eth_price


def s_update_eth_gross_return(params, substep, state_history, state, policy_input):
    eth_price = state["eth_price"]
    eth_gross_return = eth_price / state_history[-1][-1]["eth_price"]

    return "eth_gross_return", eth_gross_return


def s_update_stability_fee(params, substep, state_history, state, policy_input):
    stability_fee = params["stability_fee"](state["timestep"])
    return "stability_fee", stability_fee


############################################################################################################################################


def is_cdp_above_liquidation_ratio(cdp, eth_price, target_price, liquidation_ratio):
    locked = cdp["locked"]
    freed = cdp["freed"]
    drawn = cdp["drawn"]
    wiped = cdp["wiped"]
    v_bitten = cdp["v_bitten"]
    u_bitten = cdp["u_bitten"]

    # ETH * USD/ETH >= RAI * USD/RAI * unitless
    return (locked - freed - v_bitten) * eth_price >= (
        drawn - wiped - u_bitten
    ) * target_price * liquidation_ratio


def is_cdp_at_liquidation_ratio(cdp, eth_price, target_price, liquidation_ratio):
    locked = cdp["locked"]
    freed = cdp["freed"]
    drawn = cdp["drawn"]
    wiped = cdp["wiped"]
    v_bitten = cdp["v_bitten"]
    u_bitten = cdp["u_bitten"]

    # ETH * USD/ETH >= RAI * USD/RAI * unitless
    return (locked - freed - v_bitten) * eth_price == (
        drawn - wiped - u_bitten
    ) * target_price * liquidation_ratio


def wipe_to_liquidation_ratio(
    cdp, eth_price, target_price, liquidation_ratio, _raise=False
):
    locked = cdp["locked"]
    freed = cdp["freed"]
    drawn = cdp["drawn"]
    wiped = cdp["wiped"]
    v_bitten = cdp["v_bitten"]
    u_bitten = cdp["u_bitten"]

    # RAI - (USD/ETH) * ETH / (unitless * USD/RAI) -> RAI
    wipe = (drawn - wiped - u_bitten) - (locked - freed - v_bitten) * eth_price / (
        liquidation_ratio * target_price
    )
    assert_log(
        approx_greater_equal_zero(wipe, abs_tol=1e-3),
        f"wipe: {wipe} ~ cdp: {cdp}",
        _raise=_raise,
    )
    wipe = max(wipe, 0)

    if drawn <= wiped + wipe + u_bitten:
        wipe = 0

    return wipe


def draw_to_liquidation_ratio(
    cdp, eth_price, target_price, liquidation_ratio, _raise=False
):
    locked = cdp["locked"]
    freed = cdp["freed"]
    drawn = cdp["drawn"]
    wiped = cdp["wiped"]
    v_bitten = cdp["v_bitten"]
    u_bitten = cdp["u_bitten"]

    # (USD/ETH) * ETH / (USD/RAI * unitless) - RAI
    draw = (locked - freed - v_bitten) * eth_price / (
        target_price * liquidation_ratio
    ) - (drawn - wiped - u_bitten)
    assert_log(
        approx_greater_equal_zero(draw, abs_tol=1e-3), f"draw: {draw}", _raise=_raise
    )
    draw = max(draw, 0)

    return draw


def lock_to_liquidation_ratio(
    cdp, eth_price, target_price, liquidation_ratio, _raise=False
):
    locked = cdp["locked"]
    freed = cdp["freed"]
    drawn = cdp["drawn"]
    wiped = cdp["wiped"]
    v_bitten = cdp["v_bitten"]
    u_bitten = cdp["u_bitten"]

    # (USD/RAI * RAI * unitless - ETH * USD/ETH) / USD/ETH -> ETH
    lock = (
        (drawn - wiped - u_bitten) * target_price * liquidation_ratio
        - (locked - freed - v_bitten) * eth_price
    ) / eth_price
    assert_log(
        approx_greater_equal_zero(lock, abs_tol=1e-3), f"lock: {lock}", _raise=_raise
    )
    lock = max(lock, 0)

    return lock


def free_to_liquidation_ratio(
    cdp, eth_price, target_price, liquidation_ratio, _raise=False
):
    locked = cdp["locked"]
    freed = cdp["freed"]
    drawn = cdp["drawn"]
    wiped = cdp["wiped"]
    v_bitten = cdp["v_bitten"]
    u_bitten = cdp["u_bitten"]

    # (ETH * USD/ETH - unitless * RAI * USD/RAI) / (USD/ETH) -> ETH
    free = (
        (locked - freed - v_bitten) * eth_price
        - liquidation_ratio * (drawn - wiped - u_bitten) * target_price
    ) / eth_price
    assert_log(
        approx_greater_equal_zero(free, abs_tol=1e-3), f"free: {free}", _raise=_raise
    )
    free = max(free, 0)

    return free


def open_cdp_lock(lock, eth_price, target_price, liquidation_ratio):
    # ETH * USD/ETH / (USD/RAI * unitless) -> RAI
    draw = lock * eth_price / (target_price * liquidation_ratio)
    return {
        "open": 1,
        "time": 0,
        "locked": lock,
        "drawn": draw,
        "wiped": 0.0,
        "freed": 0.0,
        "w_wiped": 0.0,
        "dripped": 0.0,
        "v_bitten": 0.0,
        "u_bitten": 0.0,
        "w_bitten": 0.0,
    }


def open_cdp_draw(draw, eth_price, target_price, liquidation_ratio):
    # (RAI * USD/RAI * unitless) / (USD/ETH) -> ETH
    lock = (draw * target_price * liquidation_ratio) / eth_price
    return {
        "open": 1,
        "time": 0,
        "locked": lock,
        "drawn": draw,
        "wiped": 0.0,
        "freed": 0.0,
        "w_wiped": 0.0,
        "dripped": 0.0,
        "v_bitten": 0.0,
        "u_bitten": 0.0,
        "w_bitten": 0.0,
    }


def p_rebalance_cdps(params, substep, state_history, state):
    cdps = state["cdps"]

    eth_price = state["eth_price"]
    target_price = state["target_price"]
    liquidation_ratio = params["liquidation_ratio"]
    liquidation_buffer = params["liquidation_buffer"]

    for index, cdp in cdps.query("open == 1").iterrows():
        cdp_above_liquidation_buffer = is_cdp_above_liquidation_ratio(
            cdp, eth_price, target_price, liquidation_ratio * liquidation_buffer
        )

        if not cdp_above_liquidation_buffer:
            wiped = cdps.at[index, "wiped"]
            wipe = wipe_to_liquidation_ratio(
                cdp,
                eth_price,
                target_price,
                liquidation_ratio * liquidation_buffer,
                params["raise_on_assert"],
            )
            cdps.at[index, "wiped"] = wiped + wipe
        else:
            drawn = cdps.at[index, "drawn"]
            draw = draw_to_liquidation_ratio(
                cdp,
                eth_price,
                target_price,
                liquidation_ratio * liquidation_buffer,
                params["raise_on_assert"],
            )
            cdps.at[index, "drawn"] = drawn + draw

    open_cdps = len(cdps.query("open == 1"))
    closed_cdps = len(cdps.query("open == 0"))
    logging.debug(
        f"p_rebalance_cdps() ~ Number of open CDPs: {open_cdps}; Number of closed CDPs: {closed_cdps}"
    )

    return {"cdps": cdps}


def resolve_cdp_positions(params, state, policy_input):
    eth_price = state["eth_price"]
    target_price = state["target_price"]
    liquidation_ratio = params["liquidation_ratio"]
    liquidation_buffer = params["liquidation_buffer"]

    cdps = state["cdps"]
    cdps_copy = cdps.copy()

    v_1 = policy_input["v_1"]  # Lock
    v_2 = policy_input["v_2 + v_3"]  # Free, no v_3 liquidations
    u_1 = policy_input["u_1"]  # Draw
    # TODO: set to some form of random process around mean
    u_2 = policy_input["u_2"]  # Wipe
    w_2 = 0

    # If v_1 >= (u_1 * (targe_rate * ratio + buffer) / eth_price), then:
    # Take half of u_1 for creation of new CDPs, take ratio + buffer equivalent of v_1 towards creation of CDPs
    # Else:
    # Take half of v_1 for creation of new CDPs, take ratio + buffer equivalent of u_1 towards creation of CDPs
    if v_1 >= (u_1 * target_price * liquidation_ratio * liquidation_buffer) / eth_price:
        new_cdps_draw = u_1 * params["new_cdp_proportion"]
        u_1 = u_1 - new_cdps_draw
        new_cdps_lock = (
            new_cdps_draw * target_price * liquidation_ratio * liquidation_buffer
        ) / eth_price
        v_1 = v_1 - new_cdps_lock

        assert_log(
            v_1 >= 0, f"New CDP creation: v_1 ~ {v_1} !>= 0", params["raise_on_assert"]
        )
        assert_log(
            u_1 >= 0, f"New CDP creation: u_1 ~ {u_1} !>= 0", params["raise_on_assert"]
        )

        new_cdps_count = int(new_cdps_lock / params["new_cdp_collateral"])
        cumulative_time = state["cumulative_time"]

        cdps = cdps.append(
            [
                {
                    "open": 1,
                    "time": cumulative_time,
                    "locked": new_cdps_lock / new_cdps_count,
                    "drawn": new_cdps_draw / new_cdps_count,
                    "wiped": 0.0,
                    "freed": 0.0,
                    "w_wiped": 0.0,
                    "dripped": 0.0,
                    "v_bitten": 0.0,
                    "u_bitten": 0.0,
                    "w_bitten": 0.0,
                }
                for _ in range(new_cdps_count)
            ],
            ignore_index=True,
        )
    else:
        new_cdps_lock = v_1 * params["new_cdp_proportion"]
        v_1 = v_1 - new_cdps_lock
        new_cdps_draw = (new_cdps_lock * eth_price) / (
            target_price * liquidation_ratio * liquidation_buffer
        )
        u_1 = u_1 - new_cdps_draw

        assert_log(
            v_1 >= 0, f"New CDP creation: v_1 ~ {v_1} !>= 0", params["raise_on_assert"]
        )
        assert_log(
            u_1 >= 0, f"New CDP creation: u_1 ~ {u_1} !>= 0", params["raise_on_assert"]
        )

        new_cdps_count = int(new_cdps_lock / params["new_cdp_collateral"])
        cumulative_time = state["cumulative_time"]

        cdps = cdps.append(
            [
                {
                    "open": 1,
                    "time": cumulative_time,
                    "locked": new_cdps_lock / new_cdps_count,
                    "drawn": new_cdps_draw / new_cdps_count,
                    "wiped": 0.0,
                    "freed": 0.0,
                    "w_wiped": 0.0,
                    "dripped": 0.0,
                    "v_bitten": 0.0,
                    "u_bitten": 0.0,
                    "w_bitten": 0.0,
                }
                for _ in range(new_cdps_count)
            ],
            ignore_index=True,
        )

    cdps_newest = cdps.sort_values(by=["time"], ascending=True)  # Youngest to oldest
    cdps_oldest = cdps.sort_values(by=["time"], ascending=False)  # Oldest to youngest

    # CDP rebalancing
    for index, cdp in cdps_newest.query("open == 1").iterrows():
        locked = cdps.at[index, "locked"]
        freed = cdps.at[index, "freed"]
        drawn = cdps.at[index, "drawn"]
        v_bitten = cdps.at[index, "v_bitten"]
        wiped = cdps.at[index, "wiped"]
        u_bitten = cdps.at[index, "u_bitten"]

        cdp_above_liquidation_buffer = is_cdp_above_liquidation_ratio(
            cdp, eth_price, target_price, liquidation_ratio * liquidation_buffer
        )

        # If L<¯L+Δ, apply a wipe from QW until L=¯L+Δ, if possible;
        if not cdp_above_liquidation_buffer:
            if u_2 >= 0:
                wipe = wipe_to_liquidation_ratio(
                    cdp,
                    eth_price,
                    target_price,
                    liquidation_ratio * liquidation_buffer,
                    params["raise_on_assert"],
                )

                if u_2 - wipe > 0:
                    cdps.at[index, "wiped"] = wiped + wipe
                    u_2 = u_2 - wipe
                else:
                    cdps.at[index, "wiped"] = wiped + u_2
                    u_2 = 0
            else:
                # If positions are not cycled, but wipes and draws are exhausted, then proceed to applying any non-exhausted frees and locks:
                # If L<¯L+Δ, apply a lock from QL until L=¯L+Δ, if possible;
                lock = lock_to_liquidation_ratio(
                    cdp,
                    eth_price,
                    target_price,
                    liquidation_ratio * liquidation_buffer,
                    params["raise_on_assert"],
                )

                if v_1 - lock > 0:
                    cdps.at[index, "locked"] = locked + lock
                    v_1 = v_1 - lock
                else:
                    cdps.at[index, "locked"] = locked + v_1
                    v_1 = 0

        # If L>¯L+Δ, apply a draw from QD until L=¯L+Δ, if possible;
        else:
            if u_1 >= 0:
                draw = draw_to_liquidation_ratio(
                    cdp,
                    eth_price,
                    target_price,
                    liquidation_ratio * liquidation_buffer,
                    params["raise_on_assert"],
                )

                if u_1 - draw > 0:
                    cdps.at[index, "drawn"] = drawn + draw
                    u_1 = u_1 - draw
                else:
                    cdps.at[index, "drawn"] = drawn + u_1
                    u_1 = 0
            else:
                # If positions are not cycled, but wipes and draws are exhausted, then proceed to applying any non-exhausted frees and locks:
                # If L>¯L+Δ, apply a free from QF until L=¯L+Δ, if possible.
                free = free_to_liquidation_ratio(
                    cdp,
                    eth_price,
                    target_price,
                    liquidation_ratio * liquidation_buffer,
                    params["raise_on_assert"],
                )

                if v_2 - free >= 0:
                    cdps.at[index, "freed"] = freed + free
                    v_2 = v_2 - free
                else:
                    cdps.at[index, "freed"] = freed + v_2
                    v_2 = 0

        if u_1 <= 0 and u_2 <= 0:
            break

    # Close CDPs with excess wipes
    if u_2 > 0:
        for index, cdp in cdps_oldest.query("open == 1").iterrows():
            locked = cdps.at[index, "locked"]
            freed = cdps.at[index, "freed"]
            drawn = cdps.at[index, "drawn"]
            v_bitten = cdps.at[index, "v_bitten"]
            wiped = cdps.at[index, "wiped"]
            dripped = cdps.at[index, "dripped"]
            u_bitten = cdps.at[index, "u_bitten"]

            _v_2 = locked - freed - v_bitten
            _u_2 = drawn - wiped - u_bitten
            _w_2 = dripped

            w_2 += _w_2

            # TODO
            # cdps.at[index, 'open'] = 0
            cdps.at[index, "w_wiped"] = dripped

            if u_2 - _u_2 > 0:
                cdps.at[index, "wiped"] = wiped + _u_2
                u_2 = u_2 - _u_2
                if v_2 - _v_2 >= 0:
                    cdps.at[index, "freed"] = freed + _v_2
                    v_2 = v_2 - _v_2
                else:
                    cdps.at[index, "freed"] = freed + v_2
                    v_2 = 0
                # If all debt wiped, close
                cdps.at[index, "open"] = 0
            else:
                cdps.at[index, "wiped"] = wiped + u_2
                u_2 = 0

    if u_1 > 0:
        cumulative_time = state["cumulative_time"]
        _u_1 = u_1
        _v_1 = _u_1 * target_price * liquidation_ratio * liquidation_buffer / eth_price

        u_1 = 0
        if v_1 - _v_1 >= 0:
            v_1 = v_1 - _v_1
        else:
            _v_1 = v_1
            v_1 = 0

        cdps = cdps.append(
            {
                "open": 1,
                "time": cumulative_time,
                "locked": _v_1,
                "drawn": _u_1,
                "wiped": 0.0,
                "freed": 0.0,
                "w_wiped": 0.0,
                "dripped": 0.0,
                "v_bitten": 0.0,
                "u_bitten": 0.0,
                "w_bitten": 0.0,
            },
            ignore_index=True,
        )

    if v_1 > 0:
        cumulative_time = state["cumulative_time"]
        assert_log(u_1 == 0, u_1, params["raise_on_assert"])
        cdps = cdps.append(
            {
                "open": 1,
                "time": cumulative_time,
                "locked": v_1,
                "drawn": u_1,
                "wiped": 0.0,
                "freed": 0.0,
                "w_wiped": 0.0,
                "dripped": 0.0,
                "v_bitten": 0.0,
                "u_bitten": 0.0,
                "w_bitten": 0.0,
            },
            ignore_index=True,
        )
        v_1 = 0

    # Close CDPs with excess frees
    # Index reset in 'append'
    cdps_oldest = cdps.sort_values(by=["time"], ascending=False)  # Oldest to youngest
    if v_2 > 0:
        for index, cdp in cdps_oldest.query("open == 1").iterrows():
            locked = cdps.at[index, "locked"]
            freed = cdps.at[index, "freed"]
            drawn = cdps.at[index, "drawn"]
            v_bitten = cdps.at[index, "v_bitten"]
            wiped = cdps.at[index, "wiped"]
            dripped = cdps.at[index, "dripped"]
            u_bitten = cdps.at[index, "u_bitten"]

            w_2 += dripped
            _v_2 = locked - freed - v_bitten

            if v_2 - _v_2 > 0:
                cdps.at[index, "freed"] = freed + _v_2
                cdps.at[index, "w_wiped"] = dripped
                # TODO: let liquidate handle this?
                # cdps.at[index, 'open'] = 0
                v_2 = v_2 - _v_2
            else:
                cdps.at[index, "freed"] = freed + v_2
                cdps.at[index, "w_wiped"] = dripped
                # TODO
                # cdps.at[index, 'open'] = 0
                v_2 = 0
                break

    u_1 = cdps["drawn"].sum() - cdps_copy["drawn"].sum()
    if policy_input["u_1"]:
        event = f'u_1 not balanced: {(u_1, policy_input["u_1"])}'
        assert_log(
            math.isclose(u_1, policy_input["u_1"], rel_tol=0.0, abs_tol=1e-6),
            event,
            params["raise_on_assert"],
        )
        # if not math.isclose(u_1, policy_input['u_1'], rel_tol=1e-6, abs_tol=0.0):
        #     print(event)

    u_2 = cdps["wiped"].sum() - cdps_copy["wiped"].sum()
    if policy_input["u_2"]:
        event = f'u_2 not balanced: {(u_2, policy_input["u_2"])}'
        assert_log(
            math.isclose(u_2, policy_input["u_2"], rel_tol=0.0, abs_tol=1e-6),
            event,
            params["raise_on_assert"],
        )
        # if not math.isclose(u_2, policy_input['u_2'], rel_tol=1e-6, abs_tol=0.0):
        #     print(event)

    v_1 = cdps["locked"].sum() - cdps_copy["locked"].sum()
    if policy_input["v_1"]:
        event = f'v_1 not balanced: {(v_1, policy_input["v_1"])}'
        assert_log(
            math.isclose(v_1, policy_input["v_1"], rel_tol=0.0, abs_tol=1e-6),
            event,
            params["raise_on_assert"],
        )
        # if not math.isclose(v_1, policy_input['v_1'], rel_tol=1e-6, abs_tol=0.0):
        #     print(event)

    v_2 = cdps["freed"].sum() - cdps_copy["freed"].sum()
    if policy_input["v_2 + v_3"]:
        event = f'v_2 not balanced: {(v_2, policy_input["v_2 + v_3"])}'
        assert_log(
            math.isclose(v_2, policy_input["v_2 + v_3"], rel_tol=0.0, abs_tol=1e-6),
            event,
            params["raise_on_assert"],
        )
        # if not math.isclose(v_2, policy_input['v_2 + v_3'], rel_tol=1e-6, abs_tol=0.0):
        #     print(event)

    open_cdps = len(cdps.query("open == 1"))
    closed_cdps = len(cdps.query("open == 0"))
    logging.debug(
        f"resolve_cdp_positions() ~ Number of open CDPs: {open_cdps}; Number of closed CDPs: {closed_cdps}"
    )

    assert_log(u_1 >= 0, u_1, params["raise_on_assert"])
    assert_log(u_2 >= 0, u_2, params["raise_on_assert"])
    assert_log(v_1 >= 0, v_1, params["raise_on_assert"])
    assert_log(v_2 >= 0, v_2, params["raise_on_assert"])

    assert_log(
        approx_greater_equal_zero(
            cdps["drawn"].sum() - cdps["wiped"].sum() - cdps["u_bitten"].sum(),
            abs_tol=1e-2,
        ),
        (cdps["drawn"].sum(), cdps["wiped"].sum(), cdps["u_bitten"].sum()),
        params["raise_on_assert"],
    )

    assert_log(
        approx_greater_equal_zero(
            cdps["locked"].sum() - cdps["freed"].sum() - cdps["v_bitten"].sum(),
            abs_tol=1e-2,
        ),
        (cdps["locked"].sum(), cdps["freed"].sum(), cdps["v_bitten"].sum()),
        params["raise_on_assert"],
    )

    return {
        "cdps": cdps,
        "u_1": u_1,
        "u_2": u_2,
        "v_1": v_1,
        "v_2": v_2,
        "v_2 + v_3": v_2,
        "w_2": w_2,
    }


def p_close_cdps(params, substep, state_history, state):
    cdps = state["cdps"]
    average_debt_age = params["average_debt_age"]
    cumulative_time = state["cumulative_time"]

    closed_cdps = cdps.query("open == 1").query(
        f"{cumulative_time} - time >= {average_debt_age}"
    )

    v_2 = (
        closed_cdps["locked"].sum()
        - closed_cdps["freed"].sum()
        - closed_cdps["v_bitten"].sum()
    )
    u_2 = (
        closed_cdps["drawn"].sum()
        - closed_cdps["wiped"].sum()
        - closed_cdps["u_bitten"].sum()
    )
    w_2 = closed_cdps["dripped"].sum()

    assert_log(v_2 >= 0, v_2, params["raise_on_assert"])
    assert_log(u_2 >= 0, u_2, params["raise_on_assert"])
    assert_log(w_2 >= 0, w_2, params["raise_on_assert"])

    for index, cdp in closed_cdps.iterrows():
        locked = cdps.at[index, "locked"]
        freed = cdps.at[index, "freed"]
        drawn = cdps.at[index, "drawn"]
        v_bitten = cdps.at[index, "v_bitten"]
        wiped = cdps.at[index, "wiped"]
        u_bitten = cdps.at[index, "u_bitten"]
        dripped = cdps.at[index, "dripped"]

        free = locked - freed - v_bitten
        assert_log(free >= 0, free, params["raise_on_assert"])
        cdps.at[index, "freed"] = freed + free

        wipe = drawn - wiped - u_bitten
        assert_log(wipe >= 0, wipe, params["raise_on_assert"])
        cdps.at[index, "wiped"] = wiped + wipe

        cdps.at[index, "w_wiped"] = dripped

        cdps.at[index, "open"] = 0

    # try:
    #    cdps = cdps.drop(closed_cdps.index)
    # except KeyError:
    #    print('Failed to drop CDPs')
    #    raise

    logging.debug(f"{len(closed_cdps)} CDPs closed with v_2 {v_2} u_2 {u_2} w_2 {w_2}")

    return {"cdps": cdps, "v_2": v_2, "u_2": u_2, "w_2": w_2}


def p_liquidate_cdps(params, substep, state_history, state):
    eth_price = state["eth_price"]
    target_price = state["target_price"]
    liquidation_penalty = params["liquidation_penalty"]
    liquidation_ratio = params["liquidation_ratio"]

    cdps = state["cdps"]
    cdps_copy = cdps.copy()
    liquidated_cdps = pd.DataFrame()
    if len(cdps) > 0:
        try:
            liquidated_cdps = cdps.query("open == 1").query(
                f"(locked - freed - v_bitten) * {eth_price} < (drawn - wiped - u_bitten) * {target_price} * {liquidation_ratio}"
            )
        except:
            print(state)
            raise

    for index, cdp in liquidated_cdps.iterrows():
        locked = cdps.at[index, "locked"]
        freed = cdps.at[index, "freed"]
        drawn = cdps.at[index, "drawn"]
        wiped = cdps.at[index, "wiped"]
        dripped = cdps.at[index, "dripped"]
        v_bitten = cdps.at[index, "v_bitten"]
        u_bitten = cdps.at[index, "u_bitten"]
        w_bitten = cdps.at[index, "w_bitten"]

        assert_log(locked >= 0, locked, params["raise_on_assert"])
        assert_log(freed >= 0, freed, params["raise_on_assert"])
        assert_log(drawn >= 0, drawn, params["raise_on_assert"])
        assert_log(wiped >= 0, wiped, params["raise_on_assert"])
        assert_log(dripped >= 0, dripped, params["raise_on_assert"])
        assert_log(v_bitten >= 0, v_bitten, params["raise_on_assert"])
        assert_log(u_bitten >= 0, u_bitten, params["raise_on_assert"])
        assert_log(w_bitten >= 0, w_bitten, params["raise_on_assert"])

        try:
            v_bite = (
                (drawn - wiped - u_bitten) * target_price * (1 + liquidation_penalty)
            ) / eth_price
            assert v_bite >= 0, f"{v_bite} !>= 0 ~ {state}"
            assert v_bite <= (
                locked - freed - v_bitten
            ), f"Liquidation short of collateral: {v_bite} !<= {locked - freed - v_bitten}"
            free = locked - freed - v_bitten - v_bite
            assert free >= 0, f"{free} !>= {0}"
            assert (
                locked >= freed + free + v_bitten + v_bite
            ), f"locked eq check: {(locked, freed, free, v_bitten, v_bite)}"
            w_bite = dripped
            assert w_bite >= 0, f"w_bite: {w_bite}"
            u_bite = drawn - wiped - u_bitten
            assert u_bite >= 0, f"u_bite: {u_bite}"
            assert (
                u_bite <= drawn - wiped - u_bitten
            ), f"Liquidation invalid u_bite: {u_bite} !<= {drawn - wiped - u_bitten}"
        except AssertionError as err:
            logging.warning(err)
            v_bite = locked - freed - v_bitten
            u_bite = drawn - wiped - u_bitten
            free = 0
            w_bite = dripped

        cdps.at[index, "v_bitten"] = v_bitten + v_bite
        cdps.at[index, "freed"] = freed + free
        cdps.at[index, "u_bitten"] = u_bitten + u_bite
        cdps.at[index, "w_bitten"] = w_bitten + w_bite
        cdps.at[index, "open"] = 0

    v_2 = cdps["freed"].sum() - cdps_copy["freed"].sum()
    v_3 = cdps["v_bitten"].sum() - cdps_copy["v_bitten"].sum()
    u_3 = cdps["u_bitten"].sum() - cdps_copy["u_bitten"].sum()
    w_3 = cdps["w_bitten"].sum() - cdps_copy["w_bitten"].sum()

    assert_log(v_2 >= 0, v_2, params["raise_on_assert"])
    assert_log(v_3 >= 0, v_3, params["raise_on_assert"])
    assert_log(u_3 >= 0, u_3, params["raise_on_assert"])
    assert_log(w_3 >= 0, w_3, params["raise_on_assert"])

    # try:
    #     cdps = cdps.drop(liquidated_cdps.index)
    # except KeyError:
    #     print('Failed to drop CDPs')
    #     raise

    logging.debug(
        f"{len(liquidated_cdps)} CDPs liquidated with v_2 {v_2} v_3 {v_3} u_3 {u_3} w_3 {w_3}"
    )

    return {"cdps": cdps, "v_2": v_2, "v_3": v_3, "u_3": u_3, "w_3": w_3}


############################################################################################################################################


def s_store_cdps(params, substep, state_history, state, policy_input):
    return "cdps", policy_input["cdps"]


############################################################################################################################################
"""
Aggregate the state values from CDP state
"""


def get_cdps_state_change(state, state_history, key):
    cdps = state["cdps"]
    previous_cdps = state_history[-1][-1]["cdps"]
    return cdps[key].sum() - previous_cdps[key].sum()


def s_aggregate_v_1(params, substep, state_history, state, policy_input):
    return "v_1", get_cdps_state_change(state, state_history, "locked")


def s_aggregate_u_1(params, substep, state_history, state, policy_input):
    return "u_1", get_cdps_state_change(state, state_history, "drawn")


def s_aggregate_w_1(params, substep, state_history, state, policy_input):
    return "w_1", get_cdps_state_change(state, state_history, "dripped")


def s_aggregate_v_2(params, substep, state_history, state, policy_input):
    return "v_2", get_cdps_state_change(state, state_history, "freed")


def s_aggregate_u_2(params, substep, state_history, state, policy_input):
    return "u_2", get_cdps_state_change(state, state_history, "wiped")


def s_aggregate_w_2(params, substep, state_history, state, policy_input):
    return "w_2", get_cdps_state_change(state, state_history, "w_wiped")


def s_aggregate_v_3(params, substep, state_history, state, policy_input):
    return "v_3", get_cdps_state_change(state, state_history, "v_bitten")


def s_aggregate_u_3(params, substep, state_history, state, policy_input):
    return "u_3", get_cdps_state_change(state, state_history, "u_bitten")


def s_aggregate_w_3(params, substep, state_history, state, policy_input):
    return "w_3", get_cdps_state_change(state, state_history, "w_bitten")


############################################################################################################################################
"""
Set the state values temporarily
"""


def s_set_v_1(params, substep, state_history, state, policy_input):
    return "v_1", policy_input["v_1"]


def s_set_v_2(params, substep, state_history, state, policy_input):
    return "v_2", policy_input["v_2"]


def s_set_v_3(params, substep, state_history, state, policy_input):
    return "v_3", policy_input["v_3"]


def s_set_u_1(params, substep, state_history, state, policy_input):
    return "u_1", policy_input["u_1"]


def s_set_u_2(params, substep, state_history, state, policy_input):
    return "u_2", policy_input["u_2"]


def s_set_u_3(params, substep, state_history, state, policy_input):
    return "u_3", policy_input["u_3"]


def s_set_w_1(params, substep, state_history, state, policy_input):
    return "w_1", policy_input["w_1"]


def s_set_w_2(params, substep, state_history, state, policy_input):
    return "w_2", policy_input["w_2"]


def s_set_w_3(params, substep, state_history, state, policy_input):
    return "w_3", policy_input["w_3"]


############################################################################################################################################


def s_update_eth_collateral(params, substep, state_history, state, policy_input):
    eth_locked = state["eth_locked"]
    eth_freed = state["eth_freed"]
    eth_bitten = state["eth_bitten"]

    eth_collateral = eth_locked - eth_freed - eth_bitten
    event = (
        f"ETH collateral < 0: {eth_collateral} ~ {(eth_locked, eth_freed, eth_bitten)}"
    )
    if not assert_log(
        approx_greater_equal_zero(eth_collateral, 1e-2),
        event,
        params["raise_on_assert"],
    ):
        eth_collateral = 0

    return "eth_collateral", eth_collateral


def s_update_principal_debt(params, substep, state_history, state, policy_input):
    rai_drawn = state["rai_drawn"]
    rai_wiped = state["rai_wiped"]
    rai_bitten = state["rai_bitten"]

    principal_debt = rai_drawn - rai_wiped - rai_bitten

    event = (
        f"Principal debt < 0: {principal_debt} ~ {(rai_drawn, rai_wiped, rai_bitten)}"
    )
    if not assert_log(
        approx_greater_equal_zero(principal_debt, 1e-2),
        event,
        params["raise_on_assert"],
    ):
        principal_debt = 0

    return "principal_debt", principal_debt


def s_update_eth_locked(params, substep, state_history, state, policy_input):
    eth_locked = state["eth_locked"]
    v_1 = state["v_1"]

    assert_log(v_1 >= 0, v_1, params["raise_on_assert"])

    return "eth_locked", eth_locked + v_1


def s_update_eth_freed(params, substep, state_history, state, policy_input):
    eth_freed = state["eth_freed"]
    v_2 = state["v_2"]

    assert_log(v_2 >= 0, v_2, params["raise_on_assert"])

    return "eth_freed", eth_freed + v_2


def s_update_eth_bitten(params, substep, state_history, state, policy_input):
    eth_bitten = state["eth_bitten"]
    v_3 = state["v_3"]

    assert_log(v_3 >= 0, v_3, params["raise_on_assert"])

    return "eth_bitten", eth_bitten + v_3


def s_update_rai_drawn(params, substep, state_history, state, policy_input):
    rai_drawn = state["rai_drawn"]
    u_1 = state["u_1"]

    assert_log(u_1 >= 0, u_1, params["raise_on_assert"])

    return "rai_drawn", rai_drawn + u_1


def s_update_rai_wiped(params, substep, state_history, state, policy_input):
    rai_wiped = state["rai_wiped"]
    u_2 = state["u_2"]

    assert_log(u_2 >= 0, u_2, params["raise_on_assert"])

    return "rai_wiped", rai_wiped + u_2


def s_update_rai_bitten(params, substep, state_history, state, policy_input):
    rai_bitten = state["rai_bitten"]
    u_3 = state["u_3"]

    assert_log(u_3 >= 0, u_3, params["raise_on_assert"])

    return "rai_bitten", rai_bitten + u_3


def s_update_system_revenue(params, substep, state_history, state, policy_input):
    system_revenue = state["system_revenue"]
    w_2 = state["w_2"]
    return "system_revenue", system_revenue + w_2


## TODO: verify/test logic for negative interest rates
def calculate_accrued_interest(
    stability_fee, target_rate, timedelta, debt, accrued_interest
):
    # (1 + target_rate)
    return (((1 + stability_fee)) ** timedelta - 1) * (debt + accrued_interest)


def s_update_accrued_interest(params, substep, state_history, state, policy_input):
    previous_accrued_interest = state["accrued_interest"]
    principal_debt = state["principal_debt"]

    stability_fee = state["stability_fee"]
    target_rate = state["target_rate"]
    timedelta = state["timedelta"]

    accrued_interest = calculate_accrued_interest(
        stability_fee, target_rate, timedelta, principal_debt, previous_accrued_interest
    )
    return "accrued_interest", previous_accrued_interest + accrued_interest


def s_update_interest_bitten(params, substep, state_history, state, policy_input):
    previous_accrued_interest = state["accrued_interest"]
    w_3 = state["w_3"]
    return "accrued_interest", previous_accrued_interest - w_3


def s_update_cdp_interest(params, substep, state_history, state, policy_input):
    cdps = state["cdps"]
    stability_fee = state["stability_fee"]
    target_rate = state["target_rate"]
    timedelta = state["timedelta"]

    def resolve_cdp_interest(cdp):
        if cdp["open"]:
            principal_debt = cdp["drawn"]
            previous_accrued_interest = cdp["dripped"]
            cdp["dripped"] = calculate_accrued_interest(
                stability_fee,
                target_rate,
                timedelta,
                principal_debt,
                previous_accrued_interest,
            )
        return cdp

    cdps = cdps.apply(resolve_cdp_interest, axis=1)

    return "cdps", cdps


def s_update_cdp_metrics(params, substep, state_history, state, policy_input):
    cdps = state["cdps"]
    cdp_metrics = {
        "cdp_count": len(cdps),
        "open_cdp_count": len(cdps.query("open == 1")),
        "closed_cdp_count": len(cdps.query("open == 0")),
        "mean_cdp_collateral": pd.eval(
            "cdp_collateral = cdps.locked - cdps.freed - cdps.v_bitten", target=cdps
        )["cdp_collateral"].mean(),
        "median_cdp_collateral": pd.eval(
            "cdp_collateral = cdps.locked - cdps.freed - cdps.v_bitten", target=cdps
        )["cdp_collateral"].median(),
    }
    return "cdp_metrics", cdp_metrics
