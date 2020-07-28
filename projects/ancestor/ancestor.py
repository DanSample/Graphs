
def earliest_ancestor(ancestors, starting_node):
    # create a hashtable
    lookup = {}
    # iterate over the ancestors
    for pair in ancestors:
        # if the pair is not in the hashtable
        if pair[1] not in lookup:
            lookup[pair[1]] = [pair[0]]
        else:
            lookup[pair[1]].append(pair[0])
    # DFT through the nodes to get to the last generation
    def recursive(graph, vertex):
            # if the vertex is not in the graph
            if vertex not in graph:
                # return 1 and the vertex
                return (1, vertex)
            # create a list for the results
            results = []
            # iterate over the graph
            for val in graph[vertex]:
                # append the recursion to the results
                results.append(recursive(graph, val))

            # if only one ancestor
            if len(results) == 1:
                return (results[0][0] + 1, results[0][1])

            # if there are two ancestors, compare them
            if results[0][0] > results[1][0]:
                return (results[0][0] + 1, results[0][1])
            elif results[0][0] < results[1][0]:
                return (results[1][0] + 1, results[1][1])
            else:
                # if the same age, return lowest ID
                if results[0][1] < results[1][1]:
                    return (results[0][0] + 1, results[0][1])
                else:
                    return (results[1][0] + 1, results[1][1])

    # get earliest ancestor and deal with cases where
    # the one picked is the earliest ancestor
    earliest = recursive(lookup, starting_node)
    if earliest[0] == 1:
        return -1
    else:
        return earliest[1]