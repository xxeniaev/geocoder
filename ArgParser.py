import sys


class ArgParser:
    def __init__(self):
        super().__init__()
        self.input = sys.argv
        del self.input[0]
