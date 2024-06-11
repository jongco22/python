#이중 for문
com_ls=[i*j for i in range(2,10) for j in range(1,10)]

#일반 반복문
gen_ls=[]
for i in range(2,10):
    for j in range(1,10):
        gen_ls.append(i*j)
        
print(com_ls)
print(gen_ls)
