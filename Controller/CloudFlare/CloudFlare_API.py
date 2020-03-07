import requests

from Config.Config import base_url, headers, root_domain, domain


class CloudFlare_Class:
    def __init__(self):
        self.name = domain
        self.zone_ID = self.get_Zoneid()
        self.dns_ID = self.get_Dnsid()

    def get_Zoneid(self):
        response = requests.get(base_url + '?name=' + root_domain, headers=headers).json()
        return response['result'][0]['id']

    def get_Dnsid(self):
        response = requests.get(
            base_url + '/' + self.get_Zoneid() + '/dns_records?type=CNAME&name=' + domain + '&page=1&per_page=20&order=type&direction=desc&match=all',
            headers=headers).json()
        return response['result'][0]['id']

    def put_Data(self, content):
        post_Data = {
            'type': 'CNAME',
            'name': self.name,
            'content': content,
            'ttl': 1,
        }
        result = requests.put(
            'https://api.cloudflare.com/client/v4/zones/' + self.zone_ID + '/dns_records/' + self.dns_ID,
            json=post_Data, headers=headers).json()
        return result['success'], result['result']['content']
