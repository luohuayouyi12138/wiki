'''
MIT License

author: 
落花有意12138(https://zh.wikisource.org/wiki/User:%E8%90%BD%E8%8A%B1%E6%9C%89%E6%84%8F12138)
MediaWiki(https://mediawiki.org/)
'''
from typing_extensions import ParamSpec
import requests

S = requests.Session()
apiUrl = "https://zh.wikisource.org/w/api.php"

def getToken(type: str):
    PARAMS = {
        "action": "query",
        "meta": "tokens",
        "type": type,
        "format": "json"
    }
    R = S.get(url=apiUrl, params=PARAMS)
    DATA = R.json()
    TOKEN = DATA['query']['tokens'][type+'token']

    return TOKEN

def login(name: str, password: str, token: str):
    PARAMS = {
        "action": "login",
        "lgname": name,
        "lgpassword": password,
        "lgtoken": token,
        "format": "json"
    }
    R = S.post(apiUrl, data=PARAMS)
    return R

def edit(title: str, text: str, token: str, summary: str="此次编辑为机器人编辑"):
    PARAMS = {
        "action": "edit",
        "title": title,
        "token": token,
        "text": text,
        "format": "json",
        "bot": True,
        # "createonly": True,#当存在时不要编辑页面
        "summary": summary#编辑摘要
    }
    R = S.post(apiUrl, data=PARAMS)
    DATA = R.json()

    return DATA

def get(title: str):
    PARAMS = {
        "action": "parse",
        "format": "json",
        "page": title,
        "prop": "text",
        "formatversion": "2"
    }
    R = S.post(apiUrl, data=PARAMS)
    return R