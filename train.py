# train.py
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO
from custom_env import Dota2SquirelEnv
from config import models_path

env = Dota2SquirelEnv()
env = DummyVecEnv([lambda: env])  # Упаковываем в Vectorized Env

# Создаем или загружаем модель
model = PPO("MlpPolicy", env, verbose=1, learning_rate=3e-4, n_steps=2048, ent_coef=0.01)

print("🚀 Начинаем обучение...")
model.learn(total_timesteps=100)
model.save(models_path + "/ppo_squirel_model")
print("✅ Модель сохранена!")
