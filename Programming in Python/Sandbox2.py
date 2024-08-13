title = input('Enter the title of the book: ')
author = input('Enter the book author name: ')
price = float(input('Enter the price of the book in INR: '))
stock = int(input("Enter the stock Quantity of the book: "))
purchaseQty = int(input("Enter the purchase Quantity: "))
print(f"The title of the book is {title}\n Author name is {author}\n Price is {price:2f}\n and the stock Quantity is {stock}")
if stock>purchaseQty:
    print("The Book is in the Stock.")
else :
    print("The Book is out of Stock.")