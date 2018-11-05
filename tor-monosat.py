# I will try to perform RAPTOR attack on BGP
# I will try to mimic BGP using monosat

from monosat import *
total_relays = 8
class packet:
    source  = BitVector(4)
    relay1  = BitVector(4)
    relay2  = BitVector(4)
    relay3  = BitVector(4)
    dest    = BitVector(4)
    stage   = BitVector(3)
def packet_contsraint(p):
    AssertAnd ( Not(p.source == p.relay1) , Not(p.source == p.relay2) , Not(p.source == p.relay3) , Not(p.source == p.dest),
            Not(p.relay1 == p.relay2) , Not(p.relay1 == p.relay3) , Not(p.relay1 == p.dest) ,
            Not(p.relay2 == p.relay3) , Not(p.relay2 == p.dest)   ,
            Not(p.relay3 == p.dest) , 
            p.source >= 1 , p.source <= total_relays ,
            p.relay1 >= 1 , p.relay1 <= total_relays ,
            p.relay2 >= 1 , p.relay2 <= total_relays ,
            p.relay3 >= 1, p.relay3 <= total_relays ,
            p.dest >= 1 , p.dest <= total_relays
            )

def print_packet(p):
    print(p.source.value())
    print(p.relay1.value())
    print(p.relay2.value())
    print(p.relay3.value())
    print(p.dest.value())

def move_packet(p):
    p.stage = 1
    
    while(p.stage <= 5):
        if(p.stage == 1):
            print("Stage : 1 Previous Node : -1 Current Node :",p.source.value(),"Next Node : ",p.relay1.value())
        elif(p.stage == 2):
            print("Stage : 2 Previous Node : ",p.source.value(),"Current Node :",p.relay1.value() , "Next Node : ",p.relay2.value())
        elif(p.stage == 3):
            print("Stage : 3 Previous Node : ",p.relay1.value(),"Current Node :",p.relay2.value(),"Next Node : ",p.relay3.value())
        elif(p.stage == 4):
            print("Stage : 4 Previous Node : ",p.relay2.value(),"Current Node :",p.relay3.value(),"Next Node : ",p.dest.value())
        elif(p.stage == 5):
            print("Stage : 5 Previous Node : ",p.relay3.value(),"Current Node :",p.dest.value(),"Next Node : -1" )
        p.stage = p.stage + 1



#All values in router will be from added nodes
p1 = packet()


#Let's say there is only one packet in system

packet_contsraint(p1)

Solve()

print_packet(p1)
move_packet(p1)


g = Graph()
# There are eight routers
n1 = g.addNode()
n2 = g.addNode()
n3 = g.addNode()
n4 = g.addNode()
n5 = g.addNode()
n6 = g.addNode()
n7 = g.addNode()
n8 = g.addNode()


#Following are connected graphs with one hop length
g.addUndirectedEdge(n1,n2)
g.addUndirectedEdge(n1,n3)
g.addUndirectedEdge(n1,n4)
g.addUndirectedEdge(n2,n3)
g.addUndirectedEdge(n3,n5)
g.addUndirectedEdge(n3,n6)
g.addUndirectedEdge(n4,n5)
g.addUndirectedEdge(n4,n8)
g.addUndirectedEdge(n5,n7)
g.addUndirectedEdge(n6,n7)
g.addUndirectedEdge(n6,n8)
g.addUndirectedEdge(n7,n8)

