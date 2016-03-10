# -*- coding: utf-8 -*-
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

import json
import random
import time
from multiprocessing import Process

with open('cache.json') as f:
    cache = json.load(f)
with open('dB.json') as f:
    dB = json.load(f)
with open('config.json') as f:
    config = json.load(f)


def get_phrase():
    cache['number_of_words'] = random.randint(1, 12)
    cache['use_profanity'] = random.choice([True, False])
    with open('cache.json', 'w') as f:
        json.dump(cache, f, indent=2)
    if cache['use_profanity']:
        cache['number_of_profanity_words'] = random.randint(1, 4)
    else:
        cache['number_of_profanity_words'] = 0
    with open('cache.json', 'w') as f:
        json.dump(cache, f, indent=2)
    message = []
    for i in range(cache['number_of_words']):
        words = random.choice(dB['words'])
        try:
            if len(message) == 0 or words != message[i - 1]:
                message.append(words)
        except Exception:
            pass
    profanity_message = []
    if cache['number_of_profanity_words'] != 0:
        for i in range(cache['number_of_profanity_words']):
            profanity_words = random.choice(dB['words'])
            try:
                if len(profanity_message) == 0 or profanity_words != profanity_message[i - 1]:
                    profanity_message.append(profanity_words)
            except Exception:
                pass
    else:
        pass

    message.extend(profanity_message)
    random.shuffle(message)
    return " ".join(message)


def speak(sendmsg, message):
    if cache['speak_check_complete']:
        sendmsg(message['replyto'], "%s: %s" % (message['nick'], cache['line_pending']))
        cache['speak_check_complete'] = False  # After it's done, reset it.
        cache['line_pending'] = ""
        cache['number_of_words'] = 0
        with open('cache.json', 'w') as f:
            json.dump(cache, f, indent=2)
    else:
        speak_check(sendmsg, message)


def speak_check(sendmsg, message):
    cache['line_pending'] = get_phrase()
    with open('cache.json', 'w') as f:
        json.dump(cache, f, indent=2)
    if cache['number_of_words'] == 1:
        if any(x in cache['line_pending'] for x in dB['words3']):
            speak_check(sendmsg, message) # Restart this process.
        else:
            cache['speak_check_complete'] = True
            with open('cache.json', 'w') as f:
                json.dump(cache, f, indent=2)
            speak(sendmsg, message)
    else:
        if any(x in cache['line_pending'] for x in dB['words2']):
            speak_check(sendmsg, message) # Restart this process.
        elif any(x in cache['line_pending'].split()[-1] for x in dB['words3']):
            speak_check(sendmsg, message) # Restart this process.
        else:
            cache['speak_check_complete'] = True
            with open('cache.json', 'w') as f:
                json.dump(cache, f, indent=2)
            speak(sendmsg, message)


def words_autoshuffle():
    while True:
        time.sleep(config['autoshuffle_words'])
        random.shuffle(dB['words'])
        random.shuffle(dB['words4'])
        with open('dB.json', 'w') as f:
            json.dump(dB, f, indent=2)
