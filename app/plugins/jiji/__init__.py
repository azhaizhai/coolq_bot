from nonebot import on_natural_language, NLPSession


@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
  if session.ctx['user_id'] == 1252584289:
    await session.send("把四鸟踢了!")