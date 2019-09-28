a = [10, 13 ,5 ,24 ,18]

max=a[0]

for i in a:
    if i>max:
        max = i

min = a[0]

for i in a:
    if i<min:
        min = i

print(min+max)
