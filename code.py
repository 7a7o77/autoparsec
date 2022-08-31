from time import sleep
import requests
import json
import os
try:
    users = []
    attempts = 0
    data = {"authorization":"auth code"}
    url = "https://kessel-api.parsec.app/v2/hosts?mode=game&public=true"
    count = 0
    peer = 0
    def connect(peer):
        print("[system]peer:"+peer+"\n[system]user:"+i["user"]["name"]+"\n[system]lobbyname:"+i["name"])
        sleep(1)
        os.system('C:/"Program Files"/Parsec/parsecd.exe peer_id='+peer)
        print("quiting in 5 seconds")
        input("[try again ?]\n[doesnt join the lobbies you already joined]\nenter?")
        print("looking for open lobbies...")
    def filter(i,solo,gamename):
        if solo.lower() == "y" or solo.lower() == "yes" :
            if gamename.lower().replace(" ","") in i["name"].lower().replace(" ","") and i["players"] == 0 and not i["user"]["id"] in users:
                peer = i["peer_id"]
                users.append(i["user"]["id"])
                connect(peer)
        else:
            if gamename.lower().replace(" ","") in i["name"].lower().replace(" ","") and i["players"] < i["max_players"] and not i["user"]["id"] in users:
                print("found")
                peer = i["peer_id"]
                users.append(i["user"]["id"])
                connect(peer)
    gamename = input("enter the game name\ngame:")
    solo = input("do you want to play game with the host alone?\ny/n:")
    print("looking for open lobbies...")
    while True:
        try:
            r = requests.session()
            r.headers.update(data)
            t = r.get(url)
            list = json.loads(t.text)
            for i in list["data"]:
                filter(i,solo,gamename)
                
        except KeyError:
            print("wrong auth code")
            sleep(3)
            quit()
except KeyboardInterrupt:
    print("quiting in 3 seconds")
    sleep(3)
    quit()
