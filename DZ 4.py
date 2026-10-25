class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Тварина видає звук.")

    def show_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Вік: {self.age} років")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("Гав-гав!")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Няв-няв!")


dog = Dog("Бобік", 3, "Вівчарка")
cat = Cat("Мурчик", 2, "Рудий")

print("=== СОБАКА ===")
dog.show_info()
print(f"Порода: {dog.breed}")
dog.speak()

print("\n=== КІТ ===")
cat.show_info()
print(f"Колір: {cat.color}")
cat.speak()