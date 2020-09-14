from gym.envs.registration import register

register(
    id='trading-v0',
    entry_point='gym_trading.envs:TradingEnv',
    max_episode_steps=1000,
)
