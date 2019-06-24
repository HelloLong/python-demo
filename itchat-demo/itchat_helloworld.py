import itchat

bot = itchat.new_instance()
bot.s.proxies['http'] = 'socks5://127.0.0.1:1080'


bot.auto_login()
bot.send('hello, filehelper', toUserName='filehelper')

remote_admin = bot.search_friends(nickName='dc')[0]
# remote_admin.send('[START] OK!')
bot.send_msg('这是一个测试', toUserName=remote_admin["UserName"])