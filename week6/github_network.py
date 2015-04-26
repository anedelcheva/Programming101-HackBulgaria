import requests
import json
from directedGraph import DirectedGraph


class GithubNetwork:

    def __init__(self, url):
        user_request = requests.get(url)
        self.me = user_request.json()['login']
        r = requests.get(url+'/following')
        self.following = r.json()
        followers_request = requests.get(url+'/followers')
        self.followers = followers_request.json()
        self.network = DirectedGraph()

    def put_connections_to_network(self):
        for following in self.following:
            self.network.add_edge(self.me, following['login'])
        for follower in self.followers:
            self.network.add_edge(follower['login'], self.me)
        return self.network.graph

    def adding_following_of_my_following(self):
        https = 'https://api.github.com/users/'
        for following in self.following:
            following_request = requests.get(https+following['login']+'/following')
            user_following = following_request.json()
            for person in user_following:
                self.network.add_edge(following['login'], person['login'])
        return self.network.graph

    def adding_followers_of_my_followers(self):
        https = 'https://api.github.com/users/'
        for follower in self.followers:
            follower_request = requests.get(https+follower['login']+'/followers')
            user_followers = follower_request.json()
            for person in user_followers:
                self.network.add_edge(person['login'], follower['login'])
        return self.network.graph

    def do_you_follow_indirectly(self, user):
        for my_following in self.network.graph[self.me]:
            for user_following in self.network.graph[my_following]:
                if user in user_following:
                    return True
        return False

    def does_he_she_follows_indirectly(self, user):
        for current_user in self.network.graph:
            if self.me in self.network.graph[current_user]:
                    if current_user in self.network.graph[user]:
                        return True
        return False

    def get_following_list(self):
        user_following = []
        for following in self.following:
            user_following.append(following['login'])
        return user_following

    def do_you_follow(self, user):
        return user in self.network.graph[self.me]

    def does_he_she_follows(self, user):
        return self.me in self.network.graph[user]

aneta = GithubNetwork('https://api.github.com/users/anedelcheva')
'''aneta.put_connections_to_network()
aneta.adding_followers_of_my_followers()
aneta.adding_following_of_my_following()'''
print (json.dumps(aneta.network.graph, sort_keys=True, indent=4))

#print (aneta.me, aneta.followers, aneta.network.graph)
#print (json.dumps(aneta.user, sort_keys=True, indent=4))
#print (aneta.do_you_follow('tborisova'))

'''    def do_you_follow(self, user):
        return user in self.get_following_list()'''
