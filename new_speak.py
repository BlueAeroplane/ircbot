# 12 year old simulator - An IRC bot that simulates an annoying 12 year old.
# Copyright (C) 2016 Nathaniel Olsen

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# I know this is fucking ugly, but it's something until I find a better and cleaner method.

import random
import bot

wordsdB = ['fgt', 'm8', 'u', 'wot', 'penis', 'me', 'is', 'are', 'gay', 'ass', 'lookin', 'minecraft', 'fk', 'dank', 'memes', 'a', 'was', 'me', 'shit', 'piss', 'bitch', 'you', 'off', 'on', 'mum', 'quickscope', 'oooh', 'oh', 'motherfucka', 'such', 'many', '( ͡° ͜ʖ ͡°)', 'noscope', 'l33t', 'n0scope', 'oooooooohooooh', 'smoke', 'weed', 'everyday', 'fag', 'faggot', 'cunt', 'big', 'yeaaaaaaaa', 'sex', 'this', 'make', 'ho', 'suck', 'my']

def speak():
    numlist = ['1','2','3','4','5', '6', '7', '8', '9', '10']
    number_of_words = random.choice(numlist)
    if number_of_words == "1":
    	bot.sendmsg(bot.message['replyto'], '%s' % (random.choice(wordsdB)))
    elif number_of_words == "2":
    	bot.sendmsg(bot.message['replyto'], '%s %s' % (random.choice(wordsdB),random.choice(wordsdB)))
    elif number_of_words == "3":
    	bot.sendmsg(bot.message['replyto'], '%s %s %s' % (random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB)))
    elif number_of_words == "4":
    	bot.sendmsg(bot.message['replyto'], '%s %s %s %s' % (random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB)))
    elif number_of_words == "5":
    	bot.sendmsg(bot.message['replyto'], '%s %s %s %s %s' % (random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB)))
    elif number_of_words == '6':
    	bot.sendmsg(bot.message['replyto'], '%s %s %s %s %s %s' % (random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB)))
    elif number_of_words == '7':
    	bot.sendmsg(bot.message['replyto'], '%s %s %s %s %s %s %s' % (random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB)))
    elif number_of_words == '8':
    	bot.sendmsg(bot.message['replyto'], '%s %s %s %s %s %s %s %s' % (random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB)))
    elif number_of_words == '9':
    	bot.sendmsg(bot.message['replyto'], '%s %s %s %s %s %s %s %s %s' % (random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB)))
    elif number_of_words == '10':
    	bot.sendmsg(bot.message['replyto'], '%s %s %s %s %s %s %s %s %s %s' % (random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB),random.choice(wordsdB)))
