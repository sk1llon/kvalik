class MyDict:

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def get_dict(self, key):
        if key in self.dictionary:
            print(self.dictionary[key])
        else:
            print(0)


dct = {'a': 10, 'b': 20, 'c': 30}
my_dictionary = MyDict(dct)
my_dictionary.get_dict('d')
my_dictionary.get_dict('a')
