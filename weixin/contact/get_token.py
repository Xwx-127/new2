from weixin.contact.get_yaml import GetYaml
import requests

class GetToken:
    def get_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        conf = GetYaml().get_yaml()
        res = requests.get(url,
                           params={'corpid':conf['corpid'],
                                   'corpsecret':conf['corpsecret']})
        return res.json()['access_token']

if __name__ == '__main__':
    print(GetToken().get_token())