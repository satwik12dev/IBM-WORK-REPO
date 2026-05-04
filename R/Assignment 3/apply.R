# Create a matrix
data <- matrix(c(10, 20, 30,
                 40, 50, 60),
               nrow = 2, byrow = TRUE)

print("Matrix:")
print(data)

# Apply function on rows (sum)
row_sum <- apply(data, 1, sum)
print("Sum of each row:")
print(row_sum)
