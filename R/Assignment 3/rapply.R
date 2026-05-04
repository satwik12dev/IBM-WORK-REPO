# Nested list
data <- list(a = 1:3,
             b = list(c = 4:6, d = 7:9))

# Multiply all elements by 2
result <- rapply(data, function(x) x * 2)
print(data)
print(result)