import requests
import json
from bs4 import BeautifulSoup
from histogram import Histogram


class ScanBgWeb:

    def __init__(self, url):
        self.url = url
        r = requests.get(url)
        self.html = BeautifulSoup(r.text)
        self.histogram = Histogram()

    def put_all_hrefs_to_list(self):
        hrefs_list = []
        for link in self.html.find_all('a'):
            hrefs_list.append(link.get('href'))
        return hrefs_list

    def filter_hrefs(self):
        hrefs_list = self.put_all_hrefs_to_list()
        link_php = 'link.php?id='
        hrefs_list_filtered = []
        for href in hrefs_list:
            if link_php in str(href):
                hrefs_list_filtered.append(href)
        return hrefs_list_filtered

    def get_servers(self):
        hrefs_list = self.filter_hrefs()
        bg_servers = []
        for href in hrefs_list:
            try:
                response = requests.get(self.url + '/' + href, timeout=3)
                bg_servers.append(response.headers['server'])
                #print (response.headers['server'])
            except:
                pass
        return bg_servers

    def servers_to_file(self):
        bg_servers = self.get_servers()
        with open('servers_bg.txt', 'w') as f:
            for server in bg_servers:
                #print (server)
                f.write(server + '/n')

web = ScanBgWeb('http://register.start.bg')
r = requests.get(web.url).headers['server']
print (r)
#print (web.get_servers())
web.servers_to_file()
