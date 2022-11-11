#Напишіть клас Parallelogram, який приймає два аргументи width та length та метод get_area, який вираховує площу паралелограму.
#Успадкуйте від нього клас Square,перевизначіть в ньому метод get_area таким чином, щоб він вираховував площу квадрата

class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.result = None

    def get_area(self):
        self.result = self.width * self.length
        return self.result


class Square(Parallelogram):
    def __init__(self, width):
        super().__init__(width, length=width)
    def get_area(self):
       super().get_area()
       result_square = self.length **2
       return f" area square: {result_square}"

input_width = int(input("введите ширину"))
input_lenght = int(input("введите длину"))
object_in_class_parallelogram = Parallelogram(input_width,input_lenght)
call_method_class_parallelogram = object_in_class_parallelogram.get_area()
print(f" area Parallelogram: {call_method_class_parallelogram} ")


object_in_class_Square = Square(input_lenght)
call_method_class_Square = object_in_class_Square.get_area()
print(call_method_class_Square)