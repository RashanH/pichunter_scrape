#rashan hasaranga
import os
import json
import re
import shutil
import urllib.request

#variable defines
pics_directory = "pics"
albums_for_once = 10

#get last album
last_album_file = [f for f in os.listdir('.') if f.endswith('.cura')]
last_albumz = [item.replace(".cura", "") for item in last_album_file]
last_album = last_albumz[0]

#send http requests to download images
def album_scrape(id):
        path = pics_directory + "/" + str(id)
    #try:
        if not os.path.exists(path):
            os.mkdir(path)
        else:
            print("Already downloaded album - " + str(id))
            return
        #urllib.request.urlretrieve("https://y2.pichunter.com/" + str(id) + "_1_o.jpg", pics_directory + "/" + str(id) + "/" + str(id) + "_1_o.jpg")
        #json
        contents = urllib.request.urlopen("https://www.pichunter.com/gallery/" + str(id)).read()
        jsonobj = re.findall(r'var metaData = (.*?);', str(contents))
        jsonitems = json.loads(jsonobj[0])
        models = (jsonitems['models']) or "none"
        tags = (jsonitems['tags']) or "none"
        site = (jsonitems['site']) or "none"
        title = re.findall(r'<h1>(.*?)</h1>', str(contents)) or "none"

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

        print("Downloaded " + str(id) + " - 1")
        print(title)
        print(jsonitems['models'])
        print(jsonitems['site'])
        print(jsonitems['tags'])
        #complete_album(id)
        return
    #except:
        #if os.path.exists(path) and os.path.isdir(path):
            #shutil.rmtree(path)
        #print("This is an error message! - " + str(id))

#download whole album
def complete_album(id):
    for item in range(2, 31):
        try:
            urllib.request.urlretrieve("https://y2.pichunter.com/" + str(id) + "_" + str(item) + "_o.jpg", pics_directory + "/" + str(id) + "/" + str(id) + "_" + str(item) + "_o.jpg")
            print("Downloaded " + str(id) + " - " + str(item))
        except:
            print("Album done! - " + str(id))
            return

#loop albums
for x in range(albums_for_once):
  album_scrape(x+int(last_album))
else:
  print("Finally finished!")
