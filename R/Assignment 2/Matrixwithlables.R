#  Create a 5 x 4 matrix (simple)
mat1 <- matrix(1:20, nrow = 5, ncol = 4)
rownames(mat1) <- c("R1","R2","R3","R4","R5")
colnames(mat1) <-
print("5 x 4 Matrix:")
print(mat1)


#  Create a 3 x 3 matrix with labels (fill by rows)
mat2 <- matrix(1:9, nrow = 3, byrow = TRUE)

# Add row and column names
rownames(mat2) <- c("R1", "R2", "R3")
colnames(mat2) <- c("C1", "C2", "C3")

print("3 x 3 Matrix (Row-wise filled with labels):")
print(mat2)


# 3️⃣ Create a 2 x 2 matrix with labels (fill by columns)
mat3 <- matrix(1:4, nrow = 2, byrow = FALSE)

# Add labels
rownames(mat3) <- c("Row1", "Row2")
colnames(mat3) <- c("Col1", "Col2")

print("2 x 2 Matrix (Column-wise filled with labels):")
print(mat3)