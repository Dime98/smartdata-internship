# 13. Read a list of numbers from a file, add to each number a value such that in the end they
# will be sorted ascendantly. Save new numbers into the same file.

file_arr = []

with open('13_numbers.txt', encoding="utf8") as file:
    for line in file: 
        line = line.strip()
        # print(line)
        try:
            file_arr.append(int(line))
        # i know except pass wrong
        except:
            pass


lst = [0]
added_sorted = []
for i in file_arr:
    added_sorted.append(i+max(lst))
    print()
    print(f"i     {i}")
    print(f"max   {max(lst)}")
    print(f"i+max {i+max(lst)}")
    lst.append(i+max(lst))
    print(f"lst   {lst}")

print()
for i in added_sorted:
    print(i)
#     with open('13_numbers.txt', 'a') as f:
#         context = str(i) + "\n"
#         f.write(context)