import json
import requests
from nonebot import on_command, CommandSession
from torequests.utils import curlparse


@on_command('gfwtcp',aliases=('gt'), only_to_me=False)
async def _(session: CommandSession):
    args = session.current_arg_text.strip().split(' ')
    if len(args) == 2:
        try:
            curl_3 = """curl 'http://api.cherbim.com/check.php' -H 'Accept: */*' -H 'Referer: http://api.qingyushop.ml/' -H 'Origin: http://api.qingyushop.ml' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' --data 'ip={0}&port={1}' --compressed --insecure""".format(
                args[0], args[1])
            curl_4 = r"""curl 'http://api.qingyushop.ml/check.php' -H 'Cookie: __cfduid=dcda57671c2ae2a72ce54d68367ec16001565742656' -H 'Origin: http://api.qingyushop.ml' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: zh-CN,zh;q=0.9,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Accept: */*' -H 'Referer: http://api.qingyushop.ml/' -H 'X-Requested-With: XMLHttpRequest' -H 'Connection: keep-alive' --data 'ip={0}&port={1}' --compressed --insecure""".format(
                args[0], args[1])
            requests_3 = curlparse(curl_3)
            requests_4 = curlparse(curl_4)
            try:
                t3 = requests.request(**requests_3)
                t4 = requests.request(**requests_4)
                t_1 = json.loads(t3.text)
                t_2 = json.loads(t4.text)
                result_1 = ["国内检测结果：ICMP可用;TCP可用", "国内检测结果：ICMP可用;TCP不可用", "国内检测结果：ICMP不可用;TCP可用",
                            "国内检测结果：ICMP不可用;TCP不可用"]
                result_2 = ["国外检测结果：ICMP可用;TCP可用", "国外检测结果：ICMP可用;TCP不可用", "国外检测结果：ICMP不可用;TCP可用",
                            "国外检测结果：ICMP不可用;TCP不可用"]
                if t_1["icmp"] == "success":
                    if t_1["tcp"] == "success":
                        text_1 = result_1[0]
                    else:
                        text_1 = result_1[1]
                else:
                    if t_1["tcp"] == "success":
                        text_1 = result_1[2]
                    else:
                        text_1 = result_1[3]

                if t_2["icmp"] == "success":
                    if t_2["tcp"] == "success":
                        text_2 = result_2[0]
                    else:
                        text_2 = result_2[1]
                else:
                    if t_2["tcp"] == "success":
                        text_2 = result_2[2]
                    else:
                        text_2 = result_2[3]
                text_content = "{0}/{1}的检测结果为:".format(args[0], args[1]) + "\n" + text_1 + '\n' + text_2
                await session.send(text_content)
            except Exception as e:
                pass
        except:
            pass
    else:
        await  session.send('/gfwtcp [域名/IP] [端口]')


guolei = ''
haiwai = ''


@on_command('gfwdns', aliases=('gd'), only_to_me=False)
async def _(session: CommandSession):
    global haiwai, guolei
    args = session.current_arg_text.strip().split(' ')
    if len(args) == 1:
        if args[0] != '':
            html = requests.get(
                'https://myssl.com/api/v1/tools/dns_query?qtype=1&host=' + args[0] + '&qmode=-1').json()
            try:
                haiwai = '域名: ' + args[0] + '\n海外:\nIP ' + html['data']['01'][0]['answer']['records'][0][
                    'value'] + '\n' + html['data']['01'][0]['answer']['records'][0]['ip_location']
                guolei = '\n国内:\nIP ' + html['data']['86'][0]['answer']['records'][0]['value'] + '\n' + \
                         html['data']['86'][0]['answer']['records'][0]['ip_location']
                # await session.send(haiwai+guolei)
            except:
                haiwai = '域名: ' + args[0] + '\n海外:\nIP ' + html['data']['01'][0]['answer']['error']
                # await session.send(haiwai + guolei)
                try:
                    guolei = '\n国内:\nIP ' + html['data']['86'][0]['answer']['records'][0]['value'] + '\n' + \
                             html['data']['86'][0]['answer']['records'][0]['ip_location']
                    # await session.send(haiwai + guolei)
                except:
                    guolei = '\n国内:\nIP ' + html['data']['86'][0]['answer']['error']
                    # await session.send(haiwai + guolei)
            finally:
                await session.send(haiwai + guolei)
        else:
            await  session.finish('/gfwdns [域名]')
