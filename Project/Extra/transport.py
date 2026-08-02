# a programme to show the total cost to travell some where in ring road
print("==============WELCOME TO NAPAL YATAYAT============")
name = input("Enter your name: ")
print("TOTAL LENGTH OF RING ROAD:27km")
print("TOTAL BUS STOPS=6(every 5km)")
print("Price per 5km:Rs 15")
print("Price per km:15/5 =Rs3")
print("Chose Where you want to travell")
print("1.kalanki-swambhu(distace-5km)")
print("2.kalanki-chabel(distance-10km)")
print("3.kalanki-bus park(distance-15km)")
print("4.kalanki-tinkune(distance-20km)")
print("5.kalaknki-air port(distance-25km)")
print("6.Kalanki-kalanki(distance-27)")
Bus_stops = {
    1:("Kalanki-swambhu",15),
    2:("Kalanki-chabel",30),
    3:("Kalanki-bus park",45),
    4:("Kalanki-tinkune",60),
    5:("Kalanki-air port",75),
    6:("Kalainki-kalanki",85)
}
stop = int(input('Enter your bus stop: '))
if stop in Bus_stops:
    pass
else:
    print("SORRY,We don't provide the service")
identification ={
    1:("Student"),
    2:("Other")
}
print("Identify yourself")
print("1.STUDENT")
print("2.OTHER")
identity = int(input("Enter your identification: "))
if identity in identification:
    pass
else:
    print("Invalid identity")
Location , COST =Bus_stops[stop]
cost = COST-40/100*COST
if identity==1:
    print("==============BILL============")
    print(f"Customer's Name: {name}")
    print(f"Location: {Location}")
    print(f"Total Cost: {cost}")

else:
    print("==============BILL============")
    print(f"Customer's Name: {name}")
    print(f"Location: {Location}")
    print(f"TOTAL COST: {COST}")
print('         THANKS FOR VISITING               ' )