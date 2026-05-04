x <- 1:10
y <- x^2

plot(x,y,
     type="b",pch=19,xaxt="n",yaxt="n",
     main="Custom Axis Tick Spacing",
     xlab="X values",
     ylab = "Y values")

axis(slide=1,
     at = seq(1,10,by=2),
     labels = seq(1,10,by=2),
     col="red", col.axis = "darkgreen",
     tick = -0.02)
