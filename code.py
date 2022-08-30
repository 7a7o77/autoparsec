#unused packges = failed attempts
from time import sleep
import requests
import json
import subprocess
import webbrowser
import socket
import clipboard
import js2py
import websockets
import asyncio
try:
    attempts = 0
    data = {"authorization":"AUTHCODE"} #enter your auth code here
    url = "https://kessel-api.parsec.app/v2/hosts?mode=game&public=true"
    count = 0
    
    
    
    peer = 0
    gamename = input("enter the game name\ngame:")#get game name
    solo = input("do you want to play game with the host alone?\ny/n:")#solo mode
    print("looking for open lobbies...")
    while True:
        try:
            r = requests.session() #start a session
            r.headers.update(data) #update the session
            t = r.get(url) #get a list of games
            list = json.loads(t.text) # turn into a dic
            if solo.lower() == "y" or solo.lower() == "yes":
                for i in list["data"]:
                    if gamename.lower() in i["name"].lower() and i["players"] == 0: #filter
                        peer = i["peer_id"]
                        print("[system]pear:"+peer+"\n[system]user:"+i["user"]["name"])
                        sleep(2)
                        webbrowser.open('''https://parsec.app/join-arcade/?peer='''+peer)
                        print("quiting in 5 seconds")
                        sleep(5)
                        quit()
            else:
                for i in list["data"]: #too lazy to make a function
                    if gamename.lower() in i["name"].lower() and i["players"] < i["max_players"]:
                        peer = i["peer_id"]
                        data2 = {'session_id': '_','role': 'client','version': '1','sdk_version': '0'}
                        print("[system]pear:"+peer+"\n[system]user:"+i["user"]["name"])
                        sleep(2)
                        webbrowser.open("https://parsec.gg/g/"+peer)
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

   
