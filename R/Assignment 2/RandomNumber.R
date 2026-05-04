set.seed(1)
nums <- rnorm(10)
nums_round <- round(nums, 1)

num_list <- as.list(nums_round)
counts <- table(nums_round)

print(num_list)
print(counts)