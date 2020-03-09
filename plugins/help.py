from nonebot import on_command, CommandSession
import requests
import socket


@on_command('help', only_to_me=False)
async def ipinfo(session: CommandSession):
    await session.send('NB-Bot v1.0.2\n'
                       'by 单字汪\n'
                       'nonepage略作修改\n\n'
                       
                       '指令列表:\n'
                       '/ip 查询IP消息\n'
                       '/gfwdns 查询域名DNS信息\n'
                       '/gfwtcp 被墙检测\n')
