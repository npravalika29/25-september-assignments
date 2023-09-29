list_a = [42,73,88,54,21]
def maximum(a):
    res = a[0]
    for i in range(1,len(a)):
        if res < a[i]:
            res = a[i]
    print(res)
maximum(list_a)   
    

            
            

