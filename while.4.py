n=eval(input('introduceti un numar:'))
c=0
s=0
p=1
while c<n:
    c+=1
    s+=c
    p*=c

print(f'suma={round(s, 2)}',f'produsul={round(p, 2)}',f'media aritmetica={round(s/c, 2)}', sep='\n')