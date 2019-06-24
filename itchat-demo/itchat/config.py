import os, platform

VERSION = '1.2.32'
BASE_URL = 'https://login.weixin.qq.com'
OS = platform.system() #Windows, Linux, Darwin
DIR = os.getcwd()
DEFAULT_QR = 'QR.png'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'

# PROXIES = {'http':'http://公司代理IP地址:公司代理http端口号','https':'https://公司代理IP地址:公司代理https端口号'}
PROXIES = {'http':'http://公司代理IP地址:公司代理http端口号','https':'https://公司代理IP地址:公司代理https端口号'}