x = int(input("Digite um valor inteiro "))
y = 1
z = 0
if(x<=0):
    print("Número inválido ")
else:
    while(y<=x):
        if((x%y)==0):
            z = z + 1 
        y = y + 1 
    if(z>2 or z == 1):
        print("Não primo")
    else:
        print("Primo")
        

