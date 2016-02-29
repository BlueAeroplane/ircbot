# 12 year old simulator - An IRC bot that simulates an annoying 12 year old.
# Copyright (C) 2016 Nathaniel Olsen

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import random

words = ['fgt', 'm8', 'u', 'wot', 'penis', 'me', 'is', 'are', 'gay', 'ass', 'lookin', 'minecraft', 'fk', 'dank', 'memes', 'a', 'was', 'me', 'shit', 'piss', 'bitch', 'you', 'off', 'on', 'mum', 'quickscope', 'oooh', 'oh', 'motherfucka', 'such', 'many', '( ͡° ͜ʖ ͡°)', 'noscope', 'l33t', 'n0scope', 'oooooooohooooh', 'smoke', 'weed', 'everyday', 'fag', 'faggot', 'cunt', 'big', 'yeaaaaaaaa', 'sex', 'this', 'make', 'ho', 'suck', 'my', 'illuminati', 'confirmed', '9/11', 'r8', '8/8', 'as', 'at', 'am', 'homo', 'queer', 'lol', 'XDXDXDXD', 'lame', 'GG', 'bruh', 'bro', 'mad', 'lets', 'have', 'cancer', 'noone', 'cares', 'MLG', 'pro', 'let', 'eat', 'asshole', 'anus', 'anal', 'mom', 'dat', 'rectum', 'pepe', 'doritos', 'mountain', 'dew', 'hi', 'hey', 'bye']

def get_phrase():
    number_of_words = random.randint(1, 12)
    return " ".join([random.choice(words) for _ in range(number_of_words)])

def speak(sendmsg, message):
    sendmsg(message['replyto'], get_phrase())
