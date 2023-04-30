from gendiff.gendiff_tools import get_dct_from_file
from gendiff.gendiff_tools import create_lst_of_keys
from gendiff.output_diff_stylich import create_string_of_diff_stylish


def identify_change_of_line(key, dct1, dct2):
    if dct1.get(key) == dct2.get(key):
        return 'equal'

    elif key in dct1 and key in dct2:
        if isinstance(dct1[key], dict) and not isinstance(dct2[key], dict):
            return 'changed'
        elif isinstance(dct1[key], dict):
            return 'equal'
        else:
            return 'changed'

    elif key in dct1:
        return 'removed'

    else:
        return 'added'


def create_lst_of_keys_stylish(dct1, dct2):
    lst_of_diff_stylish = create_lst_of_keys(dct1, dct2)

    for index, key in enumerate(lst_of_diff_stylish):
        lst_of_diff_stylish[index] = [
            key,
            identify_change_of_line(key, dct1, dct2)
        ]
        if isinstance(dct1.get(key), dict) and isinstance(dct2.get(key), dict):
            lst_of_diff_stylish[index].append(
                create_lst_of_keys_stylish(dct1[key], dct2[key])
            )
        elif isinstance(dct1.get(key), dict):
            lst_of_diff_stylish[index].append(
                create_lst_of_keys_stylish(dct1[key], dct1[key])
            )
        elif isinstance(dct2.get(key), dict):
            lst_of_diff_stylish[index].append(
                create_lst_of_keys_stylish(dct2[key], dct2[key])
            )

    return lst_of_diff_stylish


def generate_gendiff(file1, file2):
    dct_from_file1 = get_dct_from_file(file1)
    dct_from_file2 = get_dct_from_file(file2)

    lst_of_diff = create_lst_of_keys_stylish(dct_from_file1, dct_from_file2)

    result_string = create_string_of_diff_stylish(
        dct_from_file1, dct_from_file2, lst_of_diff
    )

    return result_string

#
# generate_gendiff(
#     '../for_developer/file1.json', '../for_developer/file2.json')
