from nonebot import on_natural_language, NLPSession, on_command, CommandSession, IntentCommand
import random
import conn
import requests

redis = conn.REDIS
cursor = conn.MYSQL.cursor()

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):
  if session.ctx['user_id'] == 1596738425:
    return
  if session.ctx['user_id'] == 1441297016:
    if random.random() < 0.01 and redis.set("1441297016_warning", "0", ex = 600, nx=True):
      r = requests.get("https://chp.shadiao.app/api.php",params={'from': 'cn_syuico'})
      await session.send(r.text, at_sender=True)

@on_natural_language(only_to_me=False)
async def _(session: NLPSession):  
  if session.ctx['user_id'] == 1596738425:
    return
  if cursor.execute("select * from `jiji_group` where `user_id`= %s", session.ctx["user_id"]) > 0:
    result = cursor.fetchone()
    if random.random() < result['random'] and redis.set(str(result['user_id'])+"_warning", "0", ex = 600, nx=True):
      await session.send(result['note'], at_sender = result['at_me'] == 1)


@on_natural_language(keywords={'江叶', '浆液', '桨叶', '浆叶'}, only_to_me=False)
async def _(session: NLPSession):
  if session.ctx['user_id'] == 1596738425:
    return
  if redis.set("1252584289_warning", "0", ex = 600, nx=True):
    await session.send("[CQ:at,qq=1252584289]  有人偷偷说你坏话")

@on_natural_language(keywords={'把四鸟踢了'}, only_to_me=False)
async def _(session: NLPSession):
  if session.ctx['user_id'] == 1596738425:
    return
  if redis.set("604853027_warning", "0", ex = 600, nx=True):
    return IntentCommand(100.0, ('repeat',), None, session.msg)

@on_command('repeat', only_to_me=False)
async def _(session: CommandSession):
  if session.ctx['user_id'] == 1596738425:
    return
  await session.send(session.current_arg)

@on_command('clear_siniao_cache', only_to_me=False)
async def _(session: CommandSession):
  if session.ctx['user_id'] == 1596738425:
    return
  redis.delete("604853027_warning")
  await session.send("done")
  
@on_command('my_notice', aliases=('我的舔狗'), only_to_me=False)
async def _(session: CommandSession):
  if session.ctx['user_id'] == 1596738425:
    return
  results = session.current_arg_text.split()
  flag = True

  present = cursor.execute("select * from `jiji_group` where `user_id`= %s", session.ctx["user_id"]) > 0

  if present:
    value = cursor.fetchone()
  else:
    value = {'user_id': session.ctx["user_id"], 'note': "", 'random': 0.5, 'at_me': 0}

  if len(results) > 0:
    i = 0
    for result in results:
      if i == 0:
        value['note'] = result
        i += 1
      elif i == 1:
        random = float(result)
        if random > 0 and random <= 1:
          value['random'] = random
          i += 1
        else:
          flag = False
      elif i == 2:
        at_me = int(result)
        if at_me == 0 or at_me == 1:
          value['at_me'] = at_me
          i += 1
        else:
          flag = False
      else:
        break
  else:
    flag = False

  if flag:
    if present:
      sql_res = cursor.execute("UPDATE `jiji_group` SET `note`=%s, `random`=%s, `at_me`=%s WHERE `user_id`=%s", (value['note'], value['random'], value['at_me'], value["user_id"]))
    else:
      sql_res = cursor.execute("INSERT INTO `jiji_group` (`user_id`, `note`, `random`, `at_me`) VALUES (%s, %s, %s, %s)", (value["user_id"], value['note'], value['random'], value['at_me']))
    
    if sql_res > 0:
      conn.MYSQL.commit()
      await session.send("done")
    else:
      await session.send("数据库更新失败，请联系江叶debug")
  else:
    await session.send("用法: my_notice(或 我的舔狗) 参数1 参数2(可选) 参数3(可选)\n参数1: 当你说话时要触发机器人说的内容。\n参数2: 你说话触发机器人响应的概率，默认0.5(需要是一个大于0，小于等于1的小数) \n参数3: 机器人响应是否要@你，默认为0.(0或1，0为不@，1为@)")
  