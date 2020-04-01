from nonebot import on_natural_language, NLPSession
import random
import conn

redis = conn.REDIS

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
  if session.ctx['user_id'] == 604853027:
    if random.random() < 0.1 and redis.set("604853027_warning", "0", ex = 600, nx=True):
      await session.send("把四鸟踢了!")
  elif session.ctx['user_id'] == 1821703949:
    if random.random() < 0.5 and redis.set("1821703949_warning", "0", ex = 600, nx=True):
      await session.send("毛玉哥哥我爱你＾3＾")

@on_natural_language(keywords={'江叶', '浆液', '桨叶'})
async def _(session: NLPSession):
  if redis.set("1252584289_warning", "0", ex = 600, nx=True):
    await session.send("[CQ:at,qq=1252584289]  有人偷偷说你坏话")
  