
employee_df <- data.frame(
  emp_id <- c(1, 2, 3, 4, 5),
  name <- c("A", "B", "C", "D", "E"),
  age <- c(22, 27, 25, 21, 39),
  department <- c("HR", "IT", "Finance", "Marketing", "Sales")
)


# Display summary
print("Summary of Data:")
print(summary(employee_df))