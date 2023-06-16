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

front_edge_bar = water_trapper[0]
end_edge_bar = water_trapper[-1]
print(f"front_edge_bar  {front_edge_bar}")
print(f"end_edge_bar    {end_edge_bar}")

start, end, direction = None, None, 1
height = None
if end_edge_bar < front_edge_bar:
    start = len(water_trapper) - 1
    end = 0
    direction = -1
    height = end_edge_bar
else:
    end = len(water_trapper) - 1
    start = 0
    height = front_edge_bar


print(start, end, direction)
print(f"height {height} ")
store = []
end_bool = False
def guts(height, start, end, direction, water_trapper):
    for index in range(start, end-1, direction):
        print()
        print(index, start, end)
        print(f"[{index}] {water_trapper[index]}")
        print(f"sum {sum(store)} {store}")
        print(f"height {height}")

        if index == end:
            print(f"\t\t\tsum {sum(store)} {store}")
            print("\t\t\t===================")
        # if index != start or index != end:
        while water_trapper[index] < height:
            print(f"\t  [{index}] {water_trapper[index]} {end}")
            store.append(height-water_trapper[index])
            index += direction
            print(f"\t  index {index} end {end} {index == end} {sum(store)}")
        if index == end:
            print(f"\t\t\t gotta stop here {sum(store)}")
            end_bool = True
            break
        print(f"\t  [{index}] {water_trapper[index]}")
        guts(water_trapper[index], index - 1, end, direction, water_trapper)
        
        if end_bool == True:
            break

        
        # if start == end:
            # break


guts(height, start+direction, end, direction, water_trapper)
print()
print(store,sum(store))