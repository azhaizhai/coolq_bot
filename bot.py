from os import path
import nonebot
import config

if __name__ == '__main__':
    nonebot.init(config)
    nonebot.load_plugins(
      path.join(path.dirname(__file__), 'app', 'plugins'),
        'app.plugins'
    )
    nonebot.run()

    nonebot.on_message
    async def _(ctx: session.ctx):
      if ctx['user_id'] == "1252584289":
        ctx['message'] = "remove_siniao"