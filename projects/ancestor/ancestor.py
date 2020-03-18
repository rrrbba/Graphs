class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        #to add vertex just add another row
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()
        #keys are vertices and the set (values) are relationships that they have and in this case it's the parents


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


def earliest_ancestor(ancestors, starting_node):
    '''
    Write a function that, given the dataset and the ID of an individual in the dataset, returns their earliest known ancestor – the one at the farthest distance from the input individual. 
    If there is more than one ancestor tied for "earliest", return the one with the lowest numeric ID. 
    If the input individual has no parents, the function should return -1.
    '''
    #use bfs
    #intiate a graph to use
    graph = Graph()
    
    #iterate through ancestors
    for node in ancestors:
        # print(node)
        #add vertices to graph
        graph.add_vertex(node[0])
        graph.add_vertex(node[1])
        
        #add edges(connections between vertices)
        graph.add_edge(node[1], node[0])
        print(graph.vertices)
    #return ancestor at farthest distance from input
    q = Queue()
    # print(f'{ancestors}')
    q.enqueue([starting_node])
    #initialize longest path variable with path of starting node
    longest_path = [starting_node]
    while q.size() > 0:
        #dequeue the first path
        path = q.dequeue()
        # get last node of the path
        last_node = path[-1]
        #since we want longest path, check if path is longer than longest path
        if len(path) > len(longest_path):
            #if true, switch them
            longest_path = path
        #if there is a tie for earliest ancestor, (edge case)
        elif len(path) == len(longest_path):
            #if last node < id at the end of longest path
            if last_node < longest_path[-1]:
                #switch them
                longest_path = path
        #get neighbors of the last node
        for neighbors in graph.get_neighbors(last_node):
            #make a copy of the path
            path_copy = path.copy()
            #add the neighbors to the copy
            path_copy.append(neighbors)
            #add copied path to queue
            q.enqueue(path_copy)
            # print(visited)
    #if no parents (edge case)
    if starting_node == longest_path[-1]:
        #return -1
        return -1
    
    #return earliest ancestor of starting node from the longest path
    return longest_path[-1]


    
        
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors,9))