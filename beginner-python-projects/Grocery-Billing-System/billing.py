# project 2:Grocery Billing System 🛒

milk_price = 50
bread_price = 40
egg_price = 10

milk_qty = int(input("Enter kitna milk chahiye (liters): "))
bread_qty = int(input("Enter kitna bread chaiye (loaf):  "))
egg_qty = int(input("Enter kitnay egg chaiye: "))

bill = (milk_qty * milk_price) + (bread_qty * bread_price) + (egg_qty * egg_price)

if bill > 500:
    discount = bill * 0.10
    final_amount = bill - discount
    print("you get a 10%  discount!")
    print("final bill after discount: Rs.", final_amount)
else:
    print("no discount. total bill:, Rs.", bill)




marks = {}

x = int(input("enter phy : "))
marks.update({"phy" : x})

x = int(input("enter math : "))
marks.update({"math" : x})

x = int(input("enter chem : "))
marks.update({"chem" : x})

print(marks)
