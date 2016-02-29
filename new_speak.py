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

words = ['ass', 'let', 'piss', 'hey', 'at', 'off', 'came', 'me', 'oooooooohooooh', 'weed', 'as', 'cum', 'n0scope', 'many', 'asshole', 'big', 'bitch', 'lookin', 'are', 'my', 'is', 'pepe', 'this', 'l33t', 'such', 'minecraft', 'am', 'u', 'queer', 'homo', 'anal', 'quickscope', 'mum', 'a', 'bro', 'oooh', 'you', 'oh', 'lame', 'sex', 'r8', '9/11', 'eat', 'fgt', 'wot', 'hi', 'bruh', 'on', 'dat', 'XDXDXDXD', 'm8', 'GG', 'me', 'mountain', 'cunt', 'doritos', '8/8', 'gay', 'faggot', 'ho', 'cummed', 'was', 'pro', 'fk', 'anus', 'smoke', 'motherfucka', 'dank', 'noscope', 'lets', '( ͡° ͜ʖ ͡°)', 'confirmed', 'have', 'penis', 'dew', 'MLG', 'illuminati', 'mad', 'fag', 'noone', 'memes', 'cares', 'bye', 'cancer', 'make', 'shit', 'suck', 'rectum', 'lol', 'everyday', 'mom', 'yeaaaaaaaa']

def get_phrase():
    number_of_words = random.randint(1, 12)
    return " ".join([random.choice(words) for _ in range(number_of_words)])

def speak(sendmsg, message):
    sendmsg(message['replyto'], get_phrase())