from time import sleep
import requests
import json
import webbrowser
import os
try:
    attempts = 0
    data = {"authorization":"AUTHCODE"} #enter your auth code here
    count = 0
    peer = 0
    gamename = input("enter the game name\ngame:")
    solo = input("do you want to play game with the host alone?\ny/n:")
    print("looking for open lobbies...")
    while True:
        try:
            r = requests.session()
            r.headers.update(data)
            t = r.get(url)
            list = json.loads(t.text)
            if solo.lower() == "y" or solo.lower() == "yes":
                for i in list["data"]:
                    if gamename.lower() in i["name"].lower() and i["players"] == 0:
                        peer = i["peer_id"]
                        print("[system]peer:"+peer+"\n[system]user:"+i["user"]["name"]+"\n[system]lobbyname:"+i["name"])
                        sleep(1)
                        os.system('C:/"Program Files"/Parsec/parsecd.exe peer_id='+peer)
                        print("quiting in 5 seconds")
                        sleep(5)
                        quit()
            else:
                for i in list["data"]:
                    if gamename.lower() in i["name"].lower() and i["players"] < i["max_players"]:
                        peer = i["peer_id"]
                        print("[system]peer:"+peer+"\n[system]user:"+i["user"]["name"]+"\n[system]lobby_name:"+i["name"])
                        sleep(1)
                        os.system('C:/"Program Files"/Parsec/parsecd.exe peer_id='+peer)
                        print("quiting in 5 seconds")
                        sleep(5)
                        quit()
            print(f"no lobbies refreshing...\nattempts:{attempts}")
            attempts = attempts + 1
            

        except KeyError:
            print("wrong auth code")
            sleep(3)
            quit()
except KeyboardInterrupt:
    print("quiting in 3 seconds")
    sleep(3)
    quit()
