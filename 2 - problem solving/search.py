

def breadth_first_search(graph, start, end):
    queue = [(start, [start])]

    while queue:
        (node, path) = queue.pop(0)
        for next in set(graph[node]) - set(path):
            if next == end:
                return path + [next]
            else:
                queue.append((next, path + [next]))


def depth_first_search(graph, start, end, path=[]):
    path = path + [start]

    # we're there
    if start == end:
        return path

    # dead end
    if not start in graph:
        return None

    shortest = None

    # try all the options
    for node in graph[start]:
        if node not in path:
            newpath = depth_first_search(graph, node, end, path)

            # return first good option
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath

    return shortest
