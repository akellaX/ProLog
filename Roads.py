import numpy as np;
class Roads :
    dict = {}
    def __init__(self):
        print("created")

    def add_road (self, key, value) :
        if not (key in self.dict) :
                self.dict[key] = {value}
        else :
                self.dict[key].add(value)

    def add_node (self, key) :
        if not(key in self.dict) :
            self.dict[key] = set()

    def showRoads (self) :
        print(self.dict)


    def removeNode (self, town) :
        self.dict.pop(town)
        self.path.pop(town)
        for key in self.dict :
            try :
                self.dict[key].remove(town)
            except :
                pass

    def BFS(self, start):
        visited = []
        queue = [start]

        while(queue):
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                neighbours = self.dict[node]

                for n in neighbours:
                    queue.append(n)
        return visited

    def isConnected(self, city1, city2):
        return city2 in self.BFS(city1)


# game = Roads();
# game.add_node("R");
# game.add_node("S");
# game.add_node("P");
#
# game.add_road("P","R",False,2);
# game.add_road("R","S",False,2);
# game.add_road("S","P",False,2);
#
# pc_turn = np.random.randint(1,3)
#
# if(pc_turn == 1):
#     turn = "R"
# elif (pc_turn == 2):
#     turn = "S"
# else:
#     turn = "P"
#
# print(turn)
# player = input()
#
# if (game.findConnection(player,turn)):
#     print("won")
# else :
#     print("loose")
#
# roads = Roads()
# roads.add_node("Moscow")
# roads.add_node("Tula")
# roads.add_node("Yaroslavl")
# roads.add_node("Pereslavl")
# roads.add_node("Kazan")
# roads.add_node("Novgorod")
# roads.add_road("Kazan","Novgorod");
# roads.add_road("Moscow", "Tula")
# roads.add_road("Moscow", "Yaroslavl")
# roads.add_road("Tula","Moscow")
# roads.add_road("Yaroslavl","Pereslavl")
# print(roads.isConnected("Kazan","Tula"))
# print(roads.BFS("Tula"))
