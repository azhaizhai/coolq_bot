from nonebot import on_natural_language, NLPSession
import random
import redis

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
  conn = redis.Redis(host='127.0.0.1', port=6379)
  if session.ctx['user_id'] == 604853027 and random.random() < 0.5:
    if conn.set("604853027_warning", "0", ex = 600, nx=True):
      await session.send("把四鸟踢了!")