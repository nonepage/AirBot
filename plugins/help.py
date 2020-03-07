from nonebot import on_command, CommandSession
import requests
import socket


@on_command('help', only_to_me=False)
async def ipinfo(session: CommandSession):
    await session.send('幽忆云 Bot 1.0.1\n'
                       'by 单字汪\n\n'
                       '指令列表:\n'
                       '/ip 查询IP消息\n'
                       '/gfwdns 查询域名DNS信息\n'
                       '/gfwtcp 被墙检测\n')
