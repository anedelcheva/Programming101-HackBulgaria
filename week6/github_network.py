import requests
import json
from directedGraph import DirectedGraph


class GithubNetwork:

    def __init__(self, url):
        user_request = requests.get(url)
        self.me = user_request.json()['login']
        r = requests.get(url+'/following')
        self.user = r.json()
        self.network = DirectedGraph()

    def put_connections_to_network(self):
        for following in self.user:
            self.network.add_edge(self.me, following['login'])
        return self.network.graph

    def get_following_list(self):
        user_following = []
        for following in self.user:
            user_following.append(following['login'])
        return user_following

    def do_you_follow(self, user):
        return user in self.network.graph[self.me]

aneta = GithubNetwork('https://api.github.com/users/anedelcheva')
#print (json.dumps(aneta.user, sort_keys=True, indent=4))
#print (aneta.put_connections_to_network())
#print (aneta.do_you_follow('tborisova'))

'''    def do_you_follow(self, user):
        return user in self.get_following_list()'''
