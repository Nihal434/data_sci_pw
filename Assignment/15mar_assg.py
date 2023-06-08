"""
Q1. Explain following with examples ?
1)Artificial Intelligence
2)Machine Learning
3)Deep Learning
Ans:
    1. Artificial Intelligence : Artificial intelligence involves replicating human intellectual processes through machines, especially computers.
    There are many applications of AI, such as expert systems, natural language processing, speech recognition, and machine vision.

    2. Machine Learning : Machine learning (ML) is a type of artificial intelligence (AI) that allows software applications to become more accurate
    at predicting outcomes without being explicitly programmed to do so. Machine learning algorithms use historical data as input to predict new output values.

    3. Deep Learning : Deep learning is a method in artificial intelligence (AI) that teaches computers to process data in a way that is inspired by
    the human brain. Deep learning models can recognize complex patterns in pictures, text, sounds, and other data to produce accurate insights and predictions

"""
"""
Q2. What is supervised learning? List some examples of supervised learning?
Ans:
    Supervised learning is an approach to creating artificial intelligence (AI), where a computer algorithm is trained on input data that has been labeled for a particular output.
    Some common examples of supervised learning include spam filters, fraud detection systems, recommendation engines, and image recognition systems.

"""

"""
Q2. What is unsupervised learning? List some examples of unsupervised learning?
Ans:
    Unsupervised learning is when it can provide a set of unlabelled data, which it is required to analyze and find patterns inside. The examples are dimension reduction and clustering.
"""
"""
Q4. What is the diference between AI, ML, DL, and DS?
Ans:
    AI (Artificial Intelligence) is a broad field of computer science that focuses on creating intelligent machines or systems that can perform tasks
    that typically require human intelligence. It encompasses various subfields and techniques, including machine learning, deep learning, and data
    science.

    ML (Machine Learning) is a subset of AI that involves the development of algorithms and statistical models that enable computers to learn and make
    predictions or decisions without being explicitly programmed. In machine learning, the system learns from patterns in data and improves its performance
    over time through experience.

    DL (Deep Learning) is a subfield of machine learning that specifically focuses on developing artificial neural networks, which are inspired by the
    structure and function of the human brain. Deep learning algorithms consist of multiple layers of interconnected nodes (neurons) that can learn
    hierarchical representations of data. It has proven to be particularly effective in areas such as image and speech recognition.

    DS (Data Science) is an interdisciplinary field that combines elements of statistics, mathematics, computer science, and domain knowledge to extract
    insights and knowledge from structured and unstructured data. Data scientists use various techniques and tools to collect, process, analyze, and 
    interpret large volumes of data to solve complex problems and make data-driven decisions.
"""
"""
Q5. What are the main difference between supervised ,unsupervised,and semi supervised learning ?
Ans:
    The main differences between supervised, unsupervised, and semi-supervised learning lie in the type of learning data available and the approach
    used to train machine learning models. Here's a breakdown of each:

    1. Supervised Learning:
    Supervised learning involves training a model using labeled data, where the input data is paired with corresponding target labels or outcomes. 
    The goal is for the model to learn the mapping between input data and output labels so that it can make accurate predictions or classifications for
    new, unseen data. Supervised learning requires a dataset with known outcomes to guide the learning process.

    2. Unsupervised Learning:
    Unsupervised learning, in contrast, deals with unlabeled data, where the input data does not have corresponding target labels. The objective of 
    unsupervised learning is to discover underlying patterns, structures, or relationships within the data without prior knowledge of the outcomes. 
    Clustering and dimensionality reduction techniques are commonly used in unsupervised learning to group similar data points or reduce the complexity of the data.

    3. Semi-Supervised Learning:
    Semi-supervised learning is a combination of both supervised and unsupervised learning approaches. It utilizes a small amount of labeled data and
    a larger amount of unlabeled data to train a model. The labeled data helps guide the learning process, while the unlabeled data allows the model 
    to learn additional patterns or information from the data distribution. Semi-supervised learning can be useful when obtaining labeled data is 
    expensive or time-consuming, as it allows leveraging the benefits of both labeled and unlabeled data.

    In summary, supervised learning uses labeled data with known outcomes, unsupervised learning deals with unlabeled data to find patterns, and 
    semi-supervised learning combines labeled and unlabeled data to train models. Each approach is suited for different types of problems and data 
    availability scenarios.
"""

"""
Q6. What is train, test and validation split? Explain thK importance of each term.
Ans:
    In machine learning, the train-test-validation split refers to the division of a dataset into separate subsets for training, evaluating, and 
    validating a machine learning model. Here's an explanation of each term and their importance:

    Training Set:
    The training set is the portion of the dataset used to train the machine learning model. It contains labeled examples where both the input data
    and their corresponding target labels are provided. During training, the model learns from these examples and adjusts its internal parameters 
    or weights to minimize the prediction errors. The training set is crucial as it directly influences the model's learning process and its ability
    to make accurate predictions.

    Test Set:
    The test set is used to evaluate the performance of the trained model. It contains examples that are distinct from the training set and are 
    labeled with the ground truth outcomes. After the model has been trained, it is applied to the test set, and its predictions are compared against 
    the true labels. This evaluation provides an estimate of how well the model generalizes to unseen data and gives an indication of its overall
    performance. The test set is important for assessing the model's effectiveness and identifying potential issues like overfitting or underfitting.

    Validation Set:
    The validation set is an optional subset used during the model development process to tune hyperparameters or perform model selection. 
    Hyperparameters are parameters that are set prior to the training process, such as learning rate or regularization strength, and they affect the 
    model's performance. By evaluating the model on the validation set, different hyperparameter configurations can be compared, and the best 
    performing ones can be selected. The validation set helps prevent overfitting on the test set and provides a way to fine-tune the model before 
    final evaluation.

"""

"""
Q7. How can unsupervised learning by used in anomaly detection ?
Ans:
    Unsupervised learning techniques are commonly used in anomaly detection, as they can help identify patterns and anomalies in data without the need
    for labeled examples. Here are some approaches to using unsupervised learning for anomaly detection:
    1. Clutering based anomaly detection
    2. Density based anomaly detection etc

"""
"""
Q8. List down some commonly used supervised learning algorithms and unsupervised learning algorithm.
Ans:
    Certainly! Here are some commonly used supervised and unsupervised learning algorithms:

Supervised Learning Algorithms:
1. Linear Regression
2. Logistic Regression
3. Decision Trees
4. Random Forests
5. Support Vector Machines (SVM)
6. Naive Bayes
7. K-Nearest Neighbors (KNN)
8. Gradient Boosting Algorithms (e.g., XGBoost, LightGBM)
9. Neural Networks (e.g., Multi-layer Perceptron)
10. Gaussian Processes

Unsupervised Learning Algorithms:
1. K-Means Clustering
2. DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
3. Hierarchical Clustering
4. Gaussian Mixture Models (GMM)
5. Principal Component Analysis (PCA)
6. t-SNE (t-Distributed Stochastic Neighbor Embedding)
7. Self-Organizing Maps (SOM)
8. Isolation Forest
9. Local Outlier Factor (LOF)
10. Association Rule Learning (e.g., Apriori, FP-Growth)


"""