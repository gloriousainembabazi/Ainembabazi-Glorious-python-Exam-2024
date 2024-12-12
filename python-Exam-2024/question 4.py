#question 4(i)(a)



#(b)
#A class is the group of object while object are the items in class

#question 4(ii)
python_exam= {"python 1":'24',"python 2":20,"pthon 3":"80" }
for key,value in python_exam ():  
   print(key,value)




#question 4(iv)

class Car:
     def __init__(self, brand, color):
         self.brand = brand
         self.color = color 

car = Car("Toyota", "Red")
print(car.brand)
print(car.color)


#question 4(v)

class Car:
     def __init__(self, brand, color):
         self.brand = brand
         self.color = color

     def start_engine(self):
         print(f"The engine of the {self.brand} has started!") # completed

car = Car("Toyota", "Red")
car.start_engine()