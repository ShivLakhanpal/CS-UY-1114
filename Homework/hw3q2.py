print("Welcome to our shop! Buy one get one half off promotion! Please enter prices of items below: ")

first_item = float(input("Please enter the price of first item: "))
second_item = float(input("Please enter the price of second item (Half off): "))
club_card = input("Do you have a club card? " + " (Y/N): ")
tax_rate = float(input("Please enter tax rate: "))

Y = "Y"
N = "N"
base_price = first_item + (second_item)/(2)
price_without_discount = base_price
price_with_discount = base_price * 0.9
tax = tax_rate/100
total_price_with = (price_with_discount)*(tax) + (price_with_discount)
total_price_without = (price_without_discount)*(tax) + (price_without_discount)
                                        

if (club_card == Y):
    print("Base Price = " + str(base_price))
    print("Price After Discounts = " + str(price_with_discount))
    print("Total Price = " + str(total_price_with))
else:
    if (club_card == N):
        print("Base Price = " + str(base_price))
        print("Price After Discounts = " + str(price_without_discount))
        print("Total Price = " + str(total_price_without))
        
