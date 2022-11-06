class TextProcessor:
    def init(self, text):
        self.text = str(text)
        self.signs = signs = "?!. \'\"`,:;-_/()[]~"

    def __is_punktiantian(self):
        for letter in self.text:
            if letter in self.signs:
                return True
        for letter in self.text:
            if letter is not self.signs:
                return False


    def get_clean_string(self, text):
        for test in self.signs:
            self.text = self.text.replace(test, '')
        return self.text

str_my = 'qwefdsfds!!r'
procc = TextProcessor(str_my)
ss = procc.get_clean_string()

class TextLoader:
    def init(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Clean string is: {}".format(self.__clean_string))
        return self.__clean_string

text_in_class = TextLoader(str_my)
text_in_class.clean_string