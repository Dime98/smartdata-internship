# 6. Using cycles, print following:
# a)*		         b) * * * * *	    c)          *	       d) * * * * *       e)         *
#   * *		            * * * *               	  * *               * * * *                * * *
#   * * *		        * * *		            * * *                 * * *              * * * * *
#   * * * *	  	    	* *		              * * * *		            * *		       * * * * * * *
#   * * * * *	      	*		            * * * * *		              *  	     * * * * * * * * *

print("\na) ")
for i in range(6):
	print(i*"* ")


print("\nb) ")
for i in range(6)[::-1]:
	print(i*"* ")

# don't know how to make it so * would have spacing
print("\nc) ")
arr_len = 6
for i in range(arr_len):
	# print()
	# print(i)
	# print((arr_len-i-1),(i+1))
	print((arr_len-i-1)*" " , end = " ")
	print((i+1) * "*",end = "\n")

# don't know how to make it so * would have spacing
print("\nd) ")
arr_len = 6
for i in range(arr_len)[::-1]:
	# print()
	# print(i)
	# print((arr_len-i-1),(i+1))
	print((arr_len-i-1)*" " , end = " ")
	print((i+1) * "*",end = "\n")

# made e) by mistake while working on c) :)
print("\ne) ")
arr_len = 6
for i in range(arr_len):
	# print(i+1, arr_len-i-1)
	# print(type(arr_len))
	# print(type(i))
	print((arr_len-i-1)*" " , (i+1) * "* ")