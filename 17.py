import math

def myDistance(a,b):  #İki vektör uzaklığı bulup gönderdi.
    my_Point_1=a
    my_Point_2=b
    a=(my_Point_1[0]-my_Point_2[0])**2
    b=(my_Point_1[1]-my_Point_2[1])**2
    return math.sqrt(a+b)

def findCenter(List_of_Points):
    a = 0
    b = 0
    for point in List_of_Points:
        a = a + point[0]
        b = b + point[1]
    l = len(List_of_Points)
    return [a/l,b/l]

my_Point_1=[0,0]
my_Point_2=[1,0]
my_Point_3=[0,1]
my_Point_4=[1,1]

my_Point_List = []
my_Point_List.append(my_Point_1)
my_Point_List.append(my_Point_2)
my_Point_List.append(my_Point_3)
my_Point_List.append(my_Point_4)
center=findCenter(my_Point_List)
print("\ncenter point:\n")
print(center)

print(myDistance(my_Point_2,my_Point_3))

a = my_Point_1[0] + my_Point_2[0] + my_Point_3[0] + my_Point_4[0]
b = my_Point_1[1] + my_Point_2[1] + my_Point_3[1] + my_Point_4[1]
center_Point = [a/4,b/4]
print("\ncenter point:\n")
print(center_Point)
