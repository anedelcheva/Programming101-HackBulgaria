import requests
from bs4 import BeautifulSoup

class FindLinksFromAnHtmlOfAPage:

# the instructor receives a url which is a web page
    def __init__(self, url):
        r = requests.get(url)
        #r.text contains all the html document in a string format
        #in self.html we have the html file of the webpage. BeautifulSoup
        #converts the string r.text to an html document
        self.html = BeautifulSoup(r.text)

    def put_all_hrefs_to_list(self):
        hrefs_list = []
        #getting all hrefs from a valid html document
        for link in self.html.find_all('a'):
            hrefs_list.append(link.get('href'))
        return hrefs_list

        #filtering those hrefs which conform
        #with the pattern link.php?id=64722
    def filter_hrefs(self):
        hrefs_list = self.put_all_hrefs_to_list()
        link_php = 'link.php?id='
        hrefs_list_filtered = []
        for href in hrefs_list:
            if link_php in str(href):
                hrefs_list_filtered.append(href)
        return hrefs_list_filtered


'''r = requests.get('http://register.start.bg/#b_6118').text
print (r)'''

links = FindLinksFromAnHtmlOfAPage('http://register.start.bg/#b_6118')
print (links.filter_hrefs())

#print (r.headers['Server'])
#r2 = requests.get('https://gsm.bg')
