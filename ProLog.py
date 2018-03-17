import Roads

class ProLog:
    dict = {}
    file = None

    def __init__(self, filename):
        self.file = open(filename)
        self.parseLine()


    def parseLine(self):
        for line in self.file:
            str = line.split("(")
            if (str[0][0]=="?"):
                self.parseQuestion()
            elif (str[0]=="exists"):
                self.parseExists()
            else:
                self.parseFact(str[0], self.parseArgiments(str[1]))
                print(self.dict)

    def parseQuestion(self):
        print("parse question")

    def parseExists(self):
        print("parse exists")


    def parseFact(self, fact , arg):
        temp = Roads.Roads()
        if (len(arg) == 1):
            temp.add_node(arg[0])
            temp.add_road(arg[0],arg[0])
        elif (len(arg) == 2):
            temp.add_node(arg[0])
            temp.add_node(arg[1])
            temp.add_road(arg[0],arg[1])
            temp.add_road(arg[1],arg[1])
        else:
            print("too much arguments")

        self.dict[fact] = temp

    def parseArgiments(self, str):
        str = str.replace(')',"").replace('"',"")
        ans = [line.rstrip() for line in str.split(",")]
        return ans

prolog = ProLog("input.txt")
