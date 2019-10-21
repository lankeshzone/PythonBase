class laptop:
    comp = "lenovo" # static variable
    def __init__(self,prodID, ProdName, Ram, OS, Apps ): #constructor
        self.prodName = ProdName # non-static or instance variabless
        self.Ram = Ram
        self.OS = OS
        self.Apps = Apps
        self.hd = 200
        print("All values for objects have been initialized \n")

    def fun1(self): # method
        x = 100 # local variable with in function
        self.Apps = 200

# two objects of class laptops are created with initializing values
lenovo = laptop("Yog123","Lenovo Yoga Series", 16, "Win-10 ","Office")
hp = laptop("hp123","pavilion Desk",32, "Linux","nill")

lenovo.fun
print(laptop.comp)
print(lenovo.prodName)
print(hp.prodName)