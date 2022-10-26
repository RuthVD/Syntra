
def exercise1(array2D):
    pass #write your code here
    som = 0
    for i in array2D:
        for k in i:
            som += k
    return (som)
    
lijst = [[1,2,3,], [4,5]]
print(exercise1(lijst))


def exercise2():
    pass #write your code here
    nieuweLijst = []
    for i in range (1,21):
        nieuweLijst.append(i**2)
    return (nieuweLijst)

print(exercise2())


def exercise3(x, y, z):
    pass #write your code here
    if x == y or y==z or x==z:
        return 0
    else:
        return x+y+z

a = 3
b = 15
c = 10
print(exercise3(a,b,c))

def exercise4(array1, array2):
    pass #write your code here
    nieuweLijst = []
    if len(array1)==len(array2):
        for i in range(len(array1)):
            nieuweLijst.append(array1[i]+array2[i])
        return nieuweLijst
    else:
        return "Fout: lijsten verschillen in lengte"
  
lijst1 = [1,2,3,4]
lijst2 = [5,6,7,8]

print(exercise4(lijst1,lijst2))


    

# def exercise5(array):
#     pass #write your code here

    
# array = [[1, 3, 1, 1, 4],
#          [2, 4, 3, 1, 2],
#          [3, 5, 4, 1, 1],
#          [4, 6, 2, 1, 4]]