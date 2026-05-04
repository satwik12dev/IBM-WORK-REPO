# Input number
num <- 7

# Flag variable
is_prime <- TRUE

# Check conditions
if (num <= 1) {
  is_prime <- FALSE
} else {
  for (i in 2:(num - 1)) {
    if (num %% i == 0) {
      is_prime <- FALSE
      break
    }
  }
}

# Output
if (is_prime) {
  cat(num, "is a Prime Number")
} else {
  cat(num, "is NOT a Prime Number")
}