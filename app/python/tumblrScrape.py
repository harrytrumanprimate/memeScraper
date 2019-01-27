##### API Key incase I ever need it
#tumblrSecretKey = 'H9K3gCRYdUGXBPC5Y6kE4D7E13BoqdUfyhGuQMUsqhwJejLeOt'
#tumblrConsumerKey = 'fPoHnTfkl4WILvsViZUX6CbsGOjLiQrXZL0E4AwvsWMWqsccKv'
#####
import urllib3
from bs4 import BeautifulSoup
import requests
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#### help() module to get documentation 

url = 'https://www.tumblr.com/search/'


searchTerms = ['meme']
def search(searchTerms,url): 
    for searchTerm in searchTerms:
        #scale whatever i'm doing to be compatible with more than one search term on tumblr
        # concatenate searchterm with url search to pass commands 
        search = url + searchTerm
        browser = webdriver.Chrome(executable_path='C:\\Users\\Chase\\Documents\\memeScraper\\app\\assets\\webDrivers\\chromedriver.exe')
        browser.implicitly_wait(30)

        # wait 1 second so we don't get banned xd 
        #time.sleep(1)
     
        #get request 
        #page = requests.get(search)
        page = browser.get(search)
        #print(page)

        ######## soup is a function that parses html content from the GET request! xd 
        soup = BeautifulSoup(page.content,'html.parser')
        #print(soup)

        ### find memes!!!!
        class1 = "flag--reblog-ui-refresh flag--messaging-new-empty-inbox flag--npf-text-web-styles flag--npf-text-colors flag--always-opaque-peepr search_results search_blogs has-discover-controls search search_results search_results_flex search_results_mode_top identity base identity-refresh search_actions_search logged_out without_auto_paginate layout_standard"
        potential_memes = soup.findAll("class",class1)
        
        print(potential_memes)





search(searchTerms,url)

