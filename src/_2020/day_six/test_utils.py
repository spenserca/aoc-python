from _2020.day_six.utils import get_count_of_distinct_yes_answers_for_group, \
    get_count_of_distinct_yes_answers_for_all_groups


def test_get_count_of_distinct_yes_answers_for_group_returns_6_for_given_input():
    group_answers = 'abcxabcyabcz'
    actual = get_count_of_distinct_yes_answers_for_group(group_answers)
    assert actual == 6


def test_get_count_of_distinct_yes_answers_for_all_groups_returns_11_for_given_input():
    answers = ['abc', '', 'a', 'b', 'c', '', 'ab', 'ac', '', 'a', 'a', 'a', 'a', '', 'b']
    actual = get_count_of_distinct_yes_answers_for_all_groups(answers)
    assert actual == 11
