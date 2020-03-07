from nonebot import on_command, CommandSession

from Config.Config import main_server_content, backup_server_content
from Controller.CloudFlare.CloudFlare_API import CloudFlare_Class as CLA

@on_command('change_server', aliases=('cs'), only_to_me=False)
async def _(session: CommandSession):
    args = session.current_arg_text.strip().split(' ')
    if len(args) == 1:
        PUT = CLA()
        try:
            if args[0] == 'akko':
                result = '服务器已切换到: ' + PUT.put_Data(backup_server_content)[1]
                await session.send(result)
            if args[0] == 'pqs':
                result = '服务器已切换到: ' + PUT.put_Data(main_server_content)[1]
                await session.send(result)
        except Exception as e:
            await  session.finish(str(e))
