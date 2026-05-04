# Create vectors for employee details
emp_id <- c(101, 102, 103, 104, 105)
name <- c("Amit", "Neha", "Ravi", "Priya", "Karan")
age <- c(25, 30, 28, 26, 32)
department <- c("HR", "IT", "Finance", "Marketing", "Sales")
salary <- c(30000, 50000, 45000, 40000, 55000)

# Create dataframe
employee_df <- data.frame(emp_id, name, age, department, salary)

# Display dataframe
print(employee_df)