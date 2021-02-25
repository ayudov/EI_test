"""
Модуль для работы с Артикулами
"""

from constants import LIST_OF_DF, code_elements_obligation
import itertools


def fill_gaps_in_mask(mask: str, words: list):
    """
    Заполнение недостающих параметров в маске
    :param mask: маска
    :param words: список слов наименования
    :return: артикул
    """
    mask_listed = mask.split('.')
    gap_idx = [i for i, n in enumerate(mask_listed) if n == '??']
    code_out = mask_listed

    for i, df in enumerate(LIST_OF_DF):
        if i in gap_idx:
            code_out[i] = find_code_el_by_word(words, i)

    return '.'.join(code_out)


def find_code_el_by_word(words: list, idx: int):
    """
    Нахождение елементе артикула по слову
    :param words: список слов
    :param idx: индекс недостающего элемента артикула
    :return: недостающий элемент артикула
    """
    df = LIST_OF_DF[idx]
    possible_combinations = []
    for i, j in itertools.combinations(range(len(words) + 1), 2):
        possible_combinations.append(words[i:j])

    for combination in possible_combinations:
        for column_name in df:
            col_list = df[column_name].tolist()
            # print(col_list)
            if ' '.join(combination) in col_list:
                return col_list[0]
    return '??'

    #
    # if idx == 0:
    #     return 'КК'
    # elif idx == 1:
    #     possible_combinations = []
    #     for i, j in itertools.combinations(range(len(words) + 1), 2):
    #         possible_combinations.append(words[i:j])
    #
    #     for combination in possible_combinations:
    #         if len(combination) <= 2:
    #             for column_name in df:
    #                 col_list = df[column_name].tolist()
    #                 if ' '.join(combination) in col_list:
    #                     return col_list[0]
    #     return '??'
    # elif idx > 2:
    #     for word in words:
    #         # print('word: ')
    #         # print(word)
    #         for column_name in df:
    #             # print(column_name)
    #             # print('---')
    #             col_list = df[column_name].tolist()
    #             # print(col_list)
    #             if word in col_list:
    #                 return col_list[0]
    #     return '??'
    # else:
    #     return '??'


def remove_gap(code, obligation=code_elements_obligation):
    """
    Удаление недостающих елементов артикула по шаблону обязательных элементов
    :param code: артикул
    :param obligation: Шаблон обязательных элементов артикула
    :return:
    """
    code_split = code.split('.')
    code_elements_obligation_split = obligation.split('.')

    out_code = []

    for a, b in zip(code_split, code_elements_obligation_split):
        if b == 'Ok':
            out_code.append(a)
        elif b == 'Ig' and a != '??':
            out_code.append(a)
        else:
            pass
    return '.'.join(out_code)
