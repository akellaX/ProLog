import Roads

class ProLog:
    storage = {}
    file = None

    def __init__(self, filename):
        self.file = open(filename)
        self.parseLine()


    def parseLine(self):
        for line in self.file:
            str = line.split("(")
            if (str[0][0] == "?"):
                print(line.rstrip())
                print (self.parseQuestion(str[0],self.parseArgiments(str[1])))
            elif (str[0] == "exists"):
                print(line.rstrip())
                self.parseExists()
            else:
                print(line.rstrip())
                self.parseFact(str[0], self.parseArgiments(str[1]))

    def parseQuestion(self, fact, arg):
        fact = fact.replace("?","").rstrip()
        if (len(arg) == 1):
            return self.storage[fact].isKey(arg[0])
        elif (len(arg) == 2):
            return self.storage[fact].isConnected(arg[0],arg[1])

    def parseExists(self):
        print("parse exists")


    def parseFact(self, fact , arg):
        if(not fact in self.storage):
            self.storage[fact] = Roads.Roads()
        if (len(arg) == 1):
            self.storage[fact].add_node(arg[0])
            self.storage[fact].add_road(arg[0],arg[0])
        elif (len(arg) == 2):
            self.storage[fact].add_node(arg[0])
            self.storage[fact].add_node(arg[1])
            self.storage[fact].add_road(arg[0],arg[1])
            self.storage[fact].add_road(arg[1],arg[1])
        else:
            print("too much arguments")

    def parseArgiments(self, str):
        str = str.replace(')',"").replace('"',"").replace("'","")
        ans = [line.rstrip() for line in str.split(",")]
        return ans

prolog = ProLog("input1.txt")
