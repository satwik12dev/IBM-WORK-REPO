# Create a list
data <- list(a = 1:5, b = 6:10, c = 11:15)

# Find sum of each element
result <- vapply(data, sum, numeric(1))

print(result)