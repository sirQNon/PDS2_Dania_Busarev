class TextProcessor:
    def __init__(self, text):
        self.text = text
        self.signs = signs = "?!.\'\"`,:;-_/()[]~"

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


str_my = 'love!! my code'
procc = TextProcessor(str_my)
ss = procc.get_clean_string()
print(ss)

class TextLoader:
    def __init__(self):
        self.__text_proccesor = TextProcessor
        self.__clean_string = None
        self.text_continue = None

    def set_clean_text(self, text_2):
        self.text_continue = self.__text_proccesor(text_2)
        self.__clean_string = self.__text_proccesor.get_clean_string(self.text_continue)
        self.clean_string

    @property
    def clean_string(self):
        return print(self.__clean_string)


call_class = TextLoader()
call_method = call_class.set_clean_text(str_my)


