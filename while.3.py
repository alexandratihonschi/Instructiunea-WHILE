n=eval(input('introduceti un numar:'))
s=0
while n%2==0 or (n%2!=0 and n%3!=0):
    if n%2==0:
        s+=n
    
    n=eval(input('introduceti un numar:'))

print('suma numerelor pare introduse:',s)