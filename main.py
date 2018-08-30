#rashan hasaranga
import os
import shutil
import urllib.request

#variable defines
pics_directory = "pics"
albums_for_once = 1

#get last album
last_album_file = [f for f in os.listdir('.') if f.endswith('.cura')]
last_albumz = [item.replace(".cura", "") for item in last_album_file]
last_album = last_albumz[0]

#send http requests to download images
def album_scrape(id):
    #try:
        path = pics_directory + "/" + str(id)
        if not os.path.exists(path):
        os.mkdir(path)
        urllib.request.urlretrieve("https://y2.pichunter.com/" + str(id) + "_1_o.jpg", pics_directory + "/" + str(id) + "/" + str(id) + "_1_o.jpg")
        complete_album(id)
    #except:
        #path = pics_directory + "/" + str(id)
        #if os.path.exists(path) and os.path.isdir(path):
            #shutil.rmtree(path)
        #print("This is an error message! - " + str(id))

#download whole album
def complete_album(id):
    for item in range(2, 31):
        #try:
            urllib.request.urlretrieve("https://y2.pichunter.com/" + str(id) + "_" + str(item) + "_o.jpg", pics_directory + "/" + str(id) + "/" + str(id) + "_" + str(item) + "_o.jpg")
            #return
        #except:
            #return

#loop albums
for x in range(albums_for_once):
  album_scrape(x+int(last_album))
else:
  print("Finally finished!")
