#install.packages("randomForest")
# Load necessary libraries
library(randomForest)

# Load the built-in iris dataset
data(iris)

# Split the data into training and testing sets
set.seed(123)  # Setting seed for reproducibility
train_indices <- sample(1:nrow(iris), 0.7 * nrow(iris))  # 70% for training
train_data <- iris[train_indices, ]
test_data <- iris[-train_indices, ]

# Create a Random Forest model using the training data
# We'll predict the 'Species' column based on other features
rf_model <- randomForest(Species ~ ., data = train_data)

# Make predictions on the test data using the Random Forest model
predicted_species <- predict(rf_model, newdata = test_data)

# Compare the predicted species with the actual species in the test data
accuracy <- sum(predicted_species == test_data$Species) / nrow(test_data)
cat("Accuracy:", accuracy)
