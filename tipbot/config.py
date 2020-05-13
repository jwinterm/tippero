#!/bin/python
#
# Cryptonote tipbot - configuration
# Copyright 2014 moneromooo
# Inspired by "Simple Python IRC bot" by berend
#
# The Cryptonote tipbot is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published
# by the Free Software Foundation; either version 2, or (at your option)
# any later version.
#

tipbot_name = "wowbux"

redis_host="127.0.0.1"
redis_port=6383

daemon_host = '127.0.0.1' # '127.0.0.1'
daemon_port = 34568 # 6060
wallet_host = '127.0.0.1'
wallet_port = 33333
wallet_update_time = 30 # seconds
withdrawal_fee=100000000000 # None defaults to the network default fee
min_withdraw_amount = 500000000000 # None defaults to the withdrawal fee
withdrawal_mixin=9
disable_withdraw_on_error = True
payment_confirmations = 6
tipbot_balance_cache_time = 35 # seconds
site_game_salt = ''
openalias_address = None
rpc_timeout = 180

admins = ["freenode:jwinterm", "reddit:jwinterm"]

# list of nicks to ignore for rains - bots, trolls, etc
no_rain_to_nicks = []

# commands used by other bots, to avoid "unknown command" complaints
silent_invalid_commands = {
  'freenode': [
    'price','worth','net','pools','calc','convert','val']
}

network_config = {
  'freenode': {
    'host': 'irc.freenode.net',
    'port': 6697,
    'login': tipbot_name,
    'delay': 0.4,
    'ssl': True,
    'sasl': True,
    'sasl_name': 'aeonbux',
    'welcome_line': 'Welcome to the freenode Internet Relay Chat Network',
    'timeout_seconds': 600,
    'channels': ['#wowbux', '#wownero'],
  },
  'reddit': {
    'subreddits': ['wownero'],
    'login': 'wowbux',
    'keyword': '/u/wowbux',
    'user_agent': tipbot_name,
    'update_period': 35,
    'load_limit': 100,
    'use_unread_api': True,
    'cache_timeout': 30,
  },
  'twitter': {
    'login': 'tipperome',
    'update_period': 90,
    'keyword': '@tipperome',
    'fs_location': '/tmp/twitter',
    'fs_prefix_tree': 2,
    'fs_hash_length': 32,
    'uri_base': 'http://127.0.0.1/',
    'prefix_when_linked': 'see: ',
  },
}

dice_min_multiplier=2
dice_max_multiplier=10
dice_edge = 0.01
dice_max_bet = 500
dice_min_bet = 0.001
# how much are we prepared to lose
dice_max_loss = 1000
# how much are we prepared to lose as a ratio of our current pot
dice_max_loss_ratio = 0.05

# see http://wizardofodds.com/games/blackjack/calculator/
blackjack_decks = 4
blackjack_split_to = 4
blackjack_insurance = True
blackjack_sidebets = ["over13", "under13", "pair", "climber", "buster", "splits", "match", "addup"]
blackjack_max_bet = 50
blackjack_min_bet = 0.001
# how much are we prepared to lose
blackjack_max_loss = 200
# how much are we prepared to lose as a ratio of our current pot
blackjack_max_loss_ratio = 0.05

bookie_fee = 0.2
bookie_min_bet = 1
bookie_max_bet = 100

pinata_start_amount = 0.75
pinata_base_target = 2
pinata_num_increments = 20
pinata_target_increment = 0.01
pinata_winner_base_share = 0.75
pinata_rain_remainder_share = 0.8
pinata_carry_remainder_share = 0.17

kitsune_max_bet = 1
kitsune_min_bet = 0.001
# how much are we prepared to lose
kitsune_max_loss = 35
# how much are we prepared to lose as a ratio of our current pot
kitsune_max_loss_ratio = 0.1

