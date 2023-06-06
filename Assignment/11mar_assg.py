"""
Q1: What is the difference between a t-test and a z-test? Provide an example scenario where you would
use each type of test.
Ans:    
    A z-test is used to test a Null Hypothesis if the population variance is known, or if the sample size is larger than 30, 
    for an unknown population variance. A t-test is used when the sample size is less than 30 and the population variance is unknown.
"""

"""
Q2: Differentiate between one-tailed and two-tailed tests.
Ans:
    The main difference between one-tailed and two-tailed tests is that one-tailed tests will only have one critical region whereas two-tailed tests will have two critical regions. 
    If we require a 100(1−α) 100 ( 1 − α ) % confidence interval we have to make some adjustments when using a two-tailed test.
"""

"""
Q3: Explain the concept of Type 1 and Type 2 errors in hypothesis testing. Provide an example scenario for
each type of error.
Ans:
    A Type I error means rejecting the null hypothesis when it’s actually true. It means concluding that results are statistically significant when, 
    in reality, they came about purely by chance or because of unrelated factors.
    A Type II error means not rejecting the null hypothesis when it’s actually false. This is not quite the same as “accepting” the null hypothesis, 
    because hypothesis testing can only tell you whether to reject the null hypothesis.
    You decide to get tested for COVID-19 based on mild symptoms. There are two errors that could potentially occur:
    Type I error (false positive): the test result says you have coronavirus, but you actually don’t.
    Type II error (false negative): the test result says you don’t have coronavirus, but you actually do.

"""
"""
Q4: Explain Bayes's theorem with an example.
Ans:
    Bayes theorem gives the probability of an “event” with the given information on “tests”. There is a difference between “events” and “tests”. For example there is a test for liver disease,
    which is different from actually having the liver disease, i.e. an event. Rare events might be having a higher false positive rate.
"""

"""
Q5: What is a confidence interval? How to calculate the confidence interval, explain with an example.
Ans:
    Confidence, in statistics, is another way to describe probability. For example, if you construct a confidence interval with a 95% confidence level, you are confident that 95 out of 100 times 
    the estimate will fall between the upper and lower values specified by the confidence interval
"""
"""
Q6. Use Bayes' Theorem to calculate the probability of an event occurring given prior knowledge of the
event's probability and new evidence. Provide a sample problem and solution.
Ans:
   Bayes theorem calculates the probability based on the hypothesis. Now, let us state and prove Bayes Theorem. Bayes rule states that the conditional probability of an event A, 
   given the occurrence of another event B, is equal to the product of the likelihood of B, given A and the probability of A divided by the probability of B. It is given as: 
    P(A/B) = [P(A)*P(B/A)]/P(B)
    Here, P(A) = how likely A happens(Prior knowledge)- The probability of a hypothesis is true before any evidence is present.
    P(B) = how likely B happens(Marginalization)- The probability of observing the evidence.
    P(A|B) = how likely A happens given that B has happened(Posterior)-The probability of a hypothesis is true given the evidence.
    P(B|A) = how likely B happens given that A has happened(Likelihood)- The probability of seeing the evidence if the hypothesis is true
"""

"""
Q7. Calculate the 95% confidence interval for a sample of data with a mean of 50 and a standard deviation
of 5. Interpret the results.
Ans:
    s=standard deviation = 5
    x_bar = sample mean = 50
    For confidence level 95%, c-level=0.95
    so (c-level)/2=0.4750
    zα/2 (z-alpha by two)= 1.96
    Thus
    population mean = x_bar ± (zα∕2) * s/√n=50 ± 1.96(5/√n)
"""
"""
Q8. What is the margin of error in a confidence interval? How does sample size affect the margin of error?
Provide an example of a scenario where a larger sample size would result in a smaller margin of error.
Ans:
    Margin of error, also called confidence interval, tells you how much you can expect your survey results to reflect the views from the overall population.
    Margin of error is the percentage of the population that is contained within the confidence interval.
    As sample size increases, the margin of error decreases. As the variability in the population increases, the margin of error increases. As the confidence level increases, 
    the margin of error increases.
    Each time you survey one more person, the cost of your survey increases, and going from a sample size of, say, 1,500 to a sample size of 2,000 decreases your margin of error
    by only 0.34% (one third of one percent!)
"""

"""
Q9. Calculate the z-score for a data point with a value of 75, a population mean of 70, and a population
standard deviation of 5. Interpret the results.
Ans:
    z-score = (datapoint-mean)/standard deviation
            =(75-70)/5
    z-score =1
"""
"""
Q10. In a study of the effectiveness of a new weight loss drug, a sample of 50 participants lost an average
of 6 pounds with a standard deviation of 2.5 pounds. Conduct a hypothesis test to determine if the drug is
significantly effective at a 95% confidence level using a t-test.
Ans:
    null hypothesis = the drug is significantly effective
    alternate hypothesis ≠ the drug is significantly effective
    t=mean/(std/root of n)
    =6/(2.5/√50)
    t-score=16.97
"""
"""
Q11. In a survey of 500 people, 65% reported being satisfied with their current job. Calculate the 95%
confidence interval for the true proportion of people who are satisfied with their job.
Ans:

"""
"""
Q12. A researcher is testing the effectiveness of two different teaching methods on student performance.
Sample A has a mean score of 85 with a standard deviation of 6, while sample B has a mean score of 82
with a standard deviation of 5. Conduct a hypothesis test to determine if the two teaching methods have a
significant difference in student performance using a t-test with a significance level of 0.01.
Ans:
    t = (x1_bar-x2_bar)/sqrt{[(s1)^2/n1]+[(s2)^2/n2]}

    t = Student's t-test
    x1 = mean of first group
    x2 = mean of second group
    s1= standard deviation of group 1
    s2= standard deviation of group 1
    n1= number of observations in group 1
    n2= number of observations in group 

    t = (85-82)/sqrt{[(6)^2/n1]+[(5)^2/n2]}
"""

"""

"""