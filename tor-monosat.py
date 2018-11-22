# I will try to perform RAPTOR attack on BGP
# I will try to mimic BGP using monosat
import math
from monosat import *
def find_shortest_distance(node1 , node2 , l , r , g):
    i = l
    while(1):
        if Solve([g.distance_leq(node1,node2,i)]):
            return i
        else:
            i = i + 1

def find_shortest_distance_b(node1 , node2 , l , r ,g):
    i = l
    count = 1
    while(1):
        if i < l or i > r:
            return find_shortest_distance(node1 , node2 , l ,r , g)
        if Solve([g.distance_leq(node1,node2,i)]):
            if i+1 == r or i == 1:

                return i
            else:
                return find_shortest_distance_b(node1 , node2 , math.ceil(l/2) + 1 , l , g)
        else:
            count = count*2
            i = i + count
    
def find_total_shortest_paths(node1 , node2 ,nodes,g):
    distance = find_shortest_distance_b(node1 , node2 , 1, nodes-1 , g)
    return find_total_paths(node1, node2, distance, nodes, g)

def find_total_paths(node1 , node2 , distance ,nodes,g):
    count = 0
    if find_shortest_distance_b(node1 , node2 , 1, nodes-1,g) == 1:
        return 1
    list1 = find_neighbours(node1 , 1,nodes, g)
    list2 = list1.copy()
    for i in list1:
        if find_shortest_distance_b(i,node2, 1 , nodes-1, g) != distance-1:
            list2.remove(i)
    list1 = list2.copy()
    for i in list1:
        count = count + find_total_paths(i,node2,distance-1,nodes, g)
    return count

def find_neighbours(node,distance,nodes,g):
   neighbours = []
   for i in range(nodes):
        if Solve([g.distance_lt(node,i,distance+1), ~g.distance_lt(node,i,distance)]):
            neighbours.append(i)
   return neighbours


def print_shortest_distances(nodes1,nodes2,g1,g2):
    print("First value is shortest distance without attacker node") 
    print("Second value is shortest distance with attacker node")
    print("Third value is total shortest paths in graph with attacker node")
    print("Fourth value is number of malicious paths out of shortest paths")
    print(end = '      ')
    for i in range(nodes1):
        print(i,end='         ')
    print()
    for i in range(nodes1):
        print(i ,":", end=' ')
        for j in range(nodes1):
            if i != j:
                a = find_shortest_distance_b(i,j,1,nodes1-1,g1)
                b = find_shortest_distance_b(i,j,1,nodes2,g2)
                print(a,b, end=' ')
                print(find_total_shortest_paths(i,j,nodes2,g2),end=' ')
                if a == b:
                    print(find_total_shortest_paths(i,j,nodes2,g2) - find_total_shortest_paths(i,j,nodes1,g1), end=' ')
                else:
                    print(find_total_shortest_paths(i,j,nodes2,g2),end=' ')
            else:
                print("0 0 0 0",end=' ')
            print(end='  ')
        print()

g1 = Graph()

n0 = g1.addNode()
n1 = g1.addNode()
n2 = g1.addNode()
n3 = g1.addNode()
n4 = g1.addNode()
n5 = g1.addNode()

g1.addUndirectedEdge(n0,n2)

g1.addUndirectedEdge(n1,n4)

g1.addUndirectedEdge(n2,n4)
g1.addUndirectedEdge(n2,n5)

g1.addUndirectedEdge(n3,n4)
g1.addUndirectedEdge(n3,n5)



g2 = Graph()

n0 = g2.addNode()
n1 = g2.addNode()
n2 = g2.addNode()
n3 = g2.addNode()
n4 = g2.addNode()
n5 = g2.addNode()
n6 = g2.addNode() # Attacker

g2.addEdge(n0,n2)

g2.addEdge(n1,n4)

g2.addEdge(n2,n0)
g2.addEdge(n2,n4)
g2.addEdge(n2,n5)

g2.addEdge(n3,n4)
g2.addEdge(n3,n5)

g2.addEdge(n4,n1)
g2.addEdge(n4,n2)
g2.addEdge(n4,n3)

g2.addEdge(n5,n2)
g2.addEdge(n5,n3)

g2.addEdge(n6,n0)
g2.addEdge(n6,n1)
g2.addEdge(n6,n2)
g2.addEdge(n6,n3)
g2.addEdge(n6,n4)
g2.addEdge(n6,n5)

g2.addEdge(n4,n6)
g2.addEdge(n5,n6)

print_shortest_distances(6,7,g1,g2)


g3 = Graph()


n0 = g3.addNode()
n1 = g3.addNode()
n2 = g3.addNode()
n3 = g3.addNode()
n4 = g3.addNode()
n5 = g3.addNode()
n6 = g3.addNode() # Attacker
n7 = g3.addNode()
n8 = g3.addNode()

n9 = g3.addNode()
n10 = g3.addNode()
n11 = g3.addNode()
n12 = g3.addNode()
n13 = g3.addNode()
n14 = g3.addNode() # Attacker
n15 = g3.addNode()
n16 = g3.addNode()

n17 = g3.addNode()
n18 = g3.addNode()
n19 = g3.addNode()
n20 = g3.addNode()
n21 = g3.addNode()
n22 = g3.addNode()
n23 = g3.addNode()
n24 = g3.addNode()

n25 = g3.addNode() # Attacker
n26 = g3.addNode()
n27 = g3.addNode()
n28 = g3.addNode()
n29 = g3.addNode()
n30 = g3.addNode()
n31 = g3.addNode()
n32 = g3.addNode()

n33 = g3.addNode()
n34 = g3.addNode() # Attacker
n35 = g3.addNode()
n36 = g3.addNode()
n37 = g3.addNode() 
n38 = g3.addNode() # Attacker
n39 = g3.addNode()
n40 = g3.addNode()

n41 = g3.addNode()
n42 = g3.addNode()
n43 = g3.addNode()
n44 = g3.addNode()
n45 = g3.addNode()
n46 = g3.addNode()
n47 = g3.addNode()
n48 = g3.addNode()

n49 = g3.addNode()
n50 = g3.addNode()



#Following are edges of connected graphs with one hop length
g3.addUndirectedEdge(n0,n49)
g3.addUndirectedEdge(n0,n24)

g3.addUndirectedEdge(n1,n3)
g3.addUndirectedEdge(n1,n7)
g3.addUndirectedEdge(n1,n49)

g3.addUndirectedEdge(n2,n6)
g3.addUndirectedEdge(n2,n7)
g3.addUndirectedEdge(n2,n23)

g3.addUndirectedEdge(n3,n5)
g3.addUndirectedEdge(n3,n6)

g3.addUndirectedEdge(n4,n5)
g3.addUndirectedEdge(n4,n9)

g3.addUndirectedEdge(n5,n9)

g3.addUndirectedEdge(n6,n48)

g3.addUndirectedEdge(n7,n49)

g3.addUndirectedEdge(n8,n9)
g3.addUndirectedEdge(n8,n13)
g3.addUndirectedEdge(n8,n47)

g3.addUndirectedEdge(n9,n10)
g3.addUndirectedEdge(n9,n13)

g3.addUndirectedEdge(n10,n12)

g3.addUndirectedEdge(n11,n12)
g3.addUndirectedEdge(n11,n17)
g3.addUndirectedEdge(n11,n18)

g3.addUndirectedEdge(n12,n14)

g3.addUndirectedEdge(n13,n14)
g3.addUndirectedEdge(n13,n15)
g3.addUndirectedEdge(n13,n16)
g3.addUndirectedEdge(n13,n47)

g3.addUndirectedEdge(n14,n16)
g3.addUndirectedEdge(n14,n17)
g3.addUndirectedEdge(n14,n50)

g3.addUndirectedEdge(n15,n25)
g3.addUndirectedEdge(n15,n26)
g3.addUndirectedEdge(n15,n47)

g3.addUndirectedEdge(n16,n20)
g3.addUndirectedEdge(n16,n26)

g3.addUndirectedEdge(n18,n19)
g3.addUndirectedEdge(n18,n50)

g3.addUndirectedEdge(n19,n20)

g3.addUndirectedEdge(n20,n27)
g3.addUndirectedEdge(n20,n35)
g3.addUndirectedEdge(n20,n50)

g3.addUndirectedEdge(n21,n22)
g3.addUndirectedEdge(n21,n25)
g3.addUndirectedEdge(n21,n28)
g3.addUndirectedEdge(n21,n29)

g3.addUndirectedEdge(n22,n25)
g3.addUndirectedEdge(n22,n48)

g3.addUndirectedEdge(n23,n24)
g3.addUndirectedEdge(n23,n48)
g3.addUndirectedEdge(n23,n49)

g3.addUndirectedEdge(n24,n28)
g3.addUndirectedEdge(n24,n46)

g3.addUndirectedEdge(n25,n30)
g3.addUndirectedEdge(n25,n31)
g3.addUndirectedEdge(n25,n32)

g3.addUndirectedEdge(n26,n32)
g3.addUndirectedEdge(n26,n33)

g3.addUndirectedEdge(n27,n36)

g3.addUndirectedEdge(n28,n34)
g3.addUndirectedEdge(n28,n48)

g3.addUndirectedEdge(n29,n30)
g3.addUndirectedEdge(n29,n44)

g3.addUndirectedEdge(n30,n44)

g3.addUndirectedEdge(n31,n37)
g3.addUndirectedEdge(n31,n44)

g3.addUndirectedEdge(n32,n37)
g3.addUndirectedEdge(n32,n38)

g3.addUndirectedEdge(n33,n35)

g3.addUndirectedEdge(n34,n44)
g3.addUndirectedEdge(n34,n46)

g3.addUndirectedEdge(n35,n38)

g3.addUndirectedEdge(n36,n41)
g3.addUndirectedEdge(n36,n42)

g3.addUndirectedEdge(n37,n39)
g3.addUndirectedEdge(n37,n40)
g3.addUndirectedEdge(n37,n41)
g3.addUndirectedEdge(n37,n43)
g3.addUndirectedEdge(n37,n44)

g3.addUndirectedEdge(n38,n41)

g3.addUndirectedEdge(n39,n44)
g3.addUndirectedEdge(n39,n45)

g3.addUndirectedEdge(n40,n41)

g3.addUndirectedEdge(n41,n43)



