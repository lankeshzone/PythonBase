class Outer:
    def __init__(self):
        self.inner = self.Inner()
        self.innerLevel = self.InnerLevel()
    def funouter(self):
        print("Iam outer function")
    def executeinner(self):
        self.inner.funinner()
        self.innerLevel.functioninnerLevel()

    # First Inner class
    class Inner:
        def __init__(self):
            self.innerTwo = self.InnerTwo()
        def funinner(self):
            print("Iam inner class function")
        def executeinnerTwo(self):
                self.innerTwo.funinnerTwo()

        #Secondlevel inner class
        class InnerTwo:
            def funinnerTwo(self):
                print("Iam inner two function")

    #Second inner class
    class InnerLevel:
        def __init__(self):
            self.x=100
        def functioninnerLevel(self):
            print("Inner Level")

outer = Outer()
outer.funouter()
outer.executeinner()
outer.inner.funinner()
outer.inner.executeinnerTwo()
outer.inner.innerTwo.funinnerTwo()

#inner = outer.Inner()
#inner.funinner()
#inner.executeinnerTwo()

#innerTwo = outer.inner.InnerTwo()
#innerTwo.funinnerTwo()