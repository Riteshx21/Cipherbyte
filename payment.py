p1_name,p1_price = "T-shirt",350.40
p2_name,p2_price = "Pant",600.30
p3_name,p3_price = "Jogger",770.20
p4_name,p4_price = "Shirt",400.0
p5_name,p5_price = "Jeans pant",1000.50

shop_name = "Sai Shopping Mall"
shop_address = "Sardar Chauk,"
shop_city = "Nashik"
pin_code = "422001"

Message = "Thanks for coming , visit again!!"

print("\t\tRECEIPT")
print("*"*50)

print("\t\t{}".format(shop_name.title()))
print("\t\t{}".format(shop_address))
print("\t\t{}".format(shop_city))
print("\t\t{}".format(pin_code))

print("*"*50)

print("\t Product Name \t Product Price")

print("\t{}\t\t${}".format(p1_name.title(),p1_price))
print("\t{}\t\t${}".format(p2_name.title(),p2_price))
print("\t{}\t\t${}".format(p3_name.title(),p3_price))
print("\t{}\t\t${}".format(p4_name.title(),p4_price))
print("\t{}\t${}".format(p5_name.title(),p5_price))

print("="*50)

print("\t\t\t Total ")

total = p1_price + p2_price + p3_price + p4_price + p5_price
print("\t\t\t${}".format(total))

print("="*50)

print("\n\t{}\n".format(Message))

print("*"*50)