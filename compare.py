class ESGT:
    def __init__(self):

        self.name = "Mr Adefamoye"
        self.age = 27
    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False



N1 = ESGT()
N2 = ESGT()
N1.age = 64
N2.name = "Engr Solomon"

if N1.compare(N2):
    print("They are the same")
else:
    print("There are different")
print(N1.name, N1.age, N2.name, N2.age)

