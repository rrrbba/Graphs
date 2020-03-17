"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

#{} with no colons are sets ex:{'1','2'}
class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        #to add vertex just add another row
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise ValueError("Vertex does not exist!")

    def add_undirected_edge(self, v1, v2):
        """
        Add an undirected edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
            self.vertices[v2].add(v1)
        else:
            raise ValueError("vertex does not exist")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            raise ValueError("Vertex does not exist!")


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #Create a queue
        q = Queue()
        #Enqueue the starting vertex FIFO
        q.enqueue(starting_vertex)
        #Create a set to store visited vertices
        visited = set()
        #While queue isn't empty
        while q.size() > 0:
            #Dequeue the first vertex 
            v = q.dequeue()
            #check if it's been visited
            #if its been visited
            if v not in visited:
                #mark as visited
                print(v)
                visited.add(v)
                #enqueue all of it's neighbors
                for neighbor in self.get_neighbors(v):
                    q.enqueue(neighbor)

 
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #Create a stack
        s = Stack()
        #Push stack to the starting vertex LIFO
        s.push(starting_vertex)
        #Create a set to store visited vertices
        visited = set()
        #While stack isn't empty
        while s.size() > 0:
            #Pop the first vertex 
            v = s.pop()
            #check if it's been visited
            #if its been visited
            if v not in visited:
                #mark as visited
                print(v)
                visited.add(v)
                #Push all of it's neighbors onto the stack
                for neighbor in self.get_neighbors(v):
                    s.push(neighbor)


    def dft_recursive(self, starting_vertex, visited =None): #made visited = set() instead of None so we don't have to do it below
        #so instead of checking if it's none, we just go ahead and check to see if starting_vertex is in visited
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited is None:
            visited = set()
        #check if starting vertex in visited
        if starting_vertex not in visited:
            #if not, mark it as visited
            visited.add(starting_vertex)
            #print starting vertex
            print(starting_vertex)
            #get neighbors of starting vertex
            for neighbor in self.get_neighbors(starting_vertex):
                #call dft_recursive on the neighbor and visited
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #Create a queue
        q = Queue()
        #Enqueue a path to the starting vertex FIFO
        q.enqueue([starting_vertex])
        #Create a set to store visited vertices
        visited = set()
        #While queue isn't empty
        while q.size() > 0:
            #Dequeue the first path
            path = q.dequeue()
            #Grab the vertex from the end of the path
            last_vertex = path[-1]
            #check if it's been visited
            #if its been visited
            if last_vertex not in visited:
                #mark as visited
                visited.add(last_vertex)
                #check if it's the target
                if last_vertex == destination_vertex:
                    #if so return the path
                    return path
                #enqueue a path to all of it's neighbors
                for neighbor in self.get_neighbors(last_vertex):
                    #make a copy of the path
                    copy_path = path.copy()
                    #append the neighbors to the copied path
                    copy_path.append(neighbor)
                    #enqueue the copy to the queue
                    q.enqueue(copy_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #Create a stack
        s = Stack()
        #Push stack to the starting vertex LIFO
        s.push([starting_vertex])
        #Create a set to store visited vertices
        visited = set()
        #While stack isn't empty
        while s.size() > 0:
            #Pop the first vertex 
            path = s.pop()
            #Grab the vertex from the end of the path
            last_vertex = path[-1]
            #check if it's been visited
            #if its been visited
            if last_vertex not in visited:
                #mark as visited
                visited.add(last_vertex)
                #check if it's the target
                if last_vertex == destination_vertex:
                    #if so, return the path
                    return path
                #Push a path to all of it's neighbors
                for neighbor in self.get_neighbors(last_vertex):
                    #make a copy of the path
                    copy_path = path.copy()
                    #append the neighbors to the copied path
                    copy_path.append(neighbor)
                    #push the copy to the stack
                    s.push(copy_path)
                    

#target = destination, LL is a graph
#searches usually return paths because you want to find the path to get there
    def dfs_recursive(self, starting_vertex, destination_vertex, visited = None, path = None): 
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #dfs is utilized stack
        #set looks like {}
        #need path for starting vertex to destination vertex

        #this was giving me an error
        #if path is None:
        # if len(path) == 0:
        #     #return None
        #     return None

        # add starting vertex to visited set
        visited.add(starting_vertex)
        #set path to [starting vertex], if one node in graph
        #path = path + [starting_vertex] 
                #[]   +   [1] = [1]
        #if 1 node in graph, starting vertex = destination vertex
        path = path + [starting_vertex]
        
        if starting_vertex == destination_vertex:
            #return path
            return path

        #loop through a path of neighbors
        for neighbor in self.get_neighbors(starting_vertex):
            #check if neighbor in visited
            if neighbor not in visited:
            #make a copy of the path
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                #if new path
                if new_path:
                    #return new_path
                    return new_path
        
        #return None 
        return None
