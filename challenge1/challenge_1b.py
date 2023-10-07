class Node:
    def __init__(self, label):
        self.label = label
        self.inbound = []
        self.outbound = []


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, label):
        node = Node(label)
        self.nodes[label] = node

    def add_edge(self, start, end):
        if start not in self.nodes:
            self.add_node(start)
        if end not in self.nodes:
            self.add_node(end)
        node_start = self.nodes[start]
        node_end = self.nodes[end]
        node_start.outbound.append(node_end)
        node_end.inbound.append(node_start)


def identify_router(graph: Graph):
    max_connections = 0
    router_labels = []
    for label, node in graph.nodes.items():
        connections = len(node.inbound) + len(node.outbound)
        if connections > max_connections:
            max_connections = connections
            router_labels = []
            router_labels.append(label)
        elif connections == max_connections:
            router_labels.append(label)
    return router_labels
