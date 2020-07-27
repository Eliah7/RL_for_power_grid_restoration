from gym.envs.registration import register
 
register(id='PowerGridRestoration-v0', 
    entry_point='gym_power_grid_restoration:PowerGridRestorationEnv', 
)