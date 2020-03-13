from nonebot import on_natural_language, NLPSession
import random

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
  if session.ctx['user_id'] == 604853027 and random.random() < 0.05:
    await session.send("把四鸟踢了!")