import config
import urllib2
import json
import time
import thread
from time import sleep



def mess(sock, message):
    sock.send("PRIVMSG #{} :{}\r\n".format(config.CHAN, message))



def ban(sock, user):
    mess(sock, ".ban {}".format(user))



def timeout(sock, user, seconds = 500):
    mess(sock, ".timeout {}".format(user, seconds))



#req = request
#res = response
def fillOpList():
    while True:
        try:
            url = "http://tmi.twitch.tv/group/user/winderton/chatters"
            req = urllib2.Request(url, headers={"accept": "*/*"})
            res = urllib2.urlopen(req).read()
            if res.find("502 bad gateway") == - 1:
                config.oplist.clear()
                data = json.loads(res)
                for p in data["chatters"]["moderators"]:
                    config.oplist[p] = "mod"
                for p in data["chatters"]["global_mods"]:
                    config.oplist[p] = "global_mod"
                for p in data["chatters"]["admins"]:
                    config.oplist[p] = "admin"
                for p in data["chatters"]["staff"]:
                    config.oplist[p] = "staff"
        except:
            "Something went wrong...do nothing"
        sleep(5)



def isOp(user):
    return user in config.oplist

