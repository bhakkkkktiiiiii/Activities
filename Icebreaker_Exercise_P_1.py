n=int(input())
if n < 380 or n > 750:
    print("Error")
else:
    
    if n<450:
        print('Violet')
    elif n<495:
        print('Blue')
    elif n<570:
        print('Green')
    elif n<590:
        print('Yellow')
    elif n<620:
        print('Orange')
    else:
        print('Red')
