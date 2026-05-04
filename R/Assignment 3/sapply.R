# Create a list
data <- list(a = 1:5, b = 6:10, c = 11:15)

print("Original List:")
print(data)

# Find sum of each element
result <- sapply(data, sum)

print("Sum of each list element:")
print(result)