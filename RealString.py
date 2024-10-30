class RealString:
    def __init__(self, content):
        self.content = content

    def __len__(self):
        return len(self.content)

    def __gt__(self, other):

        if isinstance(other, RealString):
            return len(self.content) > len(other.content)
        elif isinstance(other, str):
            return len(self.content) > len(other)
        return NotImplemented

str1 = RealString("Apple")
str2 = RealString("Яблоко")

print(str1 < str2)

