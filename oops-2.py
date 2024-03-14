class PhoneDirectory:
  def __init__(self, name, age, address, phone_number, occupation):
    self.name = name
    self.age = age
    self.address = address
    self.phone_number = phone_number
    self.occupation = occupation

  def __str__(self):
     
    return f"{self.name}: {self.phone_number}"

def find_by_name(phone_directory_list, name):
    
    return list(filter(lambda obj: obj.name == name, phone_directory_list))

person1 = PhoneDirectory("Prasanna", 23, "619 Patterson St", "901-632-3178", "Student")
person2 = PhoneDirectory("Hari priya", 25, "619 Patterson St", "901-234-7645", "Doctor")
person3 = PhoneDirectory("Sai teja", 24, "635 Patterson St", "901-756-2323", "Engineer")

print(person1)

phone_directory = [person1, person2, person3]
person_list = find_by_name(phone_directory, "Sai teja")

for person in person_list:
    print(person)
    
