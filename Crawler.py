import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urlparse
class Website():
    """This class parse a defined url and get frags of the url.
     """
    def __init__(self,url):
        #declare variables, this class must receive an url
        self.url=url
        self.domain= urlparse(url).netloc
        self.urlScheme =  urlparse(url).scheme #it will return http or https
        self.urlBase = str(self.urlScheme + '://'+ self.domain) #it will return a url like 'http://www.example.com'
    def __str__ (self):   
        return self.url,self.domain,self.urlScheme, self.urlBase
def scraping(urlsList):
    "This function receive a list of Google Url and return all the search results in that url"
    week= (time.strftime("%W"))
    found_results = []
    ID = 1
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        }
    for url in urlsList:
        try:
            r = requests.get(url,headers=headers)
            if(r.status_code == 200):
                data = r.text
                soup = BeautifulSoup(data, 'html.parser')
                queryValue= soup.find('input', attrs={'name':'q'}).get('value')
                result_block = soup.find_all('div', attrs={'class': 'g'})
                extraction_date = (time.strftime("%x"))
            elif result_block==None or len(result_block)==0:
                print("Not found results")
                return        
            else:
                print("Blocked by Google, please try again later")
        except Exception as err:
            print ("Error in request : "+ str(err))
        try:
            for result in result_block:
                link = result.find('a')['href']
                title = result.find('h3', attrs={'class': 'LC20lb'})
                description = result.find('span', attrs={'class': 'st'})
                ArticleDate=''
                website= Website(link)
                if 'num=100' in str(link) :
                    pass
                else:
                    if title != None:
                        title = title.text.strip()
                    else:
                        title="" 
                    if description != None:
                        description = description.text.strip()
                        date = description.split('-',2)
                        description= date[1]
                        ArticleDate= date[0]
                    if link != '#' and link != None:
                        found_results.append({'Title': title, 'Description': description,'url':link,'Source': website.domain,'Article_date':ArticleDate,'week': week,'Extraction Date':extraction_date,'Query':queryValue,'GoogleUrl':url})
                ID += 1
            time.sleep(5)
        except Exception as e:
            print("Error in scraping: "+ str(e))   
    return found_results
