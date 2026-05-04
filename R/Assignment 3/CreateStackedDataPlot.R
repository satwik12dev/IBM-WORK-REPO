values <- c(1,2,2,3,3,3,4,4,5)
group <- c("A","A","B","B","A","B","A","B","A")

stripchart(values ~ group,
           method = "stack",
           pch = 19,
           col = c("blue","green")
           )