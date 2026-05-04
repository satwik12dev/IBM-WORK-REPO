# Input month number
month <- 12

# Check days
if (month %in% c(1, 3, 5, 7, 8, 10, 12)) {
  cat("31 days")
  
} else if (month %in% c(4, 6, 9, 11)) {
  cat("30 days")
  
} else if (month == 2) {
  cat("28 or 29 days")
  
} else {
  cat("Invalid month number")
}