# coding:utf-8
from wxpy import *

robot = bot.Bot()
# api可直接用
tuling = Tuling(api_key='****************************')
@robot.register(msg_types=TEXT)
def auto_reply_all(msg):
	tuling.do_reply(msg)
robot.join()
