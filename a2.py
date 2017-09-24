from math import sqrt
from copy import deepcopy

class Node(object):
    # constructor for Node objects
    def __init__(self, name, posx, posy):
        self.name = name
        self.x = posx
        self.y = posy
        self.g = 0
        self.h = 0
        self.f = self.g + self.h

    # method to print Node objects -- feel free to modify!
    def str(self):
        return "Name: " + self.name + " Cost: " + str(self.f)

# AI City Graph representation
AI_nodeA = Node('A', -6, -2)
AI_nodeB = Node('B', -3, 2)
AI_nodeC = Node('C', -4, -3)
AI_nodeD = Node('D', 2, 4)
AI_nodeE = Node('E', 1, 0)
AI_nodeF = Node('F', 6, 5)

# node list
AI_CITY_NODE_LIST = [AI_nodeA, AI_nodeB, AI_nodeC, AI_nodeD, AI_nodeE, AI_nodeF]

# adjacency list
AI_CITY_ADJ_LIST = [[AI_nodeA, AI_nodeB, 5],
          [AI_nodeA, AI_nodeC, 4],
          [AI_nodeA, AI_nodeD, 11],
          [AI_nodeB, AI_nodeC, 6],
          [AI_nodeB, AI_nodeD, 5],
          [AI_nodeB, AI_nodeE, 5],
          [AI_nodeC, AI_nodeD, 10],
          [AI_nodeC, AI_nodeE, 5],
          [AI_nodeD, AI_nodeE, 5],
          [AI_nodeD, AI_nodeF, 5],
          [AI_nodeE, AI_nodeD, 5],
          [AI_nodeC, AI_nodeF, 16]]

# Heuristic function -- takes two nodes, returns a number: the Euclidean distance 
# between aNode and bNode
def euclideanDistance(aNode, bNode):
    return sqrt(((aNode.x-bNode.x)**2) + ((aNode.y-bNode.y)**2))
# find_node_to_explore -- takes a list of nodes, returns a node:
# the lowest-cost node in the frontier
def find_node_to_explore(frontier):
    #TODO
    return None

# expand_frontier -- takes a node, a list of nodes, the adjacency matrix, and a node
# returns the updated frontier, as described in assignment description
def expand_frontier(to_explore, frontier, adjacencyMatrix, goal_state):
    #TODO
    return frontier
'''           
# aStar -- full A* function: takes a list of nodes, an adjacency matrix, a start node, and a goal node
# feel free to turn debugging (printing) on/off as you wish
def aStar(nodeList, adjacencyMatrix, startNode, goalNode, debug=True):
    #Our hint to you -- getting started
    startNode.h = euclideanDistance(startNode, goalNode)
    startNode.g = 0
    startNode.f = startNode.g + startNode.h
    frontier = [startNode]
    explored = []
    found = False

    while(frontier != []):
        #printing procedure to see your progress
        if (debug):
            print("frontier:")
            for node in frontier:
                print node.str()
            print("explored:")
            for node in explored:
                print node.str()
        #TODO       
        


    # Once search is finished, show results
    if found:
        print("frontier:")
        for node in frontier:
            print node.str()
        print("explored:")
        for node in explored:
            print node.str()
        print "We found the goal!"
    else: print "Goal not found :("
'''
# Main method. Add more tests!
def main():
    '''
    #Test for AI City Graph, starting at A with goal node F
    result = aStar(AI_CITY_NODE_LIST, AI_CITY_ADJ_LIST, AI_nodeA, AI_nodeF)
    for i in result[0]:
        print(i.name)
        print ("Total Path Cost: %d" % result[1])
    #add your own tests below!
    '''
    aNode = Node("A", 5, 6)
    bNode = Node("B", 2, 2)
    print(euclideanDistance(aNode,bNode))


if __name__ == "__main__": main()


    
