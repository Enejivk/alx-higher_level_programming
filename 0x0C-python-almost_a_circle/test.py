class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def update(self, list_data):
        if len(list_data) >= 2:
            self.first_name = list_data[0]
            self.last_name = list_data[1]
            print("_______________")
            print(self.last_name)
            print("_______________")
    
student = Student("victor", "Eneji", 25)
list_data = ("peter", "david", 23)
print(student.__dict__)
student.update(list_data)

