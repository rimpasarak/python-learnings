# List comprehension for the squares of all even numbers between 0 and 9
result = [x**2 for x in range(10) if x % 2 == 0]
print(result) #print square of x (x**2)


#prints x
for x in range (20):
    if(x%2==0):
        print (x)
        
        
groups = [["Jobs", "Gates"], ["Newton", "Euclid"], ["Einstein", "Feynman"]]

# This outer loop will iterate over each list in the groups list
for group in groups:
  # This inner loop will go through each name in each list
  for name in group:
    print(name)