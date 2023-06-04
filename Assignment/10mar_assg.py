"""
Q1: What is Estimation Statistics? Explain point estimate and interval estimate.
Ans:
    A point estimate is a single value estimate of a parameter. For instance, a sample mean is a point estimate of a population mean. 
    An interval estimate gives you a range of values where the parameter is expected to lie. A confidence interval is the most common type of 
    interval estimate.
"""

"""
Q2. Write a Python function to estimate the population mean using a sample mean and standard
deviation.
Ans:
    import numpy as np
    dataset = np.array([2, 3, 4, 1, 2, 5])
    sd = np.std(dataset)
    _mean = np.mean(dataset)
    print("Population standard deviation of the dataset is", sd)
    print("Population standard deviation of the dataset is", _mean)
"""

"""
Q3: What is Hypothesis testing? Why is it used? State the importance of Hypothesis testing.
Ans:
    Hypothesis testing allows the researcher to determine whether the data from the sample is statistically significant. Hypothesis 
    testing is one of the most important processes for measuring the validity and reliability of outcomes in any systematic investigation.
"""

"""
Q4. Create a hypothesis that states whether the average weight of male college students is greater than
the average weight of female college students.
Ans:
    (Null Hypothesis)H0 : μ = average weight of male college students is greater than
    the average weight of female college students
    (Alternate Hypothesis)Ha : μ ≠ average weight of male college students is greater than
    the average weight of female college students
"""

"""
Q5. Write a Python script to conduct a hypothesis test on the difference between two population means,
given a sample from each population.
Ans:
    The hypotheses for a difference in two population means are similar to those for a difference in two population proportions. The null hypothesis, H0, is again a statement of “no effect” or “no difference.”

    H0: μ1-μ2 = 0, which is the same as H0: μ1 = μ2

    The alternative hypothesis, Ha, can be any one of the following.

    Ha: μ1-μ2 < 0, which is the same as Ha: μ1 < μ2
    Ha: μ1-μ2 > 0, which is the same as Ha: μ1 > μ2
    Ha: μ1-μ2 ≠ 0, which is the same as Ha: μ1 ≠ μ2
    
    here μ1=mean if data1 and μ2=mean of data 2
    import numpy as np
    data1 = np.array([2, 3, 4, 1, 2, 5])
    data2 = np.array([2, 3, 0, 1, 2, 5])
    mean1 = np.mean(data1)
    mean2 = np.mean(data2)
    if (mean1==mean2):
        print("Null Hypothesis accepted")
    else:
        print("Null Hypothesis rejected")
"""

"""
Q6: What is a null and alternative hypothesis? Give some examples.
Ans:
    The null hypothesis is the one to be tested and the alternative is everything else. 
    In our example: The null hypothesis would be: The mean data scientist salary is 113,000 dollars. 
    While the alternative: The mean data scientist salary is not 113,000 dollars.
"""

"""
Q7: Write down the steps involved in hypothesis testing.
Ans:
    Step 1: State your null and alternate hypothesis. ...
    Step 2: Collect data. ...
    Step 3: Perform a statistical test. ...
    Step 4: Decide whether to reject or fail to reject your null hypothesis. ...
    Step 5: Present your findings.
"""

"""
Q8. Define p-value and explain its significance in hypothesis testing.
Ans:
    The p value is a number, calculated from a statistical test, that describes how likely you are to have found a particular set of 
    observations if the null hypothesis were true. P values are used in hypothesis testing to help decide whether to reject the null hypothesis
"""

"""
Q9. Generate a Student's t-distribution plot using Python's matplotlib library, with the degrees of freedom
parameter set to 10.
Ans:
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import stats
    x = np.arange(-4,4,0.1)
    firstT = stats.t.pdf(x,10)
    plt.plot(x, firstT)
"""

"""
Q10. Write a Python program to calculate the two-sample t-test for independent samples, given two
random samples of equal size and a null hypothesis that the population means are equal.
Ans:
    import numpy as np
    import scipy.stats as stats
    group1 = np.array([14, 15, 15, 16, 13, 8, 14, 17, 16, 14, 19, 20, 21, 15, 15, 16, 16, 13, 14, 12])
    group2 = np.array([15, 17, 14, 17, 14, 8, 12, 19, 19, 14, 17, 22, 24, 16, 13, 16, 13, 18, 15, 13])
    import scipy.stats as stats
    stats.ttest_ind(a=group1, b=group2, equal_var=True)
"""

"""
Q11: What is Student’s t distribution? When to use the t-Distribution.
Ans:
    The t-distribution, also known as the Student's t-distribution, is a type of probability distribution that is similar to the normal 
    distribution with its bell shape but has heavier tails.It is used for estimating population parameters for small sample sizes or unknown variances.
"""
"""
Q12: What is t-statistic? State the formula for t-statistic.
Ans:
    In statistics, the t-statistic is the ratio of the departure of the estimated value of a parameter from its hypothesized value to its standard error. It is used 
    in hypothesis testing via Student's t-test. The t-statistic is used in a t-test to determine whether to support or reject the null hypothesis.
    You can calculate a t-value using a common t-test with the formula: t = (X‾ - μ0) / (s / √n), where X‾ is the sample mean, μ0 represents the population mean, 
    s is the standard deviation of the sample and n stands for the size of the sample.
"""
"""
Q13. A coffee shop owner wants to estimate the average daily revenue for their shop. They take a random
sample of 50 days and find the sample mean revenue to be $500 with a standard deviation of $50.
Estimate the population mean revenue with a 95% confidence interval.
Ans:
    s=standard deviation
    x_bar = sample mean = 500
    For confidence level 95%, c-level=0.95
    so (c-level)/2=0.4750
    zα/2 (z-alpha by two)= 1.96
    Thus
    population mean = x_bar ± (zα∕2) * s/√n=500 ± 1.96(50/√50)=500 ± 13.85

"""

"""
Q14. A researcher hypothesizes that a new drug will decrease blood pressure by 10 mmHg. They conduct a
clinical trial with 100 patients and find that the sample mean decrease in blood pressure is 8 mmHg with a
standard deviation of 3 mmHg. Test the hypothesis with a significance level of 0.05.
Ans:

Null hypothesis – H0 : μ = 10
Alternative hypothesis – Ha: μ ≠ 10
Z = (x̅ – μ0) / (σ /√n)

Here, x̅ is the sample mean;
μ0 is the population mean;
σ is the standard deviation;
n is the sample size.

z= (10-8)/(3/√100)
z=2/0.3
z= 6.66

significance level = 0.05
z-score for 0.05 significance level is 1.95
and calculated z value is 6.66
The value of z is 6.66667. The value of p is < .00001. The result is significant at p < .05.

"""

"""
Q15. An electronics company produces a certain type of product with a mean weight of 5 pounds and a
standard deviation of 0.5 pounds. A random sample of 25 products is taken, and the sample mean weight
is found to be 4.8 pounds. Test the hypothesis that the true mean weight of the products is less than 5
pounds with a significance level of 0.01.

Ans:
Null hypothesis – H0 : μ = true mean weight of the products is less than 5 pounds
Alternative hypothesis – Ha: μ ≠ true mean weight of the products is less than 5 pounds
Z = (x̅ – μ0) / (σ /√n)

Here, x̅ is the sample mean;
μ0 is the population mean;
σ is the standard deviation;
n is the sample size.
z= (5-4.8)/(0.5/√25)
Z = 0.63246
The value of z is 0.63246. The value of p is .26435. The result is not significant at p < .01.

"""
"""
Q16. Two groups of students are given different study materials to prepare for a test. The first group (n1 =
30) has a mean score of 80 with a standard deviation of 10, and the second group (n2 = 40) has a mean
score of 75 with a standard deviation of 8. Test the hypothesis that the population means for the two
groups are equal with a significance level of 0.01.

Ans:
t = (x1_bar-x2_bar)/sqrt{[(s1)^2/n1]+[(s2)^2/n2]}

t = Student's t-test
x1 = mean of first group
x2 = mean of second group
s1= standard deviation of group 1
s2= standard deviation of group 1
n1= number of observations in group 1
n2= number of observations in group 

t = (80-75)/sqrt{[(10)^2/30]+[(8)^2/40]}
df = 54
standard error of difference = 2.221
The two-tailed P value equals 0.0285
By conventional criteria, this difference is considered to be statistically significant.
 
"""
"""
Q17. A marketing company wants to estimate the average number of ads watched by viewers during a TV
program. They take a random sample of 50 viewers and find that the sample mean is 4 with a standard
deviation of 1.5. Estimate the population mean with a 99% confidence interval.
Ans:

    s=standard deviation
    x_bar = sample mean = 500
    For confidence level 95%, c-level=0.99
    so (c-level)/2=0.495
    zα/2 (z-alpha by two)= 0.00
    Thus
    population mean = x_bar ± (zα∕2) * s/√n = 4 ± (0)*1.5/50 = 4 

"""