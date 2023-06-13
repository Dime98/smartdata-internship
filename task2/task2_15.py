# 15. Given a binary array, find the index of 0 to be replaced with 1 to get the maximum length  sequence of continuous ones.

bin_array = [0,1,0,1,1,1,0,1,0,1]

# indx = [i for i in enumerate(bin_array) if i == 1]
indx = [i for i in range(len(bin_array)) if bin_array[i] == 1]
print(indx)

def longest_continuous_subarray(arr):
    max_length = 0
    current_length = 0
    start_index = 0
    end_index = 0

    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1] + 1:
            current_length += 1
        else:
            current_length = 1

        if current_length > max_length:
            max_length = current_length
            start_index = i - current_length + 1
            end_index = i

    return arr[start_index:end_index+1]

print(longest_continuous_subarray(indx))

# dictionary = {}
# for i in range(len(indx)):
# 	print(indx[i])
# 	flag = True
# 	# while flag == True or i != len(indx)-1:
# 	while flag == True:
# 		if i != len(indx)-2:
# 			flag = False
# 		print("\t while")
# 		print("\t",indx[i]+1)
# 		print("\t",indx[i+1])
# 		flag = False
# 		if indx[i]+1 == indx[i+1]:
# 			print("==")
# 			i+=1
# 		else:
# 			print("not ==")
# 			flag = False