class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.signs = signs = "?!. \'\"`,:;-_/()[]~"

    def __is_punktiantian(self):
        for letter in self.text:
            if letter in self.signs:
                return True
        for letter in self.text:
            if letter is not self.signs:
                return False


    def get_clean_string(self):
        if self.__is_punktiantian() == True:
            for test in self.signs:
                self.text = self.text.replace(test, '')
            return f" text corrected {self.text} "
        elif self.__is_punktiantian() == False:
            return f" text in normal {self.text} "
str_my = 'qwefsfdsr'
procc = TextProcessor(str_my)
ss = procc.get_clean_string()
print(ss)