class TextProcessor():
    def __init__(self, text):
        self.text = str(text)
        self.signs = signs = "?!. \'\"`,:;-_/()[]~"

    def __is_punktiantian(self):
        for letter in self.text:
            if letter in self.signs:
                return True
        for letter in self.text:
            if letter is not self.signs:
                return False


    def get_clean_string(self):
        for test in self.signs:
            self.text = self.text.replace(test, '')
        return self.text

str_my = 'qwefdsfds!!r'
procc = TextProcessor(str_my)
ss = procc.get_clean_string
print(ss)

