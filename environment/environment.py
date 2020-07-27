import gym
from gym import error, spaces, utils
from gym.utils import seeding
 
class PowerGridRestorationEnv(gym.Env):  
    metadata = {'render.modes': ['human']}   
    def __init__(self):
        pass
 
    def step(self, action):
        pass
 
    def reset(self):
        pass
 
    def render(self, mode='human', close=False):
        pass


if __name__ == "__main__":
    print(PowerGridRestorationEnv())