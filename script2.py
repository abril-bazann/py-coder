import sys

#print(f'hola {sys.argv[1]}') #lista

if len(sys.argv) !=3:
    print('error, necesito dos argumentos')
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1])