import re


def get_all_parents(child_parent_graph: dict, bag_type: str):
    parents = set(child_parent_graph[bag_type])
    for parent in child_parent_graph[bag_type]:
        parents |= get_all_parents(child_parent_graph, parent)

    return parents


def build_child_to_parent_graph(bag_rules):
    graph = dict()
    for r in bag_rules:
        parent, children = get_parent_children(r)

        if parent not in graph:
            graph[parent] = []
        for (count, child) in children:
            if child in graph:
                graph[child].append(parent)
            else:
                graph[child] = [parent]
    return graph


def get_parent_children(rule: str):
    parent = ' '.join(rule.split(' ')[0:2])
    child_bags = re.findall('([0-9]+\\s[a-zA-Z]+\\s[a-zA-Z]+)\\s[b][a][g]', rule)
    # children = [(count1, child1), (count2, child2), ...]
    children = parse_child_bags(child_bags)
    return parent, children


def parse_child_bags(child_bags: [str]):
    children = []
    for child in child_bags:
        child_pieces = child.split(' ')
        children.append((int(child_pieces[0]), ' '.join(child_pieces[1:])))

    if 'no other' in children:
        return []
    return children


def get_count_of_bags_containing_bag_type(bag_rules: [str], bag_type: str):
    bag_rules_graph = build_child_to_parent_graph(bag_rules)
    return len(get_all_parents(bag_rules_graph, bag_type))


def get_count_of_bags_contained_in_bag_type(bag_rules_graph, bag_type):
    bag_count = 0
    for (count, child) in bag_rules_graph[bag_type]:
        bag_count += count
        bag_count += count * get_count_of_bags_contained_in_bag_type(bag_rules_graph, child)
    return bag_count


def get_count_of_total_bags_for_bag_type(bag_rules: [str], bag_type: str):
    bag_rules_graph = dict([get_parent_children(r) for r in bag_rules])

    return get_count_of_bags_contained_in_bag_type(bag_rules_graph, bag_type)
