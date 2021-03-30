"""try:
    f1 = open("abc.txt", "a")
    f1.write("hiii")
    f2 = open("hellow", "a")
    for i in f1:
        f2.write(i)
    # =====================
    print(f1.mode)
    print(f1.close)
    print(f1.name)
except IOError:
    print("error")
    """
'''with open("abc", "a") as f:
    f.write("bhad me jao")
#automatically closes file with this syntax
'''
'''
with open("abc","r") as f1:
    data=f1.readlines()
    for line in data:
        word = line.split()
        print(word)
'''
'''
# copies daata from one file to another
#using with it takes care of automatically closing
with open("abc", 'r') as f1, open("hellow", "a") as f2:
    for line in f1:
        f2.write(line)
'''


class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.f1 = None

    def __enter__(self):
        self.f1 = open(self.filename, self.mode)
        return self.f1
