class Histogram:

    def __init__(self):
        self.web_servers = {'Apache': 0, 'nginx': 0, 'IIS': 0}

    def add(self, web_server):
        if web_server not in self.web_servers:
            return
        self.web_servers[web_server] += 1

    def count(self, web_server):
        if web_server not in self.web_servers:
            return None
        return self.web_servers[web_server]

    def statistics_servers(self):
        for key, count in self.web_servers.items():
            print ('{}: {}'.format(key, count))

    def get_dict(self):
        return self.web_servers

'''h = Histogram()
h.add('Apache')
h.add('Apache')
h.add('nginx')
h.add('nginx')
h.add('IIS')
h.add('Other')
print (h.count('Apache'))
print (h.count('nginx'))
print (h.count('IIS'))
print (h.get_dict())
h.statistics_servers()
print (h.get_dict())'''
