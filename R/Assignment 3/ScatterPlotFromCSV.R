# Read CSV
data <- read.csv("C:\\Users\\SATWIK\\OneDrive\\Desktop\\R\\CSV files\\data.csv",
                 stringsAsFactors = FALSE)

# Convert Age to numeric (safety)
data$Age <- as.numeric(data$Age)

# Remove NA values
data <- na.omit(data)

# Convert Name (text) to numeric positions
name_num <- as.numeric(as.factor(data$Name))

# Plot
plot(name_num, data$Age,
     main = "Scatter Plot of Name vs Age",
     xlab = "Name",
     ylab = "Age",
     col = "blue",
     pch = 19,
     xaxt = "n")   # remove default x-axis

# Add proper Name labels on x-axis
axis(1, at = name_num, labels = data$Name)

# Add grid
grid()