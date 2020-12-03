def get_lines_from_file(file_name: str):
    return open("./input/{0}.txt".format(file_name)).read().splitlines()
