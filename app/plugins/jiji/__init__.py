from nonebot import on_command, CommandSession, message

@on_command("remove_siniao", only_to_me = False)
async def _(session: CommandSession):
  await session.send("把四鸟踢了！")