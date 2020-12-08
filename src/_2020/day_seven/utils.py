import re


def recursive_something(bags_to_check: [str], bag_rules_dict: dict, bag_type: str):
    bag_count = 0
    for bag in bags_to_check:
        if bag_type in bag_rules_dict[bag]:
            bag_count += 1
        else:
            bag_count += recursive_something(bag_rules_dict.keys(), bag_rules_dict, bag_type)

    return bag_count


def get_count_of_bags_containing_bag_type(bag_rules: [str], bag_type: str):
    bag_rules_graph = parse_rules(bag_rules)

    # for container bags
    # if they hold a bag_type increment by 1
    # else for each bag it holds check if it holds a bag_type

    return recursive_something(bag_rules_graph.keys(), bag_rules_graph, bag_type)


def parse_rules(bag_rules):
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
