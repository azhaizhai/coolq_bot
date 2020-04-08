from nonebot import on_command, CommandSession
from datetime import timedelta

from .data_source import picture_research_results

SESSION_RUN_TIMEOUT = timedelta(seconds=30)
@on_command('以图搜番', only_to_me = False)
async def search_picture(session: CommandSession):
  if session.ctx['user_id'] == 1596738425:
    return
  pictures = session.get('pictures', prompt='请发送要搜索的图片(请在30秒内完成操作，否则会话关闭)')
  results = await picture_research_results(pictures[0])
  await session.send(results, at_sender=True)

@search_picture.args_parser
async def _(session: CommandSession):

    stripped_arg = session.current_arg_images

    if session.is_first_run:
        if stripped_arg:
            session.state['pictures'] = stripped_arg
        return

    if not stripped_arg:
        session.pause('要查询的图片不存在，请重新输入')

    session.state[session.current_key] = stripped_arg