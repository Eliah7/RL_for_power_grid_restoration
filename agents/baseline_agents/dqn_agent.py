import gym
import environment as PEnv
from stable_baselines import DQN
from stable_baselines.common.evaluation import evaluate_policy


# Create environment
jar_file = "/Users/elia/Documents/Projects/Professional Jobs/rl_power_grid_restoration/environment/assets/RLGCJavaServer0.93.jar"
case_files_array = []
java_port = 25332
case_files_array.append(
    '/Users/elia/Documents/Projects/Professional Jobs/rl_power_grid_restoration/environment/testData/IEEE39/IEEE39bus_multiloads_xfmr4_smallX_v30.raw')
case_files_array.append(
    '/Users/elia/Documents/Projects/Professional Jobs/rl_power_grid_restoration/environment/testData/IEEE39/IEEE39bus_3AC.dyr')
dyn_config_file = '/Users/elia/Documents/Projects/Professional Jobs/rl_power_grid_restoration/environment/testData/IEEE39/json/IEEE39_dyn_config.json'
rl_config_file = '/Users/elia/Documents/Projects/Professional Jobs/rl_power_grid_restoration/environment/testData/IEEE39/json/IEEE39_RL_loadShedding_3motor_continuous.json'

env = PEnv.PowerDynSimEnv(case_files_array, dyn_config_file,
                     rl_config_file, jar_file, java_port)

# Instantiate the agent
model = DQN('MlpPolicy', env, learning_rate=1e-3,
            prioritized_replay=True, verbose=1)

# Train the agent
model.learn(total_timesteps=int(2e5))
# Save the agent
model.save("dqn_PowerGridRestoration")
del model  # delete trained model to demonstrate loading

# Load the trained agent
model = DQN.load("dqn_PowerGridRestoration")

# Evaluate the agent
mean_reward, std_reward = evaluate_policy(
    model, model.get_env(), n_eval_episodes=10)

print("******* MEAN REWARD ******* ", mean_reward)

# Enjoy trained agent
obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    # env.render()
