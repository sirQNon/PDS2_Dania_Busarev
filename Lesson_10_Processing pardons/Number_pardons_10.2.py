# Напишіть програму, яка б приймала список з числами та перевіряла чи все числа в ньому унікальні.
# Реалізуйте у функції декілька обробок виключень

list_number_unique = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_number_no_unique = [0, 1, 2, 3, 2, 2, 4, 5, 6546, 532, 54324, 32, 564362, 7, 7, 8, 45, 3, 1, 123, 654, 654, 654]


def check_unique(list_unique):
    try:
        new_list_check_set = set(list_unique)
        new_list_check_list = list(new_list_check_set)
        check_flag = new_list_check_list == list_unique
        if check_flag == True:
            return print(f"list_qnique")
        elif check_flag == False:
            raise Warning("list_no_unique")
    except Exception as ex:
        print(f" an unforeseen error {str(ex)} ")


check_unique(list_number_no_unique)
check_unique(list_number_unique)
