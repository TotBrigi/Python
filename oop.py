class Person(object):
    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name =last_name
        self.phone_number = phone_number


    def get_full_name(self):
        return self.first_name + " " + self.last_name
    def get_phone_number(self):
        return self.phone_number
    def set_phone_number(self, new_number):
        self.phone_number = new_number


class Child(Person):
    def __init__(self, first_name, last_name, phone_number,toy):
        Person.__init__(self,first_name,last_name, phone_number)
        self.toy = toy

john = Child(first_name="John", last_name="Doe", phone_number=123, toy="train")
judy = Person(first_name="John", last_name="Doe", phone_number=123)

print john.toy
print john.get_full_name()
print judy.get_full_name()
