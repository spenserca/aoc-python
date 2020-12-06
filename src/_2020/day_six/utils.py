def get_count_of_distinct_yes_answers_for_group(group_answers: [str]):
    group_answer_string = ''.join(group_answers)
    return len(set([c for c in group_answer_string]))


def get_answers_by_group(answers: [str]):
    group_answers = []
    current_group_answers = []
    for a in answers:
        if a == '':
            group_answers.append(current_group_answers)
            current_group_answers = []
        else:
            current_group_answers.append(a)
    group_answers.append(current_group_answers)
    return group_answers


def get_count_of_distinct_yes_answers_for_all_groups(answers: [str]):
    group_answers = get_answers_by_group(answers)

    return sum([get_count_of_distinct_yes_answers_for_group(ga) for ga in group_answers])


def get_count_of_questions_all_answered_yes_to(answers: [str]):
    group_answers = get_answers_by_group(answers)
    yes_count = 0
    for ga in group_answers:
        group_member_count = len(ga)
        group_answer_string = ''.join(ga)
        processed_answers = []
        for c in group_answer_string:
            if group_answer_string.count(c) == group_member_count and c not in processed_answers:
                yes_count += 1
                processed_answers.append(c)

    return yes_count
