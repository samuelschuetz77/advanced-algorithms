

from collections import deque

#This max_flow_bfs function accepts capacity, source, and sink
# capacity is a dictionary of dictionairies

# ex shape 
# capacity = {
#
#    "s": {"a": 3, "b": 2},
#    "a": {"t": 2},
#    "b": {"t": 2},
#    "t": {},
#             }

#source is start, sink is end
capacities = {
    "s": {"a": 6, "b": 3, "e": 2},
    "a": {"c": 2, "d": 5},
    "b": {"c": 4},
    "c": {"t": 2}, 
    "d": {"t": 5},
    "e": {"g": 1, "f": 1},
    "f": {"g": 1},
    "g": {"t": 2},
    "t": {},
}


# a residual is room left on a directed pipe (after we send flow down towards t from it )

# residual[u][v] stores the current room on the arrow u -> v.

def max_flow_bfs(capacities, start, sink):
    residual = {}
    for u in capacities:
        residual[u] = {}
        for v in capacities[u]:
            residual[u][v] = capacities[u][v]

    total = 0 
    parent = {start:None} # p records which node led us to each new node. The source has no previous node, so its value is none
    queue = deque([start]) #starts one bfs with only start waiting
    while queue and sink not in parent: 
        u = queue.popleft() #takes oldest waiting node each time 
        for v in residual[u]: # visits each possible next node from u
            room = residual[u][v]
            if room > 0 and v not in parent: #It skips pipes with no rooom and aslo skips nodes BFS  already discovered
                parent[v] = u #record from where BFS reached the the new node
                queue.append(v) #add the node to the queue

        if sink not in parent:
            return total

        



            

#1. Start: queue [s], parent contains s.
#2. Process s: discover a, b, e; queue becomes [a, b, e].
#3. Process a: discover c, d; queue becomes [b, e, c, d].
#4. Process b: its pipe to c has room 4, but c is already in parent, so skip it.


    

    



        

    

