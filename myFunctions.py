def my_input_list(file_name) -> list[str]:
    """
    Reads all lines of a file and removes left and right white spaces
    :param file_name: Name of the file to be read
    :return: List with all lines from the read file
    """
    with open(file_name, 'r') as file:
        return list(map(str.strip, file.readlines()))


def my_input_string(file_name) -> str:
    """
    Reads a file and returns the string
    :param file_name: Name of the file to be read
    :return: File content as String
    """
    with open(file_name, 'r') as file:
        return file.read()
