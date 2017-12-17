import pandas as pd

from bs4 import BeautifulSoup

import requests

import re

import unicodedata



attributes=['Crossing','Finishing','Heading accuracy',

 'Short passing','Volleys','Dribbling','Curve',

 'Free kick accuracy','Long passing','Ball control','Acceleration',

 'Sprint speed','Agility','Reactions','Balance',

 'Shot power','Jumping','Stamina','Strength',

 'Long shots','Aggression','Interceptions','Positioning',

 'Vision','Penalties','Composure','Marking',

 'Standing tackle','Sliding tackle','GK diving',

 'GK handling','GK kicking','GK positioning','GK reflexes']





links=[]   #get all argentinian players

for offset in ['0' , '80', '160', '240', '320', '400']:

    # every web page can list 80 players, and the "offset=" indicate who is the first palyer in the webpage
    # and "?na=" country code, 14 is England
    page=requests.get('http://sofifa.com/players?na=14&offset='+offset)
    # Use html parser to parse this webpage
    soup=BeautifulSoup(page.content,'html.parser')

    # in html Hyperlink is in "<a" fragment, which looks like
    # "<a href="/player/194957" title="Phil Jones">P. Jones</a>"
    # and we can get it's link in attr "href"
    # so use the following command, we can get all hyperlink in current webpage
    for link in soup.find_all('a'):

        links.append(link.get('href'))

# the hyperlinks which contain "player/" point to palyer's ability information page,
# and that's what we need, filter other useless link.
links=['http://sofifa.com'+l for l in links if 'player/'in l]

#pattern regular expression

pattern=r"""\s*([\w\s\-\.\']*?)\s*FIFA"""   #file starts with empty spaces... players name...FIFA...other stuff
# ([\w\s\-\.\']*?) : match player's name, it's the first group, the name may contain "word space - . ' ", and we use Non-greedy strategy
# \s*FIFA"" : the fist match group above is followed by some space and FIFA
for attr in attributes:

    pattern+=r""".*?(\d*\s*"""+attr+r""")"""  #for each attribute we have other stuff..number..attribute..other stuff
    # .*? : Non-greedy strategy to find other stuff
    # (\d*\s*"""+attr+r""") the second/third/..... match group, which begin with number, and then is space, and then is attr like Crossing, Finishing
pat=re.compile(pattern, re.DOTALL)    #parsing multiline text



rows=[]
# delete the first 10 players
links=links[10:]

for j,link in enumerate(links):

    # j is player's index, start from 0, and link is player's ability information page
    print(j,link)

    row=[link]

    playerpage=requests.get(link)

    playersoup=BeautifulSoup(playerpage.content,'html.parser')

    text=playersoup.get_text()
    # Normalize webpage content
    # NFKD : Normalization Form Compatibility Decomposition (from https://en.wikipedia.org/wiki/Unicode_equivalence)
    text=unicodedata.normalize('NFKD', text).encode('ascii','ignore')
    # decode it to text UTF-8
    text=text.decode("utf-8")

    a=pat.match(text)
    # group 1 is palyer's name
    row.append(a.group(1))
    # player's ability's attributes start from group 2
    for i in range(2,len(attributes)+2):

        row.append(int(a.group(i).split()[0]))

    rows.append(row)

    print(row[1])

df=pd.DataFrame(rows,columns=['link','name']+attributes)

df.to_csv('EnglandPlayers.csv',index=False)







