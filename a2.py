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
    if frontier == []:
        return None
    cost = frontier[0].f
    returnNode = frontier[0]
    for node in frontier:
        if node.f < cost:
            cost = node.f
            returnNode = node
    return returnNode

# expand_frontier -- takes a node, a list of nodes, the adjacency matrix, and a node
# returns the updated frontier, as described in assignment description
def expand_frontier(to_explore, frontier, adjacencyMatrix, goal_state):
    frontier.remove(to_explore)
    for path in adjacencyMatrix:
        node = path[0]
        if node == to_explore:
            add_node = path[1]
            add_node.g = path[2] + node.g
            add_node.h = euclideanDistance(add_node, goal_state)
            add_node.f = add_node.g + add_node.h
            if add_node in frontier:
                old_node = frontier[frontier.index(add_node)]
                if add_node.f < old_node.f:
                    frontier.remove(old_node)
                    frontier.append(add_node)
            else:
                frontier.append(add_node)
    return frontier

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
        n = find_node_to_explore(frontier)
        frontier = expand_frontier(n, frontier, adjacencyMatrix, goalNode)
        explored.append(n)
        if n.name == goalNode.name:
            found = True

        #printing procedure to see your progress
        if (debug):
            print("frontier:")
            for node in frontier:
                print(node.str())
            print("explored:")
            for node in explored:
                print(node.str())

        # Once search is finished, show results
        if found:
           print("frontier:")
           for node in frontier:
               print(node.str())
               print("explored:")
           for node in explored:
               print(node.str())
           print("We found the goal!")
           return explored, explored[len(explored)-1].f
        else:
            print("Goal not found :(")
            return explored, 0



# Main method. Add more tests!
def main():

    #Test for AI City Graph, starting at A with goal node F
    result = aStar(AI_CITY_NODE_LIST, AI_CITY_ADJ_LIST, AI_nodeF, AI_nodeA)
    for i in result[0]:
        print(i.name)
    print ("Total Path Cost: %d" % result[1])
    #add your own tests below!

    # Test euclidean distance.
    aNode = Node('A', 3, 4)
    bNode = Node('B', 0, 0)
    calculatedDistance = euclideanDistance(aNode, bNode)
    print("Expected: %d" % 5.0)
    print(calculatedDistance)

    cNode = Node('C', 12, 13)
    dNode = Node('D', 0, 0)
    calculatedDistance = euclideanDistance(cNode, dNode)
    print("Expected: %d" % 14.0)
    print(calculatedDistance)

    eNode = Node('E', 0, 0)
    fNode = Node('F', 0, 0)
    calculatedDistance = euclideanDistance(eNode, fNode)
    print("Expected: %d" % 0.0)
    print(calculatedDistance)

    # Test find_node_to_exlpore.
    aNode.f = 7
    bNode.f = 12
    cNode.f = 2
    dNode.f = 3
    eNode.f = 6
    nodeList = [aNode, bNode, cNode, dNode, eNode]
    returnedNode = find_node_to_explore(nodeList)
    print("Expected node returned: C")
    print(returnedNode.name)

    aNode.f = 0
    bNode.f = 0
    cNode.f = 0
    dNode.f = 0
    eNode.f = 0
    nodeList = [aNode, bNode, cNode, dNode, eNode]
    returnedNode = find_node_to_explore(nodeList)
    print("Expected node returned: A")
    print(returnedNode.name)

    nodeList = []
    returnedNode = find_node_to_explore(nodeList)
    print("Expected node returned: None")
    print(returnedNode)

    # Test expand_frontier.
    ADJ_TEST_LIST = [[aNode, bNode, 5],
                        [aNode, cNode, 4],
                        [bNode, dNode, 11]]
    frontier = expand_frontier(aNode, [aNode], ADJ_TEST_LIST, fNode)
    frontierSize = len(frontier)
    print("Expected length: 2")
    print(frontierSize)
    print("Expected frontier: [B, C]")
    for node in frontier:
        print(node.name)

    frontier = expand_frontier(dNode, [dNode], ADJ_TEST_LIST, fNode)
    frontierSize = len(frontier)
    print("Expected length: 0")
    print(frontierSize)
    print("Expected frontier: []")
    print(frontier)

if __name__ == "__main__": main()



    
