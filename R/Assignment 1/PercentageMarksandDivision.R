# Take input from user
m1 <- as.numeric(readline("Enter marks of Subject 1: "))
m2 <- as.numeric(readline("Enter marks of Subject 2: "))
m3 <- as.numeric(readline("Enter marks of Subject 3: "))

# Calculate total
total <- m1 + m2 + m3

# Calculate percentage
percentage <- total / 3

# Determine division
if (percentage >= 60) {
  division <- "First Division"
} else if (percentage >= 50) {
  division <- "Second Division"
} else if (percentage >= 40) {
  division <- "Third Division"
} else {
  division <- "Fail"
}

# Display result
cat("Total Marks =", total, "\n")
cat("Percentage =", percentage, "\n")
cat("Division =", division)