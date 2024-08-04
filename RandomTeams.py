from random import choice
asami = ['hosein', 'maziar', 'akbar', 'nima', 'mehdi', 'farhad', 'mamad', 'khashayar', 'milad', 'mostafa', 'amin', 'saeed', 'pooya', 'poorya', 'reza', 'ali', 'behzad', 'soheil', 'behruz', 'shahruz', 'saman', 'mohsen']

class Person:
    def __init__(self, name):
        self.name = name


class Footbalist(Person):
    def get_team(self):
        self.teamA = []
        for i in range(len(asami) // 2):
            self.teamA.append(choice(self.name))
            self.name.remove(self.teamA[i])
        self.teamB = self.name
        return self.teamA, self.teamB


a = Footbalist(asami)
A, B = a.get_team()
print('teamA = %s \nteamB = %s' % (A, B))
