# Define three numbers
a <- 10
b <- 25
c <- 15

# Find largest
if (a >= b && a >= c) {
  largest <- a
} else if (b >= a && b >= c) {
  largest <- b
} else {
  largest <- c
}

# Output
cat("Largest number is:", largest)