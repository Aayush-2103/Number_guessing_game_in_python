while True:
    print('\t\t*****Your own CALCULATOR*****\n')
    a=float(input('1st number:- '))
    b=float(input('2nd number:- '))
    c=input('Operator:- ')

    if c=='+':
        print('Result ', a+b, '\n')

    elif c=='-':
        print('Result ', a-b, '\n')

    elif c=='*':
        print('Result ', a*b, '\n')
    
    elif c=='/':
        print('Result ', a/b, '\n')

    else:
        print('Enter Valid operator\n\n')
        continue
    