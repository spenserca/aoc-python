def get_input_lines(file_name: str):
    return open("./input/{0}.txt".format(file_name)).read().splitlines()
