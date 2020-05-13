#!/bin/python
#
# Cryptonote tipbot - dice commands
# Copyright 2014,2015 moneromooo
#
# The Cryptonote tipbot is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2, or (at your option)
# any later version.
#

import sys
import os
import redis
import hashlib
import time
import string
import random
import requests
import tipbot.config as config
from tipbot.log import log_error, log_warn, log_info, log_log
import tipbot.coinspecs as coinspecs
from tipbot.user import User
from tipbot.link import Link
from tipbot.utils import *
from tipbot.command_manager import *
from tipbot.redisdb import *


priceurl = "https://api.altex.exchange/v1/ticker"
networkurl = "http://127.0.0.1:34568/json_rpc"


def Network(link,cmd):
  identity=link.identity()
  try:
    payload = '{"jsonrpc":"2.0", "id":"0", "method":"get_info"}' 
    headers = {"Content-Type":"application/json"}
    r=requests.post(networkurl, data=payload, headers=headers)
    j=r.json()
  except Exception,e:
    pass
  try:
    height=j["result"]["height"]
    diff=j["result"]["difficulty"]
    hashrate=float(diff)/300
    link.send("The current block height is {0:,}, difficulty is {1:.2e}, and hashrate is {2:,} kh/s".format(height, diff, int(hashrate/1e3)))
  except:
    link.send("Something borked -_-")

def Mine(link,cmd):
  identity=link.identity()
  try:
    hr=float(cmd[1])
    try:
      payload = '{"jsonrpc":"2.0", "id":"0", "method":"getlastblockheader"}' 
      headers = {"Content-Type":"application/json"}
      r=requests.post(networkurl, data=payload, headers=headers)
      j=r.json()
      diff=float(j["result"]["block_header"]["difficulty"])
      lbr=float(j["result"]["block_header"]["reward"])
      ttb = diff/hr
      link.send("The estimated time to find a block with {0:.2f} kh/s at diff {1:.2e} is {2:.2f} days. On average you will earn {3:.2f} WOW per day".format(hr/1e3, diff, ttb/(60*60*24), (lbr/1e11)/(ttb/(60*60*24))))
    except:
      link.send("Something b0rked -_-")
  except:
    link.send("Mining is for suckers...")

def Mempool(link,cmd):
  identity=link.identity()
  try:
    payload = '{"jsonrpc":"2.0", "id":"0", "method":"get_info"}' 
    headers = {"Content-Type":"application/json"}
    r=requests.post(networkurl, data=payload, headers=headers)
    j=r.json()
  except Exception,e:
    pass
  try:
    txs=j["result"]["tx_pool_size"]
    link.send("The current number of txs in mempool is: {0}".format(txs))
  except:
    link.send("Something borked -_-")

def Price(link,cmd):
   try:
       r = requests.get(priceurl)
       j = r.json()
       data=j['data']
       lastbtc=float(data['BTC_WOW']['last'])
       volbtc=float(data['BTC_WOW']['volume'])
       chgbtc=float(data['BTC_WOW']['change'])
       lastxmr=float(data['XMR_WOW']['last'])
       volxmr=float(data['XMR_WOW']['volume'])
       chgxmr=float(data['XMR_WOW']['change'])
       link.send("Altex at {0:.8f} BTC on {1:6f} BTC vol, changed {2:.2f} over 24h".format(lastbtc, volbtc, chgbtc))
       link.send("Altex at {0:.8f} XMR on {1:6f} XMR vol, changed {2:.2f} over 24h".format(lastxmr, volxmr, chgxmr))
   except:
       link.send("Error retrieving data from Altex")

def NetinfoHelp(link):
  link.send_private("The netinfo module gives network and price info about %s" % coinspecs.name)
  link.send_private("Basic usage: !network")
  link.send_private("Basic usage: !mine <hashrate>")
  link.send_private("Basic usage: !mempool")
  link.send_private("Basic usage: !price")


RegisterModule({
  'name': __name__,
  'help': NetinfoHelp,
})
RegisterCommand({
  'module': __name__,
  'name': 'network',
  'function': Network,
  'registered': False,
  'help': "get network info"
})
RegisterCommand({
  'module': __name__,
  'name': 'mine',
  'function': Mine,
  'registered': False,
  'help': "get predicted mining rewards"
})
RegisterCommand({
  'module': __name__,
  'name': 'mempool',
  'function': Mempool,
  'registered': False,
  'help': "get number of txs in mempool"
})
RegisterCommand({
  'module': __name__,
  'name': 'price',
  'function': Price,
  'registered': False,
  'help': "get price info"
})


