# Create a list
data <- list(a = 1:5, b = 6:10, c = 11:15)

print("Original List:")
print(data)

# Apply sum to each element
result <- lapply(data, sum)

print("Result:")
print(result)