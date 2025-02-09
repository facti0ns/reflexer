
# Experiment on 2021-02-11T09:20:25.289537
* Passed: True
* Time: 3.175065000851949 minutes
* Results folder: /home/ubuntu/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-11T09:20:25.290821_5
* Git Hash: c64c7a7

Exceptions:

```
                                           exception  ...                                      initial_state
0  Uniswap RAI RAI_balance=3413345.008188522 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1  Uniswap RAI RAI_balance=20190774.60897813 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3  Uniswap RAI RAI_balance=4863225.894156508 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
5  Uniswap RAI RAI_balance=4210960.478978895 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
6  Uniswap RAI RAI_balance=5116277.995079072 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
7  Uniswap RAI RAI_balance=38525656.92044132 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
8                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
9                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[10 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-11T09:20:25.289537
* Passed: True
* Time: 22.471120993296307 minutes
* Results folder: /home/ubuntu/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-11T09:20:25.290821_4
* Git Hash: c64c7a7

Exceptions:

```
                                            exception  ...                                      initial_state
0   Uniswap RAI RAI_balance=20206635.092890635 RAI...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                          ETH_delta=38.2141167124878  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                        ETH_delta=181.62090056237057  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-11T09:20:25.289537
* Passed: True
* Time: 21.761529099941253 minutes
* Results folder: /home/ubuntu/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-11T09:20:25.290821_3
* Git Hash: c64c7a7

Exceptions:

```
                                            exception  ...                                      initial_state
0                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                         ETH_delta=2524.187894240135  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3                         ETH_delta=526.6818758829365  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4   Uniswap RAI RAI_balance=2038247.1439833022 RAI...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-11T09:20:25.289537
* Passed: True
* Time: 21.575931870937346 minutes
* Results folder: /home/ubuntu/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-11T09:20:25.290821_2
* Git Hash: c64c7a7

Exceptions:

```
                                            exception  ...                                      initial_state
0                         ETH_delta=506.8875106946646  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                         ETH_delta=556.6486364827186  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3   Uniswap RAI RAI_balance=2277307.9692086168 RAI...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4   Uniswap RAI RAI_balance=23617356.90744966 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-11T09:20:25.289537
* Passed: True
* Time: 22.27848733663559 minutes
* Results folder: /home/ubuntu/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-11T09:20:25.290821_1
* Git Hash: c64c7a7

Exceptions:

```
                                            exception  ...                                      initial_state
0                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                         ETH_delta=723.4393731033003  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3   Uniswap RAI RAI_balance=23485994.093109168 RAI...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                        ETH_delta=16172.066075840534  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-11T09:20:25.289537
* Passed: True
* Time: 23.702066846688588 minutes
* Results folder: /home/ubuntu/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-11T09:20:25.290821_0
* Git Hash: c64c7a7

Exceptions:

```
                                            exception  ...                                      initial_state
0                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                         ETH_delta=2069.780403933738  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2   Uniswap RAI RAI_balance=800947.6333775959 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3                          ETH_delta=6725.23599658255  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4   Uniswap RAI RAI_balance=604536.5793507294 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 25.059624397754668 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_10
* Git Hash: 1dfe23b

Exceptions:

```
                                            exception  ...                                      initial_state
0                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                          ETH_delta=516.824201248718  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2   Uniswap RAI RAI_balance=2039459.615094627 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3   Uniswap RAI RAI_balance=23720936.41989187 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4   Uniswap RAI RAI_balance=3406636.3689939436 RAI...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 26.465071666240693 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_9
* Git Hash: 1dfe23b

Exceptions:

```
                                            exception  ...                                      initial_state
0                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                        ETH_delta=1682.8360986375435  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2   Uniswap RAI RAI_balance=843752.5231843891 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3                        ETH_delta=-376.6896015554195  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                       ETH_delta=-1931.2887724283967  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 26.183073325951895 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_8
* Git Hash: 1dfe23b

Exceptions:

```
                                            exception  ...                                      initial_state
0                        ETH_delta=1824.8414368876483  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1   Uniswap RAI RAI_balance=875257.6200468285 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                         ETH_delta=953.7156860248721  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3                         ETH_delta=63.52650610845421  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 26.93676882982254 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_7
* Git Hash: 1dfe23b

Exceptions:

```
                                            exception  ...                                      initial_state
0   Uniswap RAI RAI_balance=802033.8316038542 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                         ETH_delta=6727.548943880629  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2   Uniswap RAI RAI_balance=604973.9010844954 RAI_...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                        ETH_delta=1154.3713004799201  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 26.978827567895255 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_6
* Git Hash: 1dfe23b

Exceptions:

```
                        exception  ...                                      initial_state
0   ETH_delta=-376.80740918243896  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1   ETH_delta=-2440.8654909101856  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                            None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3    ETH_delta=1201.2771424758992  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                            None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                            ...  ...                                                ...
70                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 27.620621132850648 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_5
* Git Hash: 1dfe23b

Exceptions:

```
                        exception  ...                                      initial_state
0     ETH_delta=953.5093399171142  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                            None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2   ETH_delta=-21413.048707865335  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3                            None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                            None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                            ...  ...                                                ...
70                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 27.290648194154105 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_4
* Git Hash: 1dfe23b

Exceptions:

```
                       exception  ...                                      initial_state
0                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4   ETH_delta=391.94964833718745  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                           ...  ...                                                ...
70               Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74               Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 27.691163925329842 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_3
* Git Hash: 1dfe23b

Exceptions:

```
                      exception  ...                                      initial_state
0                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3   ETH_delta=161489.1030373755  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4    ETH_delta=515.373268692714  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                          ...  ...                                                ...
70                         None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                         None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                         None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73              Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                         None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 27.25421226421992 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_2
* Git Hash: 1dfe23b

Exceptions:

```
                       exception  ...                                      initial_state
0                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2   ETH_delta=117.08668190959261  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3    ETH_delta=7775.439437044893  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4    ETH_delta=772.1809700744237  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                           ...  ...                                                ...
70                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72               Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 28.65462082227071 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_1
* Git Hash: 1dfe23b

Exceptions:

```
                       exception  ...                                      initial_state
0                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1   ETH_delta=384.68811192793675  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2   ETH_delta=14877.255667533233  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3   ETH_delta=4082.8192253124516  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4     ETH_delta=737.301802009339  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                           ...  ...                                                ...
70                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71               Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T23:03:46.416477
* Passed: True
* Time: 27.09282350540161 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T23:03:46.418089_0
* Git Hash: 1dfe23b

Exceptions:

```
                       exception  ...                                      initial_state
0   ETH_delta=2968.3462371722376  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1    ETH_delta=767.8686961652883  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2    ETH_delta=935.2883564568504  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3   ETH_delta=-856.0763679107223  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                           None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                           ...  ...                                                ...
70               Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                          None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74               Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    
# Experiment on 2021-02-10T22:33:29.788818
* Passed: True
* Time: 24.314744869867962 minutes
* Results folder: /home/bscholtz/workspace/reflexer/experiments/system_model_v3/experiment_monte_carlo
* Results ID: 2021-02-10T22:33:29.790394_0
* Git Hash: 1dfe23b

Exceptions:

```
                                            exception  ...                                      initial_state
0                        ETH_delta=2968.3462371722376  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1                         ETH_delta=767.8686961652883  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2   open         1.000000e+00\ntime         0.0000...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3   open         1.000000e+00\ntime         0.0000...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
4                                                None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
..                                                ...  ...                                                ...
70  open         1.000000e+00\ntime         0.0000...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
71  open         1.000000e+00\ntime         0.0000...  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
72                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
73                                               None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
74                                    Arb. CDP closed  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[75 rows x 8 columns]
```

Experiment metrics:


**Parameter subsets are spread across multiple experiments, with the results ID having the same timestamp and an extension for the subset index.**


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 5
* Timestep duration: 0.004 seconds
* Control parameters: ['controller_enabled', 'kp', 'ki', 'control_period', 'liquidity_demand_shock', 'arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 432
* Expected experiment duration: 622.08 minutes / 10.368 hours
    

```
sweeps={'controller_enabled': [True, False], 'kp': array([2.e-07, 1.e-06, 5.e-06]), 'ki': array([-5.e-09, -1.e-09, -2.e-10]), 'control_period': [3600, 14400, 25200], 'liquidity_demand_shock': [True, False], 'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    