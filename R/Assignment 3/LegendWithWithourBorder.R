x <- 1:5
y1 <- c(2,4,6,8,10)
y2 <- c(1,3,5,7,9)

plot(x, y1,
     type="o", col="blue", pch=16, ylim=c(0,10),
     main="Legend with border",
     xlab="X-Axis", ylab="Y-Axis")

# Add second line
lines(x, y2, type="o", col="red", pch=17)

# Correct axis syntax
axis(side = 1, at = seq(1, 5, by = 1), labels = seq(1, 5, by = 1))

# Legend without border
legend("topleft",
       legend=c("Line1","Line2"),
       col=c("blue","red"),
       pch=c(16,17),
       lty=1,
       bty="o",   # removes border
       bg="white")