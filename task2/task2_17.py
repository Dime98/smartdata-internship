# 17. Find the maximum amount of water that can be trapped within a given set of bars where 
# each bar's width is 1 unit (photo attached).

# 9. Tips or ex 17: You shoud find if there exists a local minima (you may represent bars
# as a list, where the numbers are the height of the bars). You could have water only when 
# both neighbours are haigher than the bar (set of bars). The amount of added water equals
# the smallest bar.

water_trapper = {
    0: 7,
    1: 0,
    2: 4,
    3: 2,
    4: 5,
    5: 0,
    6: 6,
    7: 4,
    8: 0,
    9: 5,
}

water_trapper = [7, 0, 4, 2, 5, 0, 6, 4, 0, 5,]
print(water_trapper)