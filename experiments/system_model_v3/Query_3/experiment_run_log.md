
# Experiment on 2021-02-26T10:59:59.004278
* Passed: True
* Time: 6.484975802898407 minutes
* Results folder: /home/aclarkdata/repos/reflexer/experiments/system_model_v3/Query_3
* Results ID: 2021-02-26T10:59:59.004623
* Git Hash: d702f40

Exceptions:

```
  exception  ...                                      initial_state
0      None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
1      None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
2      None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...
3      None  ...  {'cdp_metrics': {}, 'optimal_values': {}, 'sim...

[4 rows x 8 columns]
```

Experiment metrics:


****


* Number of timesteps: 4320 / 180.0 days
* Number of MC runs: 1
* Timestep duration: 0.004 seconds
* Control parameters: ['arbitrageur_considers_liquidation_ratio', 'rescale_target_price']
* Number of parameter combinations: 4
* Expected experiment duration: 1.1520000000000001 minutes / 0.019200000000000002 hours
    

```
sweeps={'arbitrageur_considers_liquidation_ratio': [True, False], 'rescale_target_price': [True, False]}
```

    