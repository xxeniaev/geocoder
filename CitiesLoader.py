import codecs


class CitiesLoader:
    """Загружает список городов для парсинга адреса"""
    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name

    def load(self):
        try:
            with open(self._file_name) as f:
                contents = codecs.decode(codecs.encode(f.read(), 'cp1251'), 'utf8')
        except TypeError:
            print('please, choose language or file for creating '
                  'your own dictionary')
            exit(1)
        dictionary = set()
        dictionary.update(contents.split())

        return dictionary
