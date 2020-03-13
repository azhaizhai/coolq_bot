from nonebot import on_command, CommandSession, on_natural_language, NLPSession, IntentCommand

@on_command("remove_siniao", only_to_me = False)
async def _(session: CommandSession):
  await session.send("把四鸟踢了！")

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
    # 只复读群消息，与没有对机器人说的话
    if session.ctx['user_id'] == "1252584289":
      return IntentCommand(60.0, 'remove_siniao', args={'message': session.msg})