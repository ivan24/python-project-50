import json


def generate_diff(first_file_path, second_file_path):
    with open(first_file_path, 'r') as f1:
        file1 = json.loads(f1.read())
    with open(second_file_path, 'r') as f2:
        file2 = json.loads(f2.read())

    sorted_keys = sorted(
        list(set(file1.keys()).union(set(file2.keys())))
    )
    result_dict = {}
    add_key = ' + '
    minus_key = ' - '
    not_key = "  "

    for i in sorted_keys:
        if i in file1 and i not in file2:
            result_dict.update({minus_key + i: file1[i]})
        if (i in file1 and i in file2) and (file1[i] != file2[i]):
            result_dict.update({minus_key + i: file1[i]})
            result_dict.update({add_key + i: file2[i]})
        if (i in file1 and i in file2) and (file1[i] == file2[i]):
            result_dict.update({'   ' + i: file1[i]})
        if i in file2 and i not in file1:
            result_dict.update({' + ' + i: file2[i]})

    dict_to_str = json.dumps(result_dict)
    dict_to_str = replace_char(dict_to_str)
    dict_to_str = dict_to_str.replace("\"", "")
    dict_to_str = dict_to_str.replace(",", "\n")
    dict_to_str = dict_to_str.replace ("{", "{\n ")
    dict_to_str = dict_to_str.replace ("}", "\n}")
    return dict_to_str


def replace_char(str_dict):
    str_dict = str_dict.replace('True', "true")
    str_dict = str_dict.replace('False', "false")
    str_dict = str_dict.replace('None', "none")
    return str_dict
