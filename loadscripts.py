from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import re

def create_episodes(data):

    fp = open("episodes/all_episodes.txt","w")
    fp.writelines(data)
    fp.close()

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

url='https://fangj.github.io/friends/'
req = Request(url)
page = urlopen(req)
soup = BeautifulSoup(page, 'html.parser')
items = soup.find_all('a', href=True)
season_dicts = {"s1":["0101","0124"],
                "s2":["0201","0224"],
                "s3":["0301","0325"],
                "s4":["0401","0423"],
                "s5":["0501","0523"],
                "s6":["0601","0624"],
                "s7":["0701","0724"],
                "s8":["0801","0823"],
                "s9":["0901","0924"],
                "s10":["1017","1018"]}
break_point = "401"
episode_data = []
for i in items:
    episode_no = i["href"].split("/")[-1].replace("html","txt")
    req = Request(url+i["href"])
    episodes = urlopen(req)
    soup = BeautifulSoup(episodes, 'html.parser')
    text_elements = soup.find_all('p')
    
    for j in text_elements:
        if len(striphtml(str(j)).replace("\n",""))>3:
            episode_data.append(striphtml(str(j)).replace("\n","")+"\n")

create_episodes(episode_data)
