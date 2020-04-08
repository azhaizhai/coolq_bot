from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand
from jieba import posseg
import requests

request_from = {'from': 'cn_syuico'}
nmsl_level = {'level': 'min'}

@on_command('彩虹屁', aliases=('夸夸我'), only_to_me=False)
async def chp(session: CommandSession):
  if session.ctx['user_id'] == 1252584289:
    return
  r = requests.get("https://chp.shadiao.app/api.php",params=request_from)
  await session.send(r.text)

@on_command('朋友圈文案', only_to_me=False)
async def jt(session: CommandSession):
  if session.ctx['user_id'] == 1252584289:
    return
  r = requests.get("https://pyq.shadiao.app/api.php",params=request_from)
  await session.send(r.text)

@on_command('毒鸡汤', only_to_me=False)
async def djt(session: CommandSession):
  if session.ctx['user_id'] == 1252584289:
    return
  r = requests.get("https://du.shadiao.app/api.php",params=request_from)
  await session.send(r.text)

@on_command('口吐莲花')
async def ktlh(session: CommandSession):
  if session.ctx['user_id'] == 1252584289:
    return
  params = request_from
  if session.ctx['message_type'] == "private":
    r = requests.get("https://nmsl.shadiao.app/api.php", params.update(nmsl_level))
    await session.send(r.text)

@on_command('火力全开')
async def hlqk(session: CommandSession):
  if session.ctx['user_id'] == 1252584289:
    return
  if session.ctx['message_type'] == "private":
    r = requests.get("https://nmsl.shadiao.app/api.php", params=request_from)
    await session.send(r.text)

@on_natural_language(keywords={'毒鸡汤'})
async def _(session: NLPSession):
  if session.ctx['user_id'] == 1252584289:
    return
  return IntentCommand(90.0, '毒鸡汤')

@on_natural_language(keywords={'彩虹屁', '夸'})
async def _(session: NLPSession):
  if session.ctx['user_id'] == 1252584289:
    return
  return IntentCommand(90.0, '彩虹屁')

@on_natural_language(keywords={'文案'})
async def _(session: NLPSession):
  if session.ctx['user_id'] == 1252584289:
    return
  return IntentCommand(90.0, '朋友圈文案')