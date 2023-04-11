def dis(prime,price):
     
    if prime:
        discount_price=price*((1-0.08)*(1-0.15))
    else:
        discount_price=price*(1-0.08)
    return discount_price
prime=input()
price=int(input())
print(dis(prime,price))