import requests
from bs4 import BeautifulSoup
from histogram import Histogram
import matplotlib.pyplot as plt


class ScanBgWeb:

    my_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

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
                response = requests.head(self.url + '/' + href, allow_redirects=True, timeout=3, headers=my_headers)
                bg_servers.append(response.headers['server'])
                print (response.headers['server'])
            except:
                pass
        return bg_servers

    def servers_to_file(self):
        bg_servers = self.get_servers()
        with open('servers_bg.txt', 'w') as f:
            for server in bg_servers:
                f.write(server + '\n')

    def get_statistics(self):
        with open('servers.txt', 'r') as f:
            servers = f.read()
            server_list = servers.split('\n')
            for server in server_list:
                if 'Apache' in server:
                    self.histogram.add('Apache')
                elif 'nginx' in server:
                    self.histogram.add('nginx')
                elif 'IIS' in server:
                    self.histogram.add('IIS')
                elif 'lighttpd' in server:
                    self.histogram.add('lighttpd')

web = ScanBgWeb('http://register.start.bg')
r = requests.head(web.url).headers['server']
#print (r)
#print (web.get_servers())
#web.servers_to_file()
web.get_statistics()
h = web.histogram.get_dict()
keys = list(h.keys())
values = list(h.values())
print (keys)
print (values)
X = list(range(len(keys)))
print (X)
plt.bar(X, list(h.values()), align="center")
plt.xticks(X, keys)

plt.title(".bg servers")
plt.xlabel("Server")
plt.ylabel("Count")

plt.savefig("histogram2.png")
