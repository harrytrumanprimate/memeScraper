from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import urllib
import requests
from urllib.request import urlretrieve
import time

url = 'https://www.reddit.com/r/'

subReddits = ['memes']

def searchMemes(subReddits):
    for subReddit in subReddits:

        # pause scrape to not get banned
        time.sleep(30)
        page = requests.get('https://www.reddit.com/r/' + subReddit)
        soup = bs(page.content, 'html.parser')
        #print (page)
        #print (soup) 


        #### find all memes associated with this page 
        potential_memes = soup.findAll('img',attrs={'class':'_2_tDEnGMLxpM6uOa2kaDB3 media-element'})

        list_of_memes=[]

        for meme in potential_memes:
            src=meme['src']
            #print (meme)
            list_of_memes.append(src)
            #print (list_of_img)
            

        i=1 # i loop through all memes within potential_memes and subreddits
        for meme in list_of_memes:
            memeName='reddit'+str(i)
            urlretrieve(list_of_memes[i-1], 'meme_Scraper/memes_storage/memes_Staging' + memeName + '.jpg')
            i+=1