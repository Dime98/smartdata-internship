# 26. Given an undirected graph, print all Hamiltonian paths present in it. 
# The Hamiltonian path in an undirected or directed graph is a path that visits each vertex 
# exactly once.

# code from https://www.geeksforgeeks.org/building-an-undirected-graph-and-finding-shortest-path-using-dictionaries-in-python/

# Function to find the shortest
# path between two nodes of a graph
def BFS_SP(graph, start, goal):
    explored = []
     
    # Queue for traversing the
    # graph in the BFS
    queue = [[start]]
     
    # If the desired node is
    # reached
    if start == goal:
        print("Same Node")
        return
     
    # Loop to traverse the graph
    # with the help of the queue
    while queue:
        print()
        print(f"queue {queue}")
        path = queue.pop(0)
        print(f"path  {path}")
        node = path[-1]
        print(f"node  {node}")
         
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
            print(f"neighbours {neighbours}")
             
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                print(f"new_path {new_path}")
                 
                # Condition to check if the
                # neighbour node is the goal
                if neighbour == goal:
                    print("Shortest path = ", *new_path)
                    return
            explored.append(node)
 
    # Condition when the nodes
    # are not connected
    print("So sorry, but a connecting"\
                "path doesn't exist :(")
    return
 
# Driver Code
if __name__ == "__main__":
     
    # Graph using dictionaries
    graph = {'A': ['B', 'E', 'C'],
            'B': ['A', 'D', 'E'],
            'C': ['A', 'F', 'G'],
            'D': ['B', 'E'],
            'E': ['A', 'B', 'D'],
            'F': ['C'],
            'G': ['C']}
     
    # Function Call
    BFS_SP(graph, 'D', 'F')