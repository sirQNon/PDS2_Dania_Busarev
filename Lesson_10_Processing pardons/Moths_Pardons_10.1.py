# напишіть функцію, яка б приймала номер місяця, а вертала його назву.
# Реалізуйте у функціЇ декілька обробок виключень

def months(number):
    if number < 1 or number > 12:
        raise ValueError(f"спасибо за придуманый месяц {number} , мы расмотрим ваш вариант, а пока введите пожалуйста месяц 1-12")
    try:
        months_number = {"Janury": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
                         "August": 8,
                         "September": 9, "October": 10, "November": 11, "December": 12}
        for k, v in months_number.items():
            if v == number:
                return f" Moth: {k}"
    except Exception as ex:
        return ex


number_moth = int(input(" please enter number moth - "))
print(months(number_moth))
