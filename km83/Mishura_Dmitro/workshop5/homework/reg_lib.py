import re

def get_client():
    client=input("client name")
    if re.match(r"^[A-Z]{1}[a-z]+$", client):
        return client
    else:
        return get_client
#print(get_client())
def get_date():
    date=input("date")
    if re.match(r"^([0-2][0-9]|[3][0-1])\.([0][1-9]|[1][0-2])\.\d{4}$", date):
        return date
    else:
        return get_date()
#get_date()
def get_product():
    product=input("product")
    if re.match(r"^[a-z]+$", product):
        return product
    else:
        return get_product()
#print(get_product())
def get_quantity():
    quantity=input("quantity")
    if(re.match(r"^\d+\.\d{0,2}$", quantity)):
        return quantity
    else:
        return get_quantity()
#print(get_quantity_or_price())
def get_price():
    price=input("price")
    if(re.match(r"^\d+\.\d{2}$", price)):
        return price
    else:
        return get_price()
