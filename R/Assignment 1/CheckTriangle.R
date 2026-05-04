# Take input from user
a <- as.numeric(readline("Enter side a: "))
b <- as.numeric(readline("Enter side b: "))
c <- as.numeric(readline("Enter side c: "))

# Check triangle validity
if (a + b > c && a + c > b && b + c > a) {
  
  if (a == b && b == c) {
    cat("Triangle is Equilateral")
    
  } else if (a == b || b == c || a == c) {
    cat("Triangle is Isosceles")
    
  } else {
    cat("Triangle is Scalene")
  }
  
} else {
  cat("Not a valid triangle")
}