# 19. Write a program that given 3 different dictionaries will concatenate them and create 
# new one.

d1 = {
    "d1-1" : "d1-1",
    "d1-2" : "d1-2",
    "d1-3" : "d1-3",
    }

d2 = {
    "d2-1" : "d2-1",
    "d2-2" : "d2-2",
    "d2-3" : "d2-3",
    }

d3 = {
    "d3-1" : "d3-1",
    "d3-2" : "d3-2",
    "d3-3" : "d3-3",
    }

d_sum = {}

d_sum.update(d1)
d_sum.update(d2)
d_sum.update(d3)
# print(d_sum)
for k,v in d_sum.items():
    print(k,v)