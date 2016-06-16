from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pafy


print " Youtube Song Downloader "
song=raw_input("Enter the name of the song \n")
url="https://www.youtube.com/results?search_query="+song
req=requests.get(url)
data=req.text
soup=BeautifulSoup(data, "html.parser")

song_list=[]

for link in soup.find_all('a'):
#    print(link.get('href'))
    song_list.append(link.get('href'))
    
#print song_list

for link in song_list:
    if link.find("watch") != -1:
        song_link=link
	break

#print song_link

final_link="http://www.youtube.com"+song_link

#driver=webdriver.Firefox()
#driver.get(final_link)

video=pafy.new(final_link)

#print video.title
#print video.description
#print video.rating

#info=video.allstreams
#for s in info:
#    print s.quality

stream=video.streams

for s in stream:
    print s.resolution, s.extension, (s.get_filesize()/(1024*1024))+1,"Mb"


stream_size=len(stream)
index=input("Enter index of video ")

if index <= stream_size:
    download_link=stream[index-1].url
    print download_link
else:
    print " Incorrect value! "



#best=video.getbest()

#print best.resolution
#print best.extension


#best.download(quiet=False)

#best.download()





