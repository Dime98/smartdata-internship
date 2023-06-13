# 15. Given a binary array, find the index of 0 to be replaced with 1 to get the maximum length  sequence of continuous ones.

bin_array = [0,1,0,1,1,1,0,1,0,1]

# indx = [i for i in enumerate(bin_array) if i == 1]
indx = [i for i in range(len(bin_array)) if bin_array[i] == 1]
print(indx)