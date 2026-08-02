
# product_list=[
#     {
#         "product_id": 1,
#         "product_name": "Laptop",
#         "price": 50000,
#         "quantity": 10
#     },
#     {
#         "product_id": 2,
#         "product_name": "Mobile",
#         "price": 20000,
#         "quantity": 20
#     },
#     {
#         "product_id": 3,
#         "product_name": "Tablet",
#         "price": 15000,
#         "quantity": 15
#     }
# ]
# print("==============================Welcome Too E-commerce Store===============================")
# print("Chose option")
# print("1.View Product")
# print("Buy Product")
# print("3.Exit")

# choice=int(input("Enter choice: "))
# purchases=[]
# if choice==1:
#     print("\n Available Products")
#     print("-"*50)
#     for product in product_list:
#         print("ID",product["product_id"],
#         "| Name ",product["product_name"],
#         "| Price ",product["price"],
#         "| Quantity ",product["quantity"])
#     print("-"*50)

# elif choice==2:
#     print("\n Available Products")
#     print("-"*50)
#     for product in product_list:
#         print("ID",product["product_id"],
#         "| Name ",product["product_name"],
#         "| Price ",product["price"],
#         "| Quantity ",product["quantity"])
#     print("-"*50)
   

#     num_items=int(input("Enter how many types of product you want to purchase(1-3): "))
#     total=0
#     for i in range(num_items):
#         pid=int(input("Enter pid(1-3): "))
#         qty=int(input("Enter quantity: "))
#         for product in  product_list:
#             if product["product_id"]==pid:
#                 pass

#                 if product["quantity"]>=qty:
#                     total_price=product["price"]*qty
#                     total+=total_price
#                     purchases.append({
#                         "Name":product["product_name"],
#                         "Price":product["price"],
#                         "Quantity":product["quantity"],
#                         "total":total_price
#                     })    
#                     print(f"YOU purchased {qty} {product['product_name']} for {total}")          
#                 else:
#                     print("Enough stok not available")
#                 break
#         else:
#             print("Invalid Product")

# elif choice==3:
#     print("Thanks For Vistiing")

# else:
#     print("Sorry We Don't provide The Service")

# # same using function 
# product_list=[
#     {
#         "product_id": 1,
#         "product_name": "Laptop",
#         "price": 50000,
#         "quantity": 10
#     },
#     {
#         "product_id": 2,
#         "product_name": "Mobile",
#         "price": 20000,
#         "quantity": 20
#     },
#     {
#         "product_id": 3,
#         "product_name": "Tablet",
#         "price": 15000,
#         "quantity": 15
#     }
# ]
# purchase=[]
# # To display products 
# def display_product():
#     print("\n Available Products ")
#     print("-"*50)
#     for product in product_list:
#         print("ID",product["product_id"],
#               "| Name ",product["product_name"],
#               "| price",product["price"],
#               "| Stock",product["quantity"])
#     print("-"*50)

# # To buy product
# def buy_product():
#     total=0
#     num_item = int(input("Enter how many different types of product you want to purchase: "))

#     for i in range(num_item):
#         pid = int(input("Enter pid of prefered product: "))
#         qty = int(input("Enter quantity :"))
#         for product in product_list:
#             if pid ==product["product_id"]:
#                 pass
#                 if qty <=product["quantity"]:
#                     total_price = product["price"]*qty
#                     total+=total_price
#                     print(f"You bought {qty} {product["product_name"]} for {total_price}")
#                     purchase.append({
#                         "Name":product["product_name"],
#                         "Price":product["price"],
#                         "Quantity":qty,
#                         "total_price":total_price,
#                         "total":total
#                     })
                  
#                 else:
#                     print("Enough stok not availble ")
#                 break
#             else:
#                 print("Enter Valid pid ")

# # To exit 
# def exit():
#     print("Thanks for visiting ")

# # Main Loop
# print("\n Chose a option")
# print("1.View product")
# print("2.Buy Product")
# print("3.Exit")

# choice = int(input("Enter a choice: "))

# if choice==1:
#     display_product()

# elif choice ==2:
#     display_product()
#     buy_product()

# elif choice==3:
#     exit()

# else:
#     print("We don't provide the service")

# if purchase:
#     print("========================================Bill=============================================")
#     print("Name \t Price \t Quantity \t Total")
#     print("-"*60)
#     for item in purchase:
#         print(f"{item["Name"]} \t{item["Price"]} \t {item["Quantity"]} \t      {item["total_price"]}")
#         print("-"*60)

#     print(f"Grand Total :                                       {item["total"]}")


invoice=open("data.txt","a")
name = input("Enter your name: ")
print("Chose a laptop")
print("DEll,(Rs50000)")
print("HP,(Rs 6000)")
print("LENEVO,Rs70000")
print("MACBOOK,Rs80000")
laptops = {
    "DELL":50000,
    'HP':60000,
    "LENEVO":70000,
    "MACBOOK":80000,
}
PRODUCT = input("Enter product you want to purchase: ")
if PRODUCT in  laptops:
    quantity = int(input("Enter the quantity: "))
    print("Chose delivery option")
    print("1.Home(Rs1000)")
    print("2.Pick Up(Rs0)")
    delivery_option = {
        1:("Home",1000),
        2:("PICK UP",0)
    }
    delivery_choice =int(input("Enter delivery option: "))
    if delivery_choice in delivery_option: 
        pass
    else:
        print("Invalid choiçe")
    packing_option={
        1:("Box",1000),
        2:("Paper Bag",10)
    }
    print("Chose a packing option")
    print("1.Box(Rs1000)")
    print("2.Paper Bag(Rs 0)")
    packing_choice =int(input("Enter your packing choice: "))
    if packing_choice in packing_option:
        pass
    else:
        print("Ivalaid packing choice")
    Location_option = {
        1:("KATHMANDU"),
        2:("BHAKTAPUR"),
        3:("LALITPUR")
    }
    print("Chose your location")
    print("1.KATHMANDU")
    print("2.BHAKTAPUR")
    print("3.LALITPUR")
    location_choice = int(input("Énter your location: "))
    if location_choice in Location_option:
        pass
    else:
        print("SORRY,We Don't ship in your Location")
   
else:
    print("SORRY,PRODUCT NOT ANAILABLE")
laptops_cost = laptops[PRODUCT]
delivery_name,delivery_cost = delivery_option[delivery_choice]
packing_name ,packing_cost = packing_option[packing_choice]
location = Location_option[location_choice]
total = laptops_cost*quantity+delivery_cost+packing_cost
VAT = 13/100*total
Grand_Total = total+VAT

(print("==================================WELCOME TO ABC ELECTRONICS SHOWROOM============================="))
(print("............................................BILL..................................................."))
(print(f"Customer's Name: {name}"))
(print(f"Purchased Product: {PRODUCT}"))
(print(f"Price per unit: {laptops[PRODUCT]}"))
print(f"Purchased Quantity: {quantity}")
(print(f"Delivery: {delivery_name}"))
(print(f"Delivery Cost: {delivery_cost}"))
(print(f"Packing: {packing_name}"))
(print(f"Packing cost: {packing_cost}"))
(print(f"Location : {location}"))
(print(f"Total : {total}"))
print(f"VAT: {VAT}")
(f"Grand Total: {Grand_Total}")
(print("                                  Thanks For Visiting                            ") )



invoice.write(f"Name:{name}\n,Purchased product:{PRODUCT},\nPrice per unit: {laptops[PRODUCT]},\nPurchased Quantity: {quantity},/nDelivery: {delivery_name},\nDelivery Cost: {delivery_cost},\nPacking: {packing_name}Packing cost: {packing_cost},\nLocation : {location},\nTotal : {total},\nVAT: {VAT},\nGrand Total: {Grand_Total}\n")
invoice.close()