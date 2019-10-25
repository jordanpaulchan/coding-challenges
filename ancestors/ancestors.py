def create_ancestor_graph(relationships):
    ancestor_graph = {}
    for parent, child in relationships:
        if parent not in ancestor_graph:
            ancestor_graph[parent] = []

        if child not in ancestor_graph:
            ancestor_graph[child] = []

        ancestor_graph[child].append(parent)

    return ancestor_graph


def earliest_ancestor(child, ancestor_graph):
    if child not in ancestor_graph or not ancestor_graph[child]:
        return -1

    queue = [child]
    visited = set()

    while queue:
        tempq = []
        for person in queue:
            for ancestor in ancestor_graph[person]:
                if ancestor not in visited:
                    visited.add(ancestor)
                    tempq.append(ancestor)

        if not tempq:
            return queue[0]

        queue = tempq

    return -1


def get_all_ancestors(child, ancestor_graph):
    if child not in ancestor_graph or not ancestor_graph[child]:
        return set()

    queue = [child]
    visited = set()

    while queue:
        tempq = []
        for person in queue:
            for ancestor in ancestor_graph[person]:
                if ancestor not in visited:
                    visited.add(ancestor)
                    tempq.append(ancestor)

        queue = tempq

    return visited


def has_common_ancestor(child1, child2, ancestor_graph):
    child1_ancestors = get_all_ancestors(child1, ancestor_graph)
    child2_ancestors = get_all_ancestors(child2, ancestor_graph)

    return len(child1_ancestors & child2_ancestors) > 0


def one_or_zero_parents(ancestor_graph):
    children = []
    for child in ancestor_graph.keys():
        if len(ancestor_graph[child]) <= 1:
            children.append(child)
    return children


parent_child_pairs1 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 4),
]
ancestor_graph1 = create_ancestor_graph(parent_child_pairs1)
print(earliest_ancestor(8, ancestor_graph1))  # 14
print(earliest_ancestor(7, ancestor_graph1))  # 14
print(earliest_ancestor(6, ancestor_graph1))  # 14
print(earliest_ancestor(15, ancestor_graph1))  # 2
print(earliest_ancestor(14, ancestor_graph1))  # -1
print()
print(has_common_ancestor(3, 8, ancestor_graph1))  # false
print(has_common_ancestor(5, 8, ancestor_graph1))  # true
print(has_common_ancestor(6, 8, ancestor_graph1))  # true
print(has_common_ancestor(6, 9, ancestor_graph1))  # true
print(has_common_ancestor(1, 3, ancestor_graph1))  # false
print(has_common_ancestor(7, 11, ancestor_graph1))  # true
print(has_common_ancestor(6, 5, ancestor_graph1))  # true
print(has_common_ancestor(5, 6, ancestor_graph1))  # true
print()
print(one_or_zero_parents(ancestor_graph1))
print()

parent_child_pairs2 = [
    (2, 3), (3, 15), (3, 6), (5, 6), (5, 7),
    (4, 5), (4, 8), (4, 9), (9, 11), (14, 2),
]
ancestor_graph2 = create_ancestor_graph(parent_child_pairs2)
print(earliest_ancestor(8, ancestor_graph2))  # 4
print(earliest_ancestor(7, ancestor_graph2))  # 4
print(earliest_ancestor(6, ancestor_graph2))  # 14
print(earliest_ancestor(15, ancestor_graph2))  # 14
print(earliest_ancestor(14, ancestor_graph2))  # -1
print()
print(has_common_ancestor(4, 12, ancestor_graph2))  # false
print(has_common_ancestor(11, 6, ancestor_graph2))  # true
print(has_common_ancestor(11, 3, ancestor_graph2))  # false
print()
print(one_or_zero_parents(ancestor_graph2))
