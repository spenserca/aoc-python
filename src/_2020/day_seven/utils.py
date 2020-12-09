import re


def get_all_parents(child_parent_graph: dict, bag_type: str):
    parents = set(child_parent_graph[bag_type])
    for parent in child_parent_graph[bag_type]:
        parents |= get_all_parents(child_parent_graph, parent)

    return parents


def build_child_to_parent_graph(bag_rules):
    graph = dict()
    for r in bag_rules:
        bags = re.findall('([a-zA-Z]+\\s[a-zA-Z]+)\\s[b][a][g]', r)
        (parent, children) = bags[0], get_children(bags)

        if parent not in graph:
            graph[parent] = []
        for child in children:
            if child in graph:
                graph[child].append(parent)
            else:
                graph[child] = [parent]
    return graph


def get_children(bags):
    children = bags[1:]
    if 'no other' in children:
        return []
    return children


def get_count_of_bags_containing_bag_type(bag_rules: [str], bag_type: str):
    bag_rules_graph = build_child_to_parent_graph(bag_rules)
    return len(get_all_parents(bag_rules_graph, bag_type))
