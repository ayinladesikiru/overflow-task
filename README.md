Challenge 1a
The time complexity of the compress function, the challenge 1 a O(n), where n is the length of the input string.
This is because the function iterates over the input string once, and the number of operations performed in the
loop is constant. The only additional operation performed is the concatenation of the compressed string at the end
of the function, but this operation also takes constant time.


Challenge 1b
Time complexity of the identify_router() the challenge 1b is O(V + E),
where V is the number of nodes in the graph and E is the number of edges in the graph.
This is because the function iterates over all of the nodes in the graph once, and for each node, it iterates over all of the node's inbound and outbound edges. This results in a total of O(V + E) operations.

Pipenv is used to create the virtul environment and use as package manager
requests module is used to call the etherscan endpoint
pytest framework is used to test the functions

encounter a little challenge in the response i got from calling the etherscan endpoint in the API documentation provided in the question, there has been some changes in the response data.
