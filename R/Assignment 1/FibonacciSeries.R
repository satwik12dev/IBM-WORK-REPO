# Number of terms
n <- 10

# First two terms
a <- 0
b <- 1

cat("Fibonacci Series:\n")
cat(a, b, sep = " ")

for(i in 3:n) {
  c <- a + b
  cat(c, " ")
  a <- b
  b <- c
}