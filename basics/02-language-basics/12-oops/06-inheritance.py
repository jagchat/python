class NameInfo:
    def __init__(self, n):
        self.name = n

class CompanyInfo(NameInfo):
    def __init__(self, name, ein):
        NameInfo.__init__(self, name)
        self.EIN = ein

    def print(self):
        print(f"Name={self.name}, EIN={self.EIN}")

o1 = CompanyInfo("Jag LLC", "A12345")
o1.print()