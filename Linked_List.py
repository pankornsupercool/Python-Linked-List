class Node:
    def __init__(self, name = None):
        self.name = name
        self.nextNode = None

class LinkedList:
    def __init__(self):
        self.headNode = None

    def printValue(self):
        printval = self.headNode
        while printval is not None :
            print(printval.name,end = "")
            printval = printval.nextNode

    

file = open("data.txt", "r")
content = file.readline()

list_1 = LinkedList()
list_1.headNode = Node(content)
cur = list_1.headNode

for line in file:
    newNode = Node(line)
    cur.nextNode = newNode
    cur = cur.nextNode

list_1.printValue()