# 9. Calculate the euclidean distance between two points in the space given 
# their coordinates (x1, y1) and (x2, y2).

import math
p = [3, 2] 
q = [4, 1] 

# Calculate Euclidean distance
print (math.dist(p, q))

x1, y1 = p[0], p[1]
x2, y2 = q[0], q[1]

# √ ( (x1 - x2)² + (y1 - y2)² )
distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
# print(f"math.sqrt( ({x1}-{x2})**2 + ({y1}-{y2})**2 )")
print(distance)

