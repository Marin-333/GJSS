class pet:
    def _init_(self, name, age):
        self.name = name
        self.age = age

        print(f"Bienvenido al mundo de las mascotas {self.name}!")

    def description(self):
        print(f"Mi nombre es {self.name} y tengo {self.age} años.")

    def eat(self, food):
        print(f"{self.name} está comiendo {food}.")

    def sleep(self):
        print(f"{self.name} está durmiendo.")

    def walk(self):
        print(f"{self.name} Da un pasito.")


class Dog(pet):
    def _init_(self, name, age, breed):
        super()._init_(name, age)
        self.breed = breed
        
    def bark(self):
        print(f"{self.name} Un guau.")

    def eat(self, food):
        print(f"{self.name} está comiendo {food} como un perro.")

    def _str_(self):
        return f"Perro: {self.name}, Edad: {self.age}, Raza: {self.breed}"
    
    

firulays = Dog("Firulays", 3, "Labrador")
Galileo = pet("Gato", 2)

firulays.eat("Croquetas")
Galileo.eat("Pescado")

print(firulays)
print(Galileo)