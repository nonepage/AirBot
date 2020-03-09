from nonebot import on_command, CommandSession
import requests
import socket
import asyncio

@on_command('ip', only_to_me=False)
async def ipinfo(session: CommandSession):
    async def get_ipinfo(ipaddr):
        addr = socket.gethostbyname(ipaddr)
        data = requests.get('http://ip-api.com/json/' + addr).json()
        country = data['country']
        area = data['isp']
        report = 'IP地址：' + addr + '\n' + 'Country：' + country + '\n' + 'ISP：' + area
        await session.send(report)

    ipaddress = session.get('ipaddress', prompt='请发送需要查询的IP地址.')
    ipinfo_report = get_ipinfo(ipaddress)
    asyncio.create_task(ipinfo_report)



@ipinfo.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()
    if session.is_first_run:
        if stripped_arg:
            session.state['ipaddress'] = stripped_arg
        return
    if not stripped_arg:
        session.pause('查询地址不能为空，请重新输入.')
    session.state[session.current_key] = stripped_arg


