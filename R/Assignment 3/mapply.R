# Two vectors
a <- c(1, 2, 3, 4)
b <- c(10, 20, 30, 40)

# Add element-wise
result <- mapply(function(x, y) x + y, a, b)

print(result)