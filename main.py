#  _____           _                 _    _
# |  __ \         | |               | |  | |
# | |__) |__ _ ___| |__   __ _ _ __ | |__| |
# |  _  // _` / __| '_ \ / _` | '_ \|  __  |
# | | \ \ (_| \__ \ | | | (_| | | | | |  | |_
# |_|  \_\__,_|___/_| |_|\__,_|_| |_|_|  |_(_)
# Coded by Rashan Hasaranga (2018)
# rashanh@github | rashan.original@fb | rashan.hasaranga@twitter

import os
import re
import json
import shutil
import urllib.request

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#validation
def inputNumber(message):
  while True:
    try:
       userInput = int(input(message))
    except ValueError:
       continue
    else:
       return userInput
       break


#show credits
print(" ______ _       _     _                              ")
print("(_____ (_)     (_)   (_)             _               ")
print(" _____) )  ____ _______ _   _ ____ _| |_ _____  ____ ")
print("|  ____/ |/ ___)  ___  | | | |  _ (_   _) ___ |/ ___)")
print("| |    | ( (___| |   | | |_| | | | || |_| ____| |    ")
print("|_|    |_|\____)_|   |_|____/|_| |_| \__)_____)_|    ")
print("  ______                                             ")
print(" / _____)                                            ")
print("( (____   ____  ____ _____ ____  _____               ")
print(" \____ \ / ___)/ ___|____ |  _ \| ___ |              ")
print(" _____) | (___| |   / ___ | |_| | ____|              ")
print("(______/ \____)_|   \_____|  __/|_____)              ")
print("                          |_|              ")

print("Coded by Rashan Hasaranga (2018)")
print("rashanh@github | rashan.original@fb | rashan.hasaranga@twitter")
print("")

#variable defines
pics_directory = "pics"
#albums_for_once = 10
albums_for_once = inputNumber("How many albums you need to download? (default : 200) : ") or "2"
print("")

#get last album
last_album_file = [f for f in os.listdir('.') if f.endswith('.cura')]
last_albumz = [item.replace(".cura", "") for item in last_album_file]
last_album = last_albumz[0]

#send http requests to download images
def album_scrape(id):
    path = pics_directory + "/" + str(id)
    os.rename(str(id) + '.cura', str(int(id)+1) + '.cura')
    try:
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print("Already downloaded album - " + str(id))
            return

        #json
        contents = urllib.request.urlopen("https://www.pichunter.com/gallery/" + str(id)).read()
        jsonobj = re.findall(r'metaData = (.*?);', str(contents))
        jsonitems = json.loads(jsonobj[0])
        models = (jsonitems['models']) or "NULL"
        tags = (jsonitems['tags']) or "NULL"
        site = (jsonitems['site']) or "NULL"
        titlez = re.findall(r'<h1>(.*?)</h1>', str(contents)) or "NULL"
        title = [w.replace('&mdash;', '-').replace('&amp;', '&').replace('&nbsp;', ' ').replace('\\', '') for w in titlez]

        data = {}
        data['album_data'] = []
        data['album_data'].append({
            'title': title,
            'pornstarts': models,
            'site': site,
            'tags': tags
            })
        with open(path + '/data.json', 'w') as outfile:
            json.dump(data, outfile)
        print(bcolors.OKGREEN + "Downloading(" + str(id) + ")"  + bcolors.ENDC +" -> " + str(models[0]) + " | " + str(title[0]))

        urllib.request.urlretrieve("https://y2.pichunter.com/" + str(id) + "_1_o.jpg", pics_directory + "/" + str(id) + "/" + str(id) + "_1_o.jpg")
        complete_album(id)
    except:
        if os.path.exists(path) and os.path.isdir(path):
            shutil.rmtree(path)
        #print("Album not found(" + str(id) + ")")
        return

#download whole album
def complete_album(id):
    for item in range(2, 31):
        try:
            urllib.request.urlretrieve("https://y2.pichunter.com/" + str(id) + "_" + str(item) + "_o.jpg", pics_directory + "/" + str(id) + "/" + str(id) + "_" + str(item) + "_o.jpg")
        except:
            print("Successfully downloaded(" + str(id) + ") -> " + str(int(item)-1)) + " photos"
            return

#loop albums
for x in range(albums_for_once):
    album_scrape(x+int(last_album))
else:
    print("")
    print("Finished downloading " + str(albums_for_once) + " albums. Thank you!")
