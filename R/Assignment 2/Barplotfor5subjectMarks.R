# Marks of five subjects
marks <- c(85, 90, 78, 88, 92)

# Subject names
subjects <- c("Math", "Science", "English", "Computer", "History")

# Create bar plot
barplot(marks,
        names.arg = subjects,
        col = "skyblue",
        main = "Marks of Five Subjects",
        xlab = "Subjects",
        ylab = "Marks")