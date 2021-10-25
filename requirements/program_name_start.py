"""
print the program name when called
"""


class program_name:
    """
program name printing class
    """
    def __init__(self, name):
        self.name = name

    @staticmethod
    def equal_line():
        """
        :return:
        """
        print("|", end="")
        print("=" * 50, end="|\n")

    def _name_print_(self):
        spaces = (25-int((len(self.name)/2)))
        # print(spaces)
        if spaces <= 0:
            spaces = 0
        print(" "*spaces, end="")
        print(self.name)

    def __print__(self):
        self.equal_line()
        print("\n")
        self._name_print_()
        print("\n")
        self.equal_line()


if __name__ == "__main__":
    program_name("test").__print__()
