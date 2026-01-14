price = int(input("Enter price"))
quantity = int(input("Enter quantity"))
sales = price*quantity

if sales >= 5000 and sales <= 7000:
    discount = sales/10
if sales <= 5000:
    discount = sales/5

netprice = sales-discount
print(f"The price of the product is {price}₹")
print(f"The quantity ordered is  {quantity}")
print(f"The amount of SALES is {sales}")
print(f"Your discount is {discount}")
print(f"The total Net price is {netprice}₹")