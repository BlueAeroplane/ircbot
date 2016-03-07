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
    message = []
    for i in range(cache['number_of_words']):
        word = random.choice(dB['words'])
        if len(message) == 0 or word != message[i - 1]:
            message.append(word)
    return " ".join(message)


def speak(sendmsg, message):
    if config['enable_speak_check']:
        if cache['speak_check_complete']:
            sendmsg(message['replyto'], "%s: %s" % (message['nick'], cache['line_pending']))
            cache['speak_check_complete'] = False  # After it's done, reset it.
            json.dump(cache, open("cache.json", 'w'), indent=2)
        else:
            speak_check(sendmsg, message)
    else:
        sendmsg(message['replyto'], "%s: %s" % (message['nick'], get_phrase()))


def speak_check(sendmsg, message):  # speak check is experimental, disabled by default.
    cache['line_pending'] = get_phrase()
    json.dump(cache, open("cache.json", 'w'), indent=2)
    if any(x in cache['line_pending'] for x in dB['words2']):
        speak_check(sendmsg, message)  # Restart this process.
    else:
        if any(x in cache['line_pending'].split()[-1] for x in dB['words3']):
            speak_check(sendmsg, message)  # Restart this process.
        else:
            cache['speak_check_complete'] = True
            json.dump(cache, open("cache.json", 'w'), indent=2)
            speak(sendmsg, message)


def words_autoshuffle():
    while True:
        time.sleep(config['autoshuffle_words'])
        words = random.shuffle(dB['words'])
        words = dB['words']
        json.dump(dB, open("dB.json", 'w'), indent=2)
