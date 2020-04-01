from nonebot import on_command, CommandSession
from datetime import timedelta

from .mud_link import TCPClient

@on_command('#玩泥巴')
async def play_mud(session: CommandSession):
    await session.send(results, at_sender=True)

@weather.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    session.state[session.current_key] = stripped_arg