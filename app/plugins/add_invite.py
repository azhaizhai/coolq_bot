from nonebot import on_request, RequestSession

@on_request('group')
async def _(session: RequestSession):
    if session.ctx['sub_type'] == 'invite' and session.ctx['user_id'] == "1252584289":
        await session.approve()
        return

@on_request('friend')
async def _(session: RequestSession):
    if session.ctx['comment'] == '搞事搞事搞事':
        await session.approve()
        return

    await session.reject('请说暗号')