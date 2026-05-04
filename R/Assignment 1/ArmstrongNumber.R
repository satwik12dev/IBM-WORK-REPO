# Input number
num <- 121

# Store original number
temp <- num

# Count digits
n <- nchar(num)

# Initialize sum
sum <- 0

# Calculate Armstrong sum
while (temp > 0) {
  digit <- temp %% 10
  sum <- sum + digit^n
  temp <- temp %/% 10
}

# Check result
if (sum == num) {
  cat(num, "is an Armstrong Number")
} else {
  cat(num, "is NOT an Armstrong Number")
}