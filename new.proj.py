class Cat:
    name = None
    age = None 
    isHappy = None
    
    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy 

    def get_data(self):
        print(self.name, "age :", self.age, "isHappy :", self.isHappy)

cat1 = Cat()
cat1.set_data("Barsik", 3, True)

cat2 = Cat()
cat2.set_data("Any", 5 , False)

cat1.get_data()
cat2.get_data()
print("Thats all")
print("08/11/24")
print("yyy")
print("14.08.24")
print("Rezyx")