values <- c(10,20,15,25,30,18,22)
names(values) <- c("A","B","C","D","E","F","G")

barplot(values,
        names.arg = names(values),
        las=2,
        col="skyblue",
        main="Barplot with all x-axis labels",
        xlab="categories",ylab="values")

par(mar = c(8,4,4,2))