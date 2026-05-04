# Marks of students
marks <- c(80, 75, 90, 60, 85, 70)

# Groups (sections)
group <- c("A", "A", "B", "B", "A", "B")

# Find average marks per group
result <- tapply(marks, group, mean)

print(result)