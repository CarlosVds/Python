pharse = "         Python is very easy to learn, but without practice you won't learn it."

list_pharse = pharse.split(", ")

for i, pharse in enumerate(list_pharse):
    print(list_pharse[i].strip())

list_pharse_2 = ', '.join(list_pharse)

print(list_pharse_2.strip())


