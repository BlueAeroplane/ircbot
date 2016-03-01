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
import json
from multiprocessing import Process
import time

cache = json.load(open('cache.json'))
dB = json.load(open('dB.json'))
config = json.load(open('config.json'))

def get_phrase():
    cache['number_of_words'] = random.randint(1, 12)
    json.dump(cache, open("cache.json", 'w'), indent=2)
    return " ".join([random.choice(dB['words']) for _ in range(cache['number_of_words'])])

def speak(sendmsg, message):
	sendmsg(message['replyto'], get_phrase())

#def speak_check(sendmsg, message): # Disabled because it doesn't work yet.
#	line_pending = get_phrase()
#	last_word = cache['number_of_words'] + 1
#	if dB['words2'] in line_pending:
#		speak(sendmsg, message) # Restart over, and get an non-duplicate sentence.
#	else:
#		sendmsg(message['replyto'], cache['line_pending'])

def words_autoshuffle():
	while True:
		time.sleep(config['autoshuffle_words'])
		words = random.shuffle(dB['words'])
		words = dB['words']
		json.dump(dB, open("dB.json", 'w'), indent=2)

