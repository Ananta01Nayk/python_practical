class init:
    def __init__(self,name,title):
        self.name = name
        self.title = title
    def out(self):
        print(f"hi { self.name} {self.title}")

obj = init("Ananta","Nayak")
obj.out()