"""
Модуль для работы с Масками
"""

from constants import MASKS


def generate_mask_of_sequence(sequence: str) -> str:
    """
    Создает маску из послежовательности
    :param sequence: послежовательность символов
    :return: маска
    """
    masks = MASKS
    located_codes = masks.loc[masks['Ключове слово'] == sequence]
    masks_list = located_codes['Маска'].tolist()

    if len(masks_list) > 1:
        separated_masks_list = []
        for mask in masks_list:
            separated_masks_list.append(mask.split('.'))

        out_mask = separated_masks_list[0]
        for mask_sec in separated_masks_list[1:]:
            tmp = []
            for (el_a, el_b) in zip(mask_sec, out_mask):

                if el_a != el_b:
                    tmp.append('??')
                elif el_a == el_b:
                    tmp.append(el_a)
            out_mask = tmp

        return '.'.join(out_mask)
    else:
        return '.'.join(masks_list)


def choose_mask(possible_masks: list) -> str:
    """
    Суммирует возможные маски
    :param possible_masks: список возможных масок
    :return: маску
    """
    if len(possible_masks) > 1:
        for i, mask in enumerate(possible_masks):
            possible_masks[i] = mask.split('.')

        out_mask = possible_masks[0]
        for mask_sec in possible_masks[1:]:
            tmp = []
            for (el_a, el_b) in zip(mask_sec, out_mask):
                if el_a != el_b:
                    if el_a == '??':
                        tmp.append(el_b)
                    elif el_b == '??':
                        tmp.append(el_a)
                elif el_a == el_b:
                    tmp.append(el_a)
            out_mask = tmp
        return '.'.join(out_mask)
    else:
        return '.'.join(possible_masks)

    pass


def all_masks_are_empty(masks: list):
    """
    Проверяет, все ли маски в списке пустые
    :param masks: Список масок
    :return: Boolean
    """
    counter = 0
    for elem in masks:
        if elem != '':
            pass
        elif elem == '':
            counter += 1
    if counter == len(masks):
        return True
    else:
        return False
