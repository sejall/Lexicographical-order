
my_arr = [
   "hello",
   "apple",
   "actor",
   "people",
   "dog"
]
print(my_arr)

# Create a new array using the sorted method
new_arr = sorted(my_arr)

print(new_arr)

# This time, my_arr won't change in place, rather, it'll be sorted 
# and a new instance will be assigned to new_arr
print(my_arr)