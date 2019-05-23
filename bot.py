# -*- coding: utf-8 -*-
import os
import telebot
import time
import random
import threading
from emoji import emojize
from telebot import types
from pymongo import MongoClient
import traceback

token = os.environ['TELEGRAM_TOKEN']
bot = telebot.TeleBot(token)


#client=MongoClient(os.environ['database'])
#db=client.
#users=db.users





def battle(game):
    if game['started']==False:
        game['started']=True
        for ids in game['players']:
            sendkb(game['players'][ids], game)


def sendkb(player, game):
    if player['die']!=1 and player['stun']<=0:
        kb=types.ReplyKeyboardMarkup()
        kb.add(types.KeyboardButton('Атаковать'), types.KeyboardButton('Блокировать'))
        gamestats=stats(game)
        bot.send_message(player['id'], gamestats, reply_markup=kb)
            
  
              
def createplayer(user):
    return {user.id:{
        'hp':1000,
        'stamina':15,
        'stun':0,
        'status':'rest',
        'action':None
    }
           }
              
              
            
def medit(message_text,chat_id, message_id,reply_markup=None,parse_mode=None):
    return bot.edit_message_text(chat_id=chat_id,message_id=message_id,text=message_text,reply_markup=reply_markup,
                                 parse_mode=parse_mode)   

print('7777')
bot.polling(none_stop=True,timeout=600)

