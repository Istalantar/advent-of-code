def my_input(file_name):
    """
    Reads all lines of a file and removes left and right white spaces
    :param file_name: Name of the file to be read
    :return: List with all lines from the read file
    """
    with open(file_name, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    return lines
