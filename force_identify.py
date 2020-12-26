l=int(input('Enter the total length '))
print(l,'m')
x=float(input('Enter the position refering from left end '))
print(x,'m')
w=int(input('Enter the total weight '))
print(w,'Kg')
Rc=(x/l)*w
Lc=w-Rc
print('Left side support reaction =',Lc,'Kg')
print('Right side support reaction =',Rc,'Kg')