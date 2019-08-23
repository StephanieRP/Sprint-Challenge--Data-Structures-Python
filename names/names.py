import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# adding both lists to a new variable
sorted_names = names_1 + names_2
# sorting the list
sorted_names.sort()

# iterating over the list
for index in range(len(sorted_names)):
    # if two names match, then add to duplicates list
    if sorted_names[index] == sorted_names[index - 1]:
        duplicates.append(sorted_names[index])


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
