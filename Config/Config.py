base_url = 'https://api.cloudflare.com/client/v4/zones'
domain = 'cn-cu-1.sgdns.club'  # 二级域名
root_domain = 'sgdns.club'  # 根域名
headers = {
    'X-Auth-Email': '@qq.com',  # CloudFlare邮箱
    'X-Auth-Key': '',  # CloudFlare Key
    'Content-Type': 'application/json'
}

main_server_ip = ['103.56.60.185', '222.186.20.44', '223.112.227.245']
main_server_port = 46760
main_server_content = '100cu-pqs.sgdns.club'

backup_server_port = 61119
backup_server_content = '300cu-akko.sgdns.club'

ftqq_sckey = ''  # http://sc.ftqq.com/
ftqq_send_url = 'https://sc.ftqq.com/'
