class Contact(object):
    def __init__(self,first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
    def __str__(self):
        return self.last_name + " " + self.last_name +": " + self.phone_number

    def set_first_name(self,new_first_name):
        self.first_name = new_first_name

    def set_last_name(self, new_last_name):
        self.last_name=new_last_name

    def set_phone_number(self, new_number):
        self.phone_number = new_number

phone_book= []

john = Contact("John", "Done", "23456778")
katie = Contact("katie", "Black", "787986")
caesar = Contact("Caesar", "White", "98979896")

katie.set_phone_number("67868767")

phone_book.append(john)
phone_book.append(katie)
phone_book.append(caesar)

for Contact in phone_book:
   print Contact

phone_book.remove(john)
print " "
for Contact in phone_book:
   print Contact