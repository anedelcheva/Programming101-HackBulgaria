from panda import Panda


class PandaAlreadyThere(Exception):
    pass


class PandasAlreadyFriends(Exception):
    pass


class PandaSocialNetwork:

    def __init__(self):
        self.network = {}

    def __str__(self):
        return str(self.network)

    def add(self, panda):
        if panda in self.network:
            raise PandaAlreadyThere

        self.network[panda] = []

    def has_panda(self, panda):
        return panda in self.network

    def make_friends(self, panda1, panda2):
        if panda1 not in self.network:
            self.add(panda1)
        if panda2 not in self.network:
            self.add(panda2)
        if panda1 in self.network[panda2]:
            raise PandasAlreadyFriends
        self.network[panda2].append(panda1)
        if panda2 in self.network[panda1]:
            raise PandasAlreadyFriends
        self.network[panda1].append(panda2)

    def are_friends(self, panda1, panda2):
        if panda1 not in self.network or panda2 not in self.network:
            return False
        return panda1 in self.network[panda2] and panda2 in self.network[panda1]

    def friends_of(self, panda):
        if panda not in self.network:
            return False
        return self.network[panda]

    def connection_level(self, panda1, panda2):
        if not self.has_panda(panda1) or not self.has_panda(panda2):
            return False
        if self.are_friends(panda1, panda2):
            return 1
        queue = []
        visited = set()
        path = {}
        path_length = 0
        found = False

        queue.append(panda1)
        visited.add(panda1)
        path[panda1] = None

        while len(queue) != 0:
            current_node = queue.pop(0)
            if current_node == panda2:
                found = True
                break
            for neighbour in self.network[current_node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
                    path[neighbour] = current_node

        if found:
            current_panda = panda2
            while path[current_panda] is not None:
                current_panda = path[current_panda]
                path_length += 1
        else:
            return -1

        return path_length

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != -1 \
            and self.connection_level(panda1, panda2) != False

    def how_many_gender_in_network(self, level, panda, gender):
        counter = 0
        for every_panda in self.network:
            current_level = self.connection_level(panda, every_panda)
            if current_level <= level and current_level != -1 \
                    and every_panda.get_gender() == gender \
                    and every_panda != panda:
                counter += 1
        return counter
