from bs4 import BeautifulSoup
import numpy as np
import requests
import cv2
import urllib
import os

def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()),dtype="uint8")
    image = cv2.imdecode(image,cv2.IMREAD_COLOR)
    return image

with open('images_url6.txt') as f:
    lines = f.readlines()


for line in lines:
    name = line.strip().split(" ")[0]
    split_urls = line.strip().split(" ")[1]
    if not split_urls == None:
        if os.path.exists('../darkflow-master/train/annotations/{}.xml'.format(name)):
            try:
                # print(split_urls)
                I = url_to_image(split_urls)          
                if (len(I.shape)) == 3:                   
                    save_path='../darkflow-master/train/images/{}.jpg'.format(name)
                    cv2.imwrite(save_path,I)
                    print("Downloading image {}.jpg".format(name))
            except:
                print("skip {}".format(name)) 

print("###################################")
print("Done download images")

for line in lines:
    name = line.split(" ")[0]
    if not os.path.exists('../darkflow-master/train/images/{}.jpg'.format(name)) and \
        os.path.exists('../darkflow-master/train/annotations/{}.xml'.format(name)):
       os.remove('../darkflow-master/train/annotations/{}.xml'.format(name))
       print('delete {}.xml'.format(name)) 

f.close()




