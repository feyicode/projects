my_dict = {}
for i in range(1,1001):
    my_dict[i] = True
    if i % 2 == 0:
        my_dict[i] = False

open_count=0

for i in range(1,1001):
    for x in range (3,1001):
        if i % x == 0:
            my_dict[i] = not(my_dict[i])

for i in my_dict:
    if my_dict[i] == True:
        open_count += 1

print(open_count)