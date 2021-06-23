class Mobile:
    wireless=True                       #  GLOBAL ACCESS inside the class
    year=2020                           #  GLOBAL ACCESS inside the class

    def __init__(self, brandname, color, is_screentouch):
        self.bn=brandname
        self.col=color
        self.func=is_screentouch
def calling(self):
    print("is calling")
def camera_click(self):
    print("picture clicked")


m1=Mobile("Apple","white",True)
m2=Mobile("Samsung","blue",True)
# print(m1.bn)
# print(m1.scr)
# print(m2.bn)
print("m1-->",m1.year)
print("m2-->",m2.year)
print("m1-->",m1.wireless)
print("m2-->",m2.wireless)

m1.camera_