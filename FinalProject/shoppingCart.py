class Item:
    #attributes
    name="undefined"
    price=10.0
    stock=0
    discount=0.0
    taxable=True
    #initializer
    def __init__(self,s,p,n,d,t):
        self.name=s
        self.price=p
        self.stock=n
        self.discount=d
        self.taxable=t
    #mutators
    def set_name(self,val):
        self.name=val

    def set_price(self,val):
        self.price=val

    def set_stock(self,val):
        self.stock=val

    def set_discount(self,val):
        self.discount=val

    def set_taxable(self,val):
        self.taxable=val
    #accessors
    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_stock(self):
        return self.stock
    def get_discount(self):
        return self.discount
    def get_taxable(self):
        return self.taxable
    #print function
    def print_item(self):
        print("Name:",self.name)
        print("price:",self.price)
        print("stock:",self.stock)
        print("discount:",self.discount)
        print("taxable:",self.taxable)
        print()

all_items=[]
file= open("Items_info.txt","r")

for line in file:
    attributes = line.strip().split(',')
    item = Item(s=attributes[0],
                p=float(attributes[1]),
                n=int(attributes[2]),
                d=float(attributes[3]),
                t=attributes[4]=='y')
    all_items.append(item)

cart={}

def show():
    for item in all_items:
        print("Name:",item.get_name())
        print("Price: $",item.get_price())
        discounted_price=item.get_price()-item.get_price()*item.get_discount()/100
        print("Discounted Price: $",discounted_price)
        print()

def add_to_cart():
    name=input("Enter item you want to add: ")
    quantity=int(input("How many do you want to add: "))
    try:
        for item in all_items:
            if item.get_name()==name:
                if quantity<=item.get_stock():
                    if name in cart:
                        cart[name]+=quantity
                    else:
                        cart[name]=quantity
                    item.set_stock(item.get_stock()-quantity)
                    print(quantity,name,"has been added to your cart")
                    break
                else:
                    print("Not enough stock")
                    break
        else:
            print("Item not found in the inventory")
    except:
        print("Error")

def delete():
    name=input("What item do you want to delete from your cart?: ")
    quantity=int(input("How many do you want to delete: "))
    try:
        if name in cart:
            if quantity<=cart[name]:
                cart[name]-=quantity
                item.set_stock(item.get_stock()+quantity)
                print(quantity,name,"deleted from your cart.")
            else: 
                print("not enough stock")
        else:
            print("Item not in cart.")
    except:
        print("Error")
    
def show_cart():
    for name, quantity in cart.items():
        item=next((item for item in all_items if item.get_name()==name),None)
        if item:
            discounted_price=item.get_price()*(1-item.get_discount()/100)
            print("Item:",name)
            print("Price: $",item.get_price())
            print("Discounted Price: $",discounted_price)
            print("Quantity in Cart:",quantity)
            print()
        else:
            print("Item",name,"not found in item list.")

def checkout():
    total_price=0.0
    missouri_tax_rate=0.04225
    
    for name, quantity in cart.items():
        item=next((item for item in all_items if item.get_name()==name),None)
        if item:
            discount_price=item.get_price()*(1-item.get_discount()/100)
            total_price+=discount_price*quantity

        else:
            print("Item",name,"not found in item list.")
    
    sales_tax=total_price*missouri_tax_rate
    final_amount=total_price+sales_tax

    print("Price after discount: $",total_price)
    print("Sales tax: $",sales_tax)
    print("Total price: $",final_amount)

    with open("items_info_updated.txt","w") as file:
        for item in all_items:
            allitems=f"{item.get_name()},{item.get_price()},{item.get_stock()},{item.get_discount()},{item.get_taxable()}\n"
            file.write(allitems)

while True:
    command=input("type show, add, delete, cart, check out, or done")

    if command=="show":
        show()
    elif command=="add":
        add_to_cart()
    elif command=="delete":
        delete()
    elif command=="cart":
        show_cart()
    elif command=="check out":
        checkout()
        break
    elif command=="done":
        break
    else:
        print("Not one of the options")
