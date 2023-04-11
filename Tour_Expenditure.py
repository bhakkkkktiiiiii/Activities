def hotel_exp(room_type,days,food_price):
    if room_type == 'Deluxe room':
        p = 7500*days
        print('price_of_stay:',p)
        sgst = 0.09*food_price
        cgst = 0.09*food_price
        tip = 0.1*food_price
        print('SGST:', round(sgst, 2)) 
        print('CGST:', round(cgst, 2)) 
        print('Tip:', round(tip, 2))
        print('Grand total for meal:', r+sgst+cgst+tip)
        
    elif room_type=='Non AC Room':
        p = 4500 * days
        print('price_of_stay:', p)
        sgst = 0.025 * food_price
        cgst = 0.025 * food_price
        tip = 0.1 * food_price
        print('SGST:', round(sgst, 2))
        print('CGST:', round(cgst, 2)) 
        print('Tip:', round(tip, 2))
        print('Grand total for meal:', r+sgst+cgst+tip)
    else:
        print('Invalid room type')
p = input('Type of room: ') #room_type
q = int(input('Number of days you stayed: ')) #days
r = int(input('Total food amount: ')) #food_price

hotel_exp(p,q,r)
