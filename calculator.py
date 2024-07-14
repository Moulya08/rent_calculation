def calculate_house_rent(rent,food,electricity_spent,persons):
    return total_bill

house_rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_spent = int(input("enter the total electricity spent = "))
charge_per_unit = int(input("enter the charge per unit = "))
persons = int(input("enter the number of persons living in room/flat = "))
total_bill = electricity_spent * charge_per_unit
output = (food + house_rent + total_bill) // persons
print("Each person will pay = ", output)