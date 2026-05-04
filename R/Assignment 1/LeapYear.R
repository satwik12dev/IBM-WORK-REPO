# Input year
year <- 2024

# Check leap year
if ((year %% 400 == 0) || (year %% 4 == 0 && year %% 100 != 0)) {
  cat(year, "is a Leap Year")
} else {
  cat(year, "is NOT a Leap Year")
}