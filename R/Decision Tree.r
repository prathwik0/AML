# Load necessary libraries
library(rpart)

# Load the built-in iris dataset
data(iris)

# Split the data into training and testing sets
set.seed(123)  # Setting seed for reproducibility
train_indices <- sample(1:nrow(iris), 0.7 * nrow(iris))  # 70% for training
train_data <- iris[train_indices, ]
test_data <- iris[-train_indices, ]

# Create a decision tree model using the training data
# We'll predict the 'Species' column based on other features
tree_model <- rpart(Species ~ ., data = train_data)

# Make predictions on the test data using the decision tree model
predicted_species <- predict(tree_model, newdata = test_data, type = "class")

# Compare the predicted species with the actual species in the test data
accuracy <- sum(predicted_species == test_data$Species) / nrow(test_data)
cat("Accuracy:", accuracy)

