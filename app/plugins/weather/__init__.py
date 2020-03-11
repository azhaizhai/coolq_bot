from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg

from .data_source import get_weather_of_city

@on_command('weather', aliases=('天气', '天气预报', '查天气'), only_to_me=False)
async def weather(session: CommandSession):
    city = session.get('city', prompt='你想查询哪个城市的天气呢？')
    weather_report = await get_weather_of_city(city)
    await session.send(weather_report)

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

@on_natural_language(keywords={'天气'}, only_to_me = False)
async def _(session: NLPSession):
  stripped_msg = session.msg_text.strip()
  words = posseg.lcut(stripped_msg)

  city = None
  # 遍历 posseg.lcut 返回的列表
  for word in words:
      # 每个元素是一个 pair 对象，包含 word 和 flag 两个属性，分别表示词和词性
      if word.flag == 'ns':
          # ns 词性表示地名
          city = word.word
          return IntentCommand(90.0, 'weather', current_arg=city)
