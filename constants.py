"""
Модуль с постоянными
"""

import pandas as pd


# def get_test_sheet():
#     """
#     Получение листа с тестовыми заданиями
#     :return: DataFrame
#     """
#     # print('loaded test sheet')
#     return pd.read_excel(r'C:\Users\yudov\Documents\Energo_invest\АВТ.xlsx', sheet_name='Test_sheet', dtype=str)


def get_masks() -> pd.DataFrame:
    """
    Получение листа с масками
    :return: DataFrame
    """
    # print('loaded masks')
    return pd.read_excel(r'C:\Users\yudov\Documents\Energo_invest\КК.xlsx', sheet_name='КК_Маска', dtype=str)


def get_KK() -> pd.DataFrame:
    """
    Получение листа КК
    :return: DataFrame
    """
    # print('loaded KK')
    return pd.read_excel(r'C:\Users\yudov\Documents\Energo_invest\КК.xlsx', sheet_name='КК', dtype=str)


def get_list_of_df(dataframe: pd.DataFrame) -> list:
    """
    Получение Датафреймов из КК
    :param dataframe: Общий DataFrame KK
    :return: Список из Датафреймов
    """

    #1
    df_list = []
    df = dataframe
    df_list.append(df[["Кран кульовий"]].dropna(how='all'))
    df_list.append(df.iloc[0:, 1:13].dropna(how='all'))
    df_list.append(df.iloc[0:, 13:18].dropna(how='all'))
    df_list.append(df.iloc[0:, 18:22].dropna(how='all'))
    df_list.append(df.iloc[0:, 22:26].dropna(how='all'))
    df_list.append(df.iloc[0:, 26:60].dropna(how='all'))
    df_list.append(df.iloc[0:, 60:69].dropna(how='all'))
    df_list.append(df.iloc[0:, 69:83].dropna(how='all'))
    df_list.append(df.iloc[0:, 83:85].dropna(how='all'))
    df_list.append(df[["Середовище тільки: газ"]].dropna(how='all'))
    df_list.append(df.iloc[0:, 86:89].dropna(how='all'))
    df_list.append(df.iloc[0:, 89:92].dropna(how='all'))
    df_list.append(df.iloc[0:, 92:136].dropna(how='all'))

    # 2
    # df_list = []
    # df = dataframe
    # df_list.append(df[["Автоматичний вимикач"]].dropna(how='all'))
    # df_list.append(df.iloc[0:, 1:26].dropna(how='all'))
    # df_list.append(df.iloc[0:, 26:30].dropna(how='all'))
    # df_list.append(df.iloc[0:, 30:44].dropna(how='all'))
    # df_list.append(df.iloc[0:, 44:48].dropna(how='all'))
    # df_list.append(df.iloc[0:, 48:50].dropna(how='all'))

    return df_list

# 1
code_elements_obligation = 'Ok.Ok.Ok.Ok.Ok.Ok.Ok.Ig.Ig.Ig.Ig.Ig.Ig'

#2
# code_elements_obligation = 'Ok.Ok.Ok.Ok.Ok.Ig'

code_elements_obligation_list = code_elements_obligation.split('.')

# TEST_SHEET = get_test_sheet()
MASKS = get_masks()
KK = get_KK()
LIST_OF_DF = get_list_of_df(KK)
N = 13
