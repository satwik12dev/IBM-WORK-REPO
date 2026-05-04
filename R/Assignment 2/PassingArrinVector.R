# Create a vector of values
values <- c(1:12)

# Define dimensions (2 x 3 x 2 array)
dims <- c(2, 3, 2)

# Create array
arr <- array(values, dim = dims)

# Assign names to each dimension
dimnames(arr) <- list(
  Row = c("R1", "R2"),
  Column = c("C1", "C2", "C3"),
  Matrix = c("M1", "M2")
)

# Print array
print(arr)