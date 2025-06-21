# custom_env.py

import gym
from gym import spaces
import numpy as np
from gsi_reader import get_game_state, extract_state
from action_executor import execute_action
from config import ACTION_SPACE, STATE_SIZE, REWARD_WIN, REWARD_DEATH, REWARD_ALIVE

class Dota2SquirelEnv(gym.Env):
    metadata = {'render_modes': ['human']}

    def __init__(self):
        super(Dota2SquirelEnv, self).__init__()
        self.action_space = spaces.Discrete(ACTION_SPACE)
        self.observation_space = spaces.Box(low=0, high=1, shape=(STATE_SIZE,), dtype=np.float32)
        self.last_health = 100
        self.episode_step = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.episode_step = 0
        while True:
            state = get_game_state()
            if state and "hero" in state:
                return np.array(extract_state(state), dtype=np.float32)
            print("[Ожидание начала игры...]")

    def step(self, action):
        self.episode_step += 1
        execute_action(action)

        game_state = get_game_state()
        if not game_state:
            return np.zeros(STATE_SIZE), 0, True, {}

        done = False
        reward = REWARD_ALIVE

        hero = game_state.get("hero", {})
        current_health = hero.get("health", 0)
        is_alive = hero.get("alive", True)

        if not is_alive:
            reward = REWARD_DEATH
            done = True
        else:
            damage_taken = self.last_health - current_health
            reward -= damage_taken * 0.1
            self.last_health = current_health

        next_state = np.array(extract_state(game_state), dtype=np.float32)
        info = {}
        return next_state, reward, done, info

    def render(self, mode='human'):
        pass

    def close(self):
        pass
