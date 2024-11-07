class Cat:
    name = None
    age = None 
    isHappy = None
    
cat1 = Cat()
cat1.name = "Barsik"
cat1.age = "3"
Cat.isHappy = True

cat2 = Cat()
cat2.name = "Murka"
cat2.age = "5"
cat2.isHappy = False

print(cat1.name)
print(cat2.name)