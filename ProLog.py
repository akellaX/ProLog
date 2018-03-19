import Roads

class ProLog:
    storage = {}
    file = None

    def __init__(self, filename):
        self.file = open(filename)
        self.parseLine()


    def parseLine(self):
        for line in self.file:
            str = line.split("(", maxsplit=1)
            if (str[0][0] == "?"):
                print(line.rstrip())
                print(self.parseQuestion(str[0],self.parseArgiments(str[1])))
            elif (str[0] == "exists"):
                print(line.rstrip())
                self.parseExists(str[1])
            else:
                print(line.rstrip())
                self.parseFact(str[0], self.parseArgiments(str[1]))
    def parseQuestion(self, fact, arg):
        fact = fact.replace("?","").rstrip()
        if (len(arg) == 1):
            return self.storage[fact].isKey(arg[0])
        elif (len(arg) == 2):
            return self.storage[fact].isConnected(arg[0],arg[1])

    def parseExists(self, str):
        str1 = str.split(":")
        variables = str1[0].replace(" ","").split(",")
        str1 = str1[1].replace(" ","").rstrip().split(")",maxsplit=1)
        fact_left = str1[0];
        fact_left = fact_left.split("(")
        arguments_left = fact_left[1].split(",")
        fact_left = fact_left[0]

        str1 = str1[1].replace(")->","").rstrip()
        temp = []
        while (str1.count(")") > 1):
            temp.append(str1.split(")")[0])
            str1 = str1.split(")",maxsplit=1)[1]
            if(str1[0] == ","):
                str1 = str1[1:]
        temp.append(str1)
        fact_right = dict()
        for i in temp:
            fact = i.split("(")[0]
            arguments = self.parseArgiments(i.split("(")[1])
            fact_right[fact] = arguments
        dict_left = dict()
        xy = self.storage[fact_left].getXY()
        if (len(arguments_left) == 1):
            dict_left[arguments_left[0]] = xy
        else:
            dict_left[arguments_left[0]] = xy[0]
            dict_left[arguments_left[1]] = xy[1]
        pair = self.storage[fact_left].getPairList(False)
        pair_rev = self.storage[fact_left].getPairList(True)

        for key, value in fact_right.items():
            if(len(value) == 1):
                for j in dict_left[next(iter(value))]:
                    self.parseOneFact(key,j)
            elif(len(value) == 2):
                if("".join(arguments_left) == "".join(value)):
                    for k in pair:
                        self.parseFact(key,k.split(","))
                else:
                    for k in pair_rev:
                        self.parseFact(key,k.split(","))




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

    def parseOneFact(self, fact , arg):
        if(not fact in self.storage):
            self.storage[fact] = Roads.Roads()
        self.storage[fact].add_node(arg)
        self.storage[fact].add_road(arg,arg)

    def parseArgiments(self, str):
        str = str.replace(')',"").replace('"',"").replace("'","")
        ans = [line.rstrip() for line in str.split(",")]
        return ans

prolog = ProLog("input.txt")
