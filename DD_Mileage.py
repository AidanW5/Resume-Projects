'''
Enter miles driven for the year and get total mileage
'''

import os

#read miles stored in text document
with open("DD_Storage.txt", "r") as f:
    stored_miles = f.read()
    

#convert string to int and print
stored_miles = int(stored_miles)

print(f"The total miles for this year is {stored_miles}")

#user imput to choose path
mileage = input("If you would like to find the difference in mileage press '1', if you would like to add miles to the total press '2': ")

#create empty list
mile_list = []

#if-else to add miles to list
if mileage == "2":
    add_mile = int(input("Add mile: "))
    if add_mile > 0:
        mile_list.append(add_mile)
    

elif mileage == "1":
    print("\nType 0 when finished\n")
    while True:
        mile_1 = int(input("Enter larger mile: "))
        if mile_1 == 0:
            break
        mile_2 = int(input("Enter smaller mile: "))
        

        if mile_1 > mile_2:
            mile_difference = mile_1 - mile_2
            mile_list.append(mile_difference)
            
        else:
            print("Enter larger mile first")
            

else:
    print("Press '1' for total miles or press '2' to add on")
    
#add mile list
mile_total = sum(mile_list)

#get final mileage
final_mileage = mile_total + stored_miles

#change final_mileage to str type
final_mileage = str(final_mileage)

#write final_milage in txt doc
with open("DD_Storage.txt", "w") as f:
    f.write(final_mileage)

#print final mileage
print(f"Your total mileage is {final_mileage} miles")