class House:
    
    houses_history = []
    def __new__(cls, *args, **kwargs):
        if args:
            cls.houses_history.append(args[0])
        return super().__new__(cls)
    
    
    def __init__(self,name,number_of_floors):
        self.name = str(name)
        self.number_of_floors = int(number_of_floors)    
        
    def go_to(self,new_floor):
        if new_floor < self.number_of_floors and new_floor > 1:
            for i in range(new_floor):
                print(i + 1)
        else:
            print("Такого этажа не существует")   
                     
    def __len__(self):
        return  self.number_of_floors  
    
    def  __str__(self):
        return f"Название: {self.name}, кол-во этажей:{self.number_of_floors}"
    
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    
    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        
    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
    
    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors   
           
    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors    
     
    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors   
        
    def __add__(self,value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self 
         
    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")          
      
        
        
h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)