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
            return f" text corrected: {self.text} "
        elif self.__is_punktiantian() == False:
            return f" text in normal: {self.text} "


str_my = 'love!! my code ?1'


procc = TextProcessor(str_my)
ss = procc.get_clean_string()
print(ss)


class TextLoader:
    def __init__(self, text_2):
        self.text_2 = text_2
        self.__text_proccesor = TextProcessor
        self.__clean_string = None
        self.text_continue = None

    def set_clean_text(self):
        self.text_continue = self.__text_proccesor(self.text_2)
        self.__clean_string = self.__text_proccesor.get_clean_string(self.text_continue)
        self.clean_string

    @property
    def clean_string(self):
        return print(self.__clean_string)

str_my_2 = 'love!! my code !2'
call_class = TextLoader(str_my_2)
call_method = call_class.set_clean_text()



class Datainterface:
    def __init__(self, list_text):
        self.list_text = list_text
        self.__data = TextLoader
        self.text_wait = None
        self.text_to_loader = None
        self.convert = None

    def process_text(self):
        if isinstance(self.list_text, str):
            self.convert = self.list_text
        elif isinstance(self.list_text, list):
            self.convert = " ".join(self.list_text)
        self.text_wait = self.__data(self.convert)
        self.text_to_loader = self.__data.set_clean_text(self.text_wait)
        return self.text_wait

new_list_str = ["real call class!", "love code phyton!", "new work interesting!", "please leave your comment on the code ?"]
call_data_interface = Datainterface(new_list_str)
call_method_process = call_data_interface.process_text()