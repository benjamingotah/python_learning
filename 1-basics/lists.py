ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

# min age 

print("This is the minimum age: ", +  min(ages))

#max age

print("This is the maximum age: ", +  max(ages))

# add min age to list
ages.append(min(ages))
print(ages)

# add max age to list
ages.append(max(ages))
print(ages)

# to find median, if odd len/2 = 1, or len/2 is even