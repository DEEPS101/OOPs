class Mobile:
    pass
    def __init__(self):
        self.brandname="Samsung"
        self.color="Black"

    def calling(self):
        return("calliiuyuhguguoygpigng")

    def cameraclick(self):
        print("picture is clicked")


#def main():
m1=Mobile()
m2=Mobile()

print(m2.calling())

print("m1 has the brandname -->",m1.brandname)
print("m2 with brandname -->",m2.brandname)
# if __name__ == '__main__':
    # main()


print("-------------------------------------------------\n---------------------------------------")


class Mobile:
    def __init__(self):
        self.brandname="Samsung"
        self.color="Black"

    def calling(self):
        print(self.color + "color" , self.brandname , "is ringing"+" loudly")

    def cameraclick(self):
        print("picture is clicked")


def main():
    m1=Mobile()
    m2=Mobile()
    print(m1.brandname)
    m1.calling()
    m1.cameraclick()

if __name__ == '__main__':
    main()


