import logging
import sys
import ssl
import socket
import os
from platform import python_version
import time
import datetime
import base64
import logging
import random

#--------------------------------------------------------------#

botnick = "mlgprom8quickscopeyoul8er"
server = "chat.freenode.net"
port = 6697
main_channel = [""] # Useful for working on the bot without flooding other channels with join/quit messages.
channels = [""] # You can leave this empty if you want to only use main_channel.
channels_different_command_trigger = [""] # You can leave this empty if you want.
join_on_invite = True # The annoying brat will join on-invite if set to True.
ssl_enabled = True # Not recommended to set this to false. 
sasl_login = False
Enforce_SASL = False # Disconnects & kills the bot if SASL fails if set to True.
nickserv_login = False
server_require_pass = False # Set this to true if the server requires a password.
account_username = '' # Used for NickServ/SASL login.
account_password = '' # Used for NickServ/SASL login.
server_password = ''
char1 = ''
char2 = ''
main_channel_only_mode = True # Will only join the main channel if True
logging_level = logging.DEBUG # Sets the logging level (valid options are DEBUG, INFO, WARNING, ERROR and CRITICAL)

#---------------------------------------------------------------#

Kid_IQ = "-1" # Such useless variable, but why not? :P

logging.getLogger(None).setLevel(logging_level)
logging.basicConfig()

class TokenBucket(object):
    """An implementation of the token bucket algorithm.

    >>> bucket = TokenBucket(80, 0.5)
    >>> bucket.consume(1)
    """
    def __init__(self, tokens, fill_rate):
        """tokens is the total tokens in the bucket. fill_rate is the
        rate in tokens/second that the bucket will be refilled."""
        self.capacity = float(tokens)
        self._tokens = float(tokens)
        self.fill_rate = float(fill_rate)
        self.timestamp = time.time()

    def consume(self, tokens):
        """Consume tokens from the bucket. Returns True if there were
        sufficient tokens otherwise False."""
        if tokens <= self.tokens:
            self._tokens -= tokens
            return True
        return False

    @property
    def tokens(self):
        now = time.time()
        if self._tokens < self.capacity:
            delta = self.fill_rate * (now - self.timestamp)
            self._tokens = min(self.capacity, self._tokens + delta)
        self.timestamp = now
        return self._tokens


tokenbucket = TokenBucket(4, 0.5)

def sendraw(msg):
    while not tokenbucket.consume(1):
        time.sleep(0.1)

    ircsock.sendall(bytes(msg, "utf-8"))

def acs_normal(message):
  return True

def ping(arg):
    sendraw("PONG : %s \n" % (arg))

def joinchan(chan):
    sendraw("JOIN %s \n" % (chan))

def random():
    bullshit = ['Fgt', 'u wot m8', '1v1 me quickscope n0scope bitch', 'penis', 'b00bs', 'minecraft is gud', 'fk you', 'm8', "I'm MLG pro lol", 'OOOH OHOHHH QUICKSCOPE MOTHERFUCKER OOOOH', 'ur gay']
    print("success")
    sendmsg(message['replyto'], '%s' % (random.choice(foo)))

def sendmsg(chan, msg):
    logging.debug("sendmsg to %s (' %s ')" % (chan, msg))
    sendraw("PRIVMSG %s :%s \n" % (chan, msg))

def join_channel():
    if main_channel_only_mode == False:
        logging.info("Joining the channels...")
        joinchan(','.join(main_channel))
        joinchan(','.join(channels))
    elif main_channel_only_mode == True:
        logging.info("Main channel only mode is enabled, Only joining the main channel(s)")
        joinchan(','.join(main_channel))
    else:
        logging.error("Invalid option for the Main channel only mode, Shutting down...")
        sys.exit()

def parse_ircmsg(rawmsg):
    tmp     = rawmsg.split(' :', 1)
    message = tmp[0].split(' ')

    if len(tmp) > 1:
        message.append(tmp[1])

    nick = None
    user = None
    host = None

    prefix = None
    if message[0][0] == ':':
        prefix = message.pop(0)
        tmp = prefix.split('!', 1)
        if len(tmp) > 1:
            nick = tmp[0][1:]
            tmp  = tmp[1].split('@', 1)
            user = tmp[0]
            if len(tmp) > 1:
                host = tmp[1]

    parsed = dict(nick = nick, user = user, host = host, prefix = prefix,
            command = message[0], args = message[1:])

    # convenience for PRIVMSGs
    parsed['replyto'] = parsed['args'][0]
    if len(parsed['replyto']) < 2:
     pass
    else:
     if parsed['replyto'][0] != '#':
        parsed['replyto'] = parsed['nick']

    return parsed

if ssl_enabled == True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
else:
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if ssl_enabled == True:
    s.connect((server, port))
    ircsock = ssl.wrap_socket(s)
else:
    ircsock.connect((server, port))
if sasl_login == True:
    sendraw("CAP REQ :sasl\r\n")
    sendraw("AUTHENTICATE PLAIN\r\n")
    datastr= "%s\0%s\0%s" % (account_username, account_username, account_password)
    sendraw("AUTHENTICATE " + base64.b64encode(datastr.encode()).decode() + "\r\n")
    sendraw("CAP END\r\n")
else:
    pass
sendraw("USER %s %s %s :uw0tm8? %s\n" % (botnick, botnick, botnick, bot_version))
if server_require_pass == True:
    sendraw("PASS %s \n" % (server_password))
else:
    pass

sendraw("NICK %s \n" % (botnick))

if nickserv_login == True:
    time.sleep(1.5)
    sendraw("PRIVMSG NickServ :IDENTIFY %s %s\r\n" % (account_username, account_password))
else:
    pass

lines = []
while 1:
    ircmsg = ''
    if len(lines) <= 1:
        rawmsg = ''
        if len(lines) == 1:
            rawmsg = lines.pop()
        rawmsg += ircsock.recv(2048).decode("utf-8")
        lines += rawmsg.split('\r\n')

    if len(lines) > 1:
        ircmsg = lines.pop(0)
    else:
        continue

    if logging_level == logging.DEBUG:
        logging.debug("RECV: " + ircmsg)
    else:
        pass

    message = parse_ircmsg(ircmsg)

    if message['command'] == 'PING':
        ping(' '.join(message['args']))

    elif message['command'] == '904':
        ID = False

    elif message['command'] == '903':
        ID = True

    elif message['command'] == '437' or message['command'] == '433':
        logging.error("Botnick %s is unavailable." % (botnick))
        sys.exit()

    elif message['command'] == '376':
        if sasl_login == True:
            if ID == True:
                logging.info("Successfuly been identified through SASL")
                join_channel()
            else:
                logging.warning("Failed to login through SASL")
            if Enforce_SASL == True:
                logging.error("Disconnecting: SASL has failed")
                sys.exit()
            else:
                join_channel()
       else:
           join_channel()

    elif message['command'] == "INVITE":
        if join_on_invite == True:
            cmd_args = message['args'][-1].split(' ')
            logging.info(message['replyto']+" invited me into "+cmd_args[0])
            joinchan(cmd_args[0])
        else:
            pass
    elif message['command'] == 'ERROR':
        sys.exit(0)

    elif message['command'] == 'PRIVMSG':
        command = None
        access  = acs_normal

        cmd_args = message['args'][-1].split(' ')

        ########
        # if there's no command, there's nothing to do in this processing loop
        if len(cmd_args) == 0:
            continue

        # first decide what command char is effective for the channel
        wanted_char = char1
        if message['replyto'] in channels_different_command_trigger:
            wanted_char = char2

        # separate the char from command
        used_char = cmd_args[0][0:len(wanted_char)]
        command_word = cmd_args[0][len(wanted_char):]
        # and then check the message starts with the effective command char
        if used_char != wanted_char:
            continue

        # should be possible to simplify the rest again like such
        if '' == command_word:
            random()

        # run the command if they're allowed to
        if not command is None:
            if access(message):
                command(message, cmd_args[1:])
            else:
                sendmsg(message['replyto'], message['nick'] +": Permission Denied")
