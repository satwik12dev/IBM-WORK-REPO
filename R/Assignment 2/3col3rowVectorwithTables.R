# Create two vectors
vec1 <- c(1, 2, 3, 4, 5, 6, 7, 8, 9)
vec2 <- c(10, 11, 12, 13, 14, 15, 16, 17, 18)

# Combine both vectors
values <- c(vec1, vec2)

# Create array: 3 rows, 3 columns, 2 tables
arr <- array(values, dim = c(3, 3, 2))

# Print the array
print(arr)