"""
Тока входа
"""
import masks
import itertools
# import constants
import codes
import re
from datetime import datetime

start = datetime.now()
# print(datetime.now())
'''
name - Наименования для распознавания
'''
# test_sheet = constants.get_test_sheet()
# names = test_sheet['Наименование']
# names_list = names.tolist()
# name = names_list[0]

# name = 'Тип 670, приварка, н/ж сталь, Tmax=180°C DN20'
name = 'Фланцевий сталевий кульовий кран серії "Silver" 11с42п з редуктором DN150/150 PN16 T180С'
print('Name: ' + name)

'''
Удаление лишних символов
'''
name = re.sub(r'[@\'?$%_()"]', "", name, flags=re.I)


'''
Раздление Наименования по 'пробел'
'''
name_split = name.split(' ')
print('Name split: ' + str(name_split))


'''
Выделение возможных словосочетаний из наименования
'''
possible_combinations = []
for i, j in itertools.combinations(range(len(name_split) + 1), 2):
    possible_combinations.append(name_split[i:j])


'''
Создание возможных масок из всех комбинаций наименования
'''
possible_masks = []
for i in possible_combinations:
    possible_masks.append(masks.generate_mask_of_sequence(' '.join(i)))


'''
Проверка. пустые ли се варианты масок
'''
if masks.all_masks_are_empty(possible_masks):
    #1
    possible_masks = ['??.??.??.??.??.??.??.??.??.??.??.??.??']

    #2
    # possible_masks = ['??.??.??.??.??.??']


'''
Удаление пустых вариантов масок
'''
possible_masks = list(filter(None, possible_masks))

'''
Сложение масок
'''
mask = masks.choose_mask(possible_masks)
print('Mask: ' + mask)

'''
Заполнение пустых элементов артикула
'''
code = codes.fill_gaps_in_mask(mask, name_split)
print('Code: ' + code)

'''
Удаление оставшихся пустых элементов артикула по шаблону:
code_elements_obligation = 'Ok.Ok.Ok.Ok.Ok.Ok.Ok.Ig.Ig.Ig.Ig.Ig.Ig'
'''
final_code = codes.remove_gap(code)
print('Final code: ' + final_code)


finish = datetime.now()
print(finish - start)
