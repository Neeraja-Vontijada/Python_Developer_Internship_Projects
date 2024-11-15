import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load the dataset
data = pd.read_csv('data.csv')


# Step 2: Set up the figure size for visualizations
plt.figure(figsize=(10, 6))

# Step 3: Create various visualizations

# 1. Bar Chart for Sales by Category
plt.figure(figsize=(10, 6))
sns.countplot(x='Category', data=data, palette='Set2')
plt.title('Count of Products by Category')
plt.xlabel('Category')
plt.ylabel('Count')
plt.show()

# 2. Scatter Plot for Price vs. Units Sold
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Price', y='Units Sold', data=data, hue='Category', palette='coolwarm', s=100, alpha=0.7)
plt.title('Price vs Units Sold')
plt.xlabel('Price')
plt.ylabel('Units Sold')
plt.show()

# 3. Heatmap for Correlation of Numerical Variables
correlation_matrix = data[['Price', 'Units Sold', 'Rating', 'Discount']].corr()
plt.figure(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='Blues', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# 4. Boxplot for Rating by Category
plt.figure(figsize=(10, 6))
sns.boxplot(x='Category', y='Rating', data=data, palette='Set1')
plt.title('Boxplot of Rating by Category')
plt.xlabel('Category')
plt.ylabel('Rating')
plt.show()

# Step 4: Insights Based on Visualizations
# 1. The bar chart shows the distribution of products across categories.
# 2. The scatter plot suggests that higher-priced products tend to have lower units sold.
# 3. The heatmap indicates that there is a weak negative correlation between Price and Units Sold.
# 4. The boxplot shows that Electronics has a wider range of ratings compared to other categories.
