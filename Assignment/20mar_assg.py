"""
Q1. What is data encoding? How is it useful in data science?
Ans:
Data encoding is the process of converting data from one format to another for the purpose of efficient transmission, storage, or processing. 
In data science, encoding is a crucial step in data preparation that involves transforming raw data into a form that can be used by machine 
learning algorithms.
There are different types of data encoding techniques, such as one-hot encoding, label encoding, and binary encoding. One hot encoding, also 
known as nominal encoding, is a technique used to represent categorical data as numerical data, which is more suitable for machine learning 
algorithms. In this technique, each category is represented as a binary vector where each bit corresponds to a unique category. For example, 
if we have a categorical variable "color" with three possible values (red, green, blue), we can represent it using one hot encoding as follows:

Red: [1, 0, 0] Green: [0, 1, 0] Blue: [0, 0, 1]
"""
"""
Q2. What is nominal encoding? Provide an example of how you would use it in a real-world scenario.
Ans:
Nominal encoding is a type of data encoding technique used to convert categorical variables into numerical features. In nominal encoding, each 
category in a categorical variable is assigned a unique integer value without any inherent order or rank.
For example, suppose we have a dataset of customer reviews for a restaurant, where the "rating" column can take one of four values: "excellent", 
"good", "fair", or "poor". We can use nominal encoding to convert the "rating" column into a numerical feature by assigning a unique integer value 
to each category:
"excellent": 1 "good": 2 "fair": 3 "poor": 4 In a real-world scenario, nominal encoding can be useful in various applications. For instance, in a 
customer feedback analysis system, we may want to analyze customer reviews of a product or service by sentiment. Using nominal encoding, we can 
convert the "sentiment" column, which could take values such as "positive", "negative", or "neutral", into a numerical feature that can be used in 
machine learning models to predict customer sentiment. By encoding the categorical variable into a numerical feature, we can extract valuable 
insights from the data and make more informed decisions based on customer feedback.

## creating a dataframe
import pandas as pd
df = pd.DataFrame({
    "rating":["excellent","good","poor","fair","fair","excellent","excellent","good","fair","poor","poor","poor","fair"]
})
df.head()
# nominal encoding with "excellent": 1 "good": 2 "fair": 3 "poor":4
df["rating_nominal"] = df["rating"].replace({"excellent": 1,"good": 2 ,"fair": 3 ,"poor":4})
#final result
df.head()
"""
"""
Q3. In what situations is nominal encoding preferred over one-hot encoding? Provide a practical example.
Ans:
Nominal encoding is preferred over one-hot encoding in situations where the number of categories in a categorical variable is very large. One-hot 
encoding creates a new binary feature for each category, which can result in a large number of features and may lead to overfitting, especially 
when the number of categories is much larger than the number of samples in the dataset.
In contrast, nominal encoding assigns a unique integer value to each category, which can reduce the dimensionality of the data and improve the 
performance of machine learning algorithms. Nominal encoding is also preferred when there is no inherent order or rank among the categories.

A practical example where nominal encoding may be preferred over one-hot encoding is in analyzing customer transaction data. Suppose we have a 
dataset of customer transactions for an e-commerce website, where the "product category" column can take one of several hundred values. If we were 
to use one-hot encoding to convert this categorical variable into numerical features, we would end up with several hundred binary features. This 
would result in a high-dimensional dataset and may lead to overfitting, especially if the number of samples is limited.
On the other hand, using nominal encoding to convert the "product category" column into a numerical feature would reduce the dimensionality of 
the data and help in improving the performance of machine learning algorithms. Nominal encoding would also be preferred here since there is no 
inherent order or rank among the product categories.
"""
"""
Q4. Suppose you have a dataset containing categorical data with 5 unique values. Which encoding technique would you use to transform this data into a format suitable for machine learning algorithms? Explain why you made this choice.
Ans:
The choice of encoding technique depends on the specific characteristics of the data and the requirements of the machine learning algorithm. 
However, with only 5 unique values in the categorical data, one-hot encoding would be a suitable choice to transform this data into a format 
suitable for machine learning algorithms.
One-hot encoding would create 5 binary features, one for each unique value in the categorical data. Each sample in the dataset would have a value 
of 1 in the corresponding feature and a value of 0 in all other features. This would allow machine learning algorithms to use the categorical data 
as input for training models and making predictions.
One reason for choosing one-hot encoding in this case is that the number of unique values is relatively small. One-hot encoding is particularly 
useful when the number of unique values in a categorical variable is small, as it leads to a sparse matrix with a manageable number of columns. 
Furthermore, one-hot encoding would ensure that the categorical data is treated as nominal data with no inherent order or ranking among the unique 
values. This is important when using machine learning algorithms that do not assume any ordering among the values of the categorical variable.
"""
"""
Q5. In a machine learning project, you have a dataset with 1000 rows and 5 columns. Two of the columns are categorical, and the remaining three 
columns are numerical. If you were to use nominal encoding to transform the categorical data, how many new columns would be created? Show your 
calculations.
Ans:
the total number of new columns created by OHE encoding would be the sum of the number of unique categories in each of the categorical columns.
Let's say the first categorical column has 8 unique categories, and the second categorical column has 6 unique categories. Then the total number 
of new columns created by nominal encoding would be:

8 + 6 = 14
"""
"""
Q6. You are working with a dataset containing information about different types of animals, including their species, habitat, and diet. Which 
encoding technique would you use to transform the categorical data into a format suitable for machine learning algorithms? Justify your answer.
Ans:
The choice of encoding technique depends on the specific characteristics of the categorical data and the requirements of the machine learning 
algorithm. However, given the nature of the data and the fact that there are likely multiple unique values in each categorical variable, a 
combination of nominal encoding and one-hot encoding may be suitable to transform the categorical data into a format suitable for machine learning 
algorithms.

Nominal encoding could be used to convert the categorical data into a numerical format. This involves assigning a unique integer value to each 
unique category in the categorical variable. For example, each unique species could be assigned a unique integer value, and each unique habitat 
and diet could also be assigned unique integer values. This approach would allow machine learning algorithms to use the categorical data as input 
for training models and making predictions.

However, since the unique values within the categorical variables are not ordered, one-hot encoding could be used to further encode the nominal 
encoded features. This involves creating binary features for each unique category within a nominal encoded variable. For example, a binary feature 
could be created for each unique species, with a value of 1 indicating the presence of that species and a value of 0 indicating the absence of 
that species. This approach can help to reduce any biases that may be introduced by nominal encoding and allows the model to learn independently 
for each category.
"""
"""
Q7.You are working on a project that involves predicting customer churn for a telecommunications company. You have a dataset with 5 features, including the customer's gender, age, contract type, monthly charges, and tenure. Which encoding technique(s) would you use to transform the categorical data into numerical data? Provide a step-by-step explanation of how you would implement the encoding.

To transform the categorical data into numerical data, we can use nominal encoding for the "gender" and "contract type" features since they have a limited number of unique values. For the "gender" feature, we can assign the values 0 and 1 to represent "male" and "female," respectively. For the "contract type" feature, we can assign the values 0, 1, and 2 to represent "month-to-month," "one year," and "two year," respectively.

For the remaining features, we can leave them as numerical data since they already have numerical values.

Here are the steps to implement the encoding:

Load the dataset into a data frame.

Identify the categorical features, which are "gender" and "contract type."

Create a mapping dictionary to assign numerical values to the categories for each categorical feature. For example:

gender_mapping = {'Male': 0, 'Female': 1}
contract_mapping = {'Month-to-month': 0, 'One year': 1, 'Two year': 2}
Apply the mapping to the categorical features using the map() function. For example:
df['gender'] = df['gender'].map(gender_mapping)
df['contract type'] = df['contract type'].map(contract_mapping)

The resulting data frame will have the categorical features transformed into numerical data using nominal encoding.
"""