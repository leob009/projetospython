from random import randint


def cria_matriz(num_l, num_col):
    mat = []
    l = []
    while len(mat) != num_l:
        l.append(randint(0, 99))
        if len(l) == num_l:
            mat.append(l)
            l = []
    return mat
num_lin = 5
num_col = 5
mat = cria_matriz(num_lin, num_col)


print('*   '*11)
for lin in range(0,num_lin):
    for col in range(0,num_col):
        print(f'{mat[lin][col]:02}',end='  ')
    print('*')
print('*   '*11)

# while True:
#     print(mat[lin][col],end=' ')
#     col +=1
#     if col == 10:
#         print('\n')
#         col = 0
#         lin +=1



