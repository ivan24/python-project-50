import json


def generate_diff(first_file_path, second_file_path):
    with open(first_file_path, 'r') as f1:
        unsorted_f1 = json.loads(f1.read())
        sorted_f1 = json.dumps(unsorted_f1)
        sorted_f1 = replace_char(sorted_f1)
        file1 = eval(sorted_f1)
    with open(second_file_path, 'r') as f2:
        unsorted_f2 = json.loads(f2.read())
        sorted_f2 = json.dumps(unsorted_f2)
        sorted_f2 = replace_char(sorted_f2)
        file2 = eval(sorted_f2)

    result_dict = {}
    for item in file1:
        if item not in file2:
            internal_dict = {'- ' + item: file1.get(item)}
            result_dict.update(internal_dict)

    for item in file2:
        if item not in file1:
            internal_dict = {'+ ' + item: file2.get(item)}
            result_dict.update(internal_dict)

    for item1 in file1:
        if item1 in file2:
            for item2 in file2:
                if item1 == item2 and file1[item1] != file2[item2]:
                    internal_dict1 = {'- ' + item1: file1.get(item1)}
                    internal_dict2 = {'+ ' + item2: file2.get(item2)}
                    result_dict.update(internal_dict1)
                    result_dict.update(internal_dict2)
                if item1 == item2 and file1[item1] == file2[item2]:
                    internal_dict = {'  ' + item1: file1.get(item1)}
                    result_dict.update(internal_dict)

    fin_str = json.dumps(result_dict)
    fin_str = fin_str.replace("\"", '')
    return fin_str


def replace_char(file):
    file = file.replace('true', "True")
    file = file.replace('false', "False")
    file = file.replace('none', "None")
    return file
