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
        graph.add_edge(node[0], node[1])
        # print(graph)
    #return ancestor at farthest distance from input
    q = Queue()
    # print(f'{ancestors}')
    q.enqueue([starting_node])
    # print(starting_node)
    visited = set()
    #
    while q.size() > 0:
        path = q.dequeue()
        # print(path)
        last_node = path[-1]
        # print(last_node)
        if last_node not in visited:
            visited.add(last_node)
            print(visited)
    #if there is a tie for earliest ancestor,
    
        #return one with lowest id

    #if no parents
        #return -1
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]
print(earliest_ancestor(test_ancestors,1))