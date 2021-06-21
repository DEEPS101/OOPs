class Mobile:
    def __init__(self,brandname,color,is_screentouch):
        self.bn=brandname
        self.col=color
        self.func=is_screentouch

    def calling(self):
        print("is calling")
    def camera_click(self):
        print("picture clicked")


m1=Mobile("Apple","white",True)
m2=Mobile("Samsung","blue",False)

print(m1.bn)
print(m1.func)
print(m2.col)
print(m2.bn)
m2.calling()
m1.camera_click()
print(m2.func)