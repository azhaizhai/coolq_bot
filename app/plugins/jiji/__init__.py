from nonebot import on_natural_language, NLPSession, on_command, CommandSession, IntentCommand
import random
import conn
import requests

redis = conn.REDIS

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
  if session.ctx['user_id'] == 604853027:
    if random.random() < 0.1 and redis.set("604853027_warning", "0", ex = 600, nx=True):
      await session.send("把四鸟踢了!")
  elif session.ctx['user_id'] == 1821703949:
    if random.random() < 0.5 and redis.set("1821703949_warning", "0", ex = 600, nx=True):
      await session.send("毛玉哥哥我爱你＾3＾")
  elif session.ctx['user_id'] == 564679098:
    if random.random() < 0.25 and redis.set("564679098_warning", "0", ex = 600, nx=True):
      await session.send("sb鸡头")
  elif session.ctx['user_id'] == 1441297016:
    if random.random() < 0.5 and redis.set("1441297016_warning", "0", ex = 600, nx=True):
      r = requests.get("https://chp.shadiao.app/api.php",params={'from': 'cn_syuico'})
      await session.send(r.text, at_sender=True)
  elif session.ctx['user_id'] == 1213825963:
    if random.random() < 0.99 and redis.set("1213825963_warning", "0", ex = 600, nx=True):
      await session.send("sb啊初")

@on_natural_language(keywords={'江叶', '浆液', '桨叶', '浆叶'}, only_to_me=False)
async def _(session: NLPSession):
  if redis.set("1252584289_warning", "0", ex = 600, nx=True):
    await session.send("[CQ:at,qq=1252584289]  有人偷偷说你坏话")

@on_natural_language(keywords={'把四鸟踢了'}, only_to_me=False)
async def _(session: NLPSession):
  if redis.set("604853027_warning", "0", ex = 600, nx=True):
    return IntentCommand(100.0, ('repeat',), None, session.msg)

@on_command('repeat', only_to_me=False)
async def _(session: CommandSession):
  await session.send(session.current_arg)

@on_command('clear_siniao_cache', only_to_me=False)
async def _(session: CommandSession):
  redis.delete("604853027_warning")
  await session.send("done")
  
  