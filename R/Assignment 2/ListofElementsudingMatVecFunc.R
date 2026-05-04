# Create a vector
vec <- c(1, 2, 3, 4, 5)

# Create a matrix
mat <- matrix(1:6, nrow = 2, ncol = 3)

# Create a function
my_function <- function(x) {
  return(x^2)
}

# Create a list containing vector, matrix, and function
my_list <- list(
  Vector = vec,
  Matrix = mat,
  Function = my_function
)

# Print the list
print(my_list)