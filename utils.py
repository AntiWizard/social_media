import os.path


def check_valid_name(value):
    if not any(char.isdigit() for char in value) and value == value.strip():
        return value
    else:
        raise TypeError("value invalid")


def check_valid_email(value):
    if "@" in value and "." in value and not value[0].isdigit() and value == value.strip():
        return value
    else:
        raise TypeError("email invalid")


def search_record(file_name, record):  # exist -> return record | not exist -> return False
    if os.path.isfile("{}.txt".format(file_name)):
        with open("{}.txt".format(file_name), 'r') as file:
            file.readline()
            next_line = file.readline()
            while next_line != "":
                if record in next_line.split(",")[:3]:
                    return next_line.strip().split(",")
                next_line = file.readline()
        return False
    raise TypeError("{} dose not existed".format(file_name))


def search_all_record(file_name, record):  # exist -> return record | not exist -> return False
    if os.path.isfile("{}.txt".format(file_name)):
        result = []
        with open("{}.txt".format(file_name), 'r') as file:
            file.readline()
            next_line = file.readline()
            while next_line != "":
                if record in next_line.split(",")[:3]:
                    result.append(next_line.strip().split(","))
                next_line = file.readline()
        return result if result else False
    raise TypeError("{} dose not existed".format(file_name))


def file_exist(file_name):
    if not os.path.isfile("{}.txt".format(file_name)):
        raise FileExistsError("file dose not exist")


def file_not_exist(file_name):
    if os.path.isfile("{}.txt".format(file_name)):
        raise FileExistsError("file dose was existed")
