def get_count_of_distinct_yes_answers_for_group(group_answers: str):
    return len(set([c for c in group_answers]))


def get_answers_by_group(answers: [str]):
    group_answers = []
    answer = ''
    for a in answers:
        if a == '':
            group_answers.append(answer)
            answer = ''
        else:
            answer += a
    group_answers.append(answer)
    return group_answers


def get_count_of_distinct_yes_answers_for_all_groups(answers: [str]):
    group_answers = get_answers_by_group(answers)

    return sum([get_count_of_distinct_yes_answers_for_group(ga) for ga in group_answers])
