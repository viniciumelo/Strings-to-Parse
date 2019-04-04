from parse_string import word_appear_times


class ParseString:
    def __init__(self, sentence):
        self.sentence = sentence
    
    def parse(self):
        return word_appear_times(self.sentence)
