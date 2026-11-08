#!/usr/bin/env python3
"""High school Statistics (TEKS 111.47.c). Original questions. Strand 1 (process) skipped."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from common import *

B = Bank('111.47.c.', 990, own='hs_stats.jsonl')
def H(code, d, q, right, wrong, e): return B.hand(code, d, q, right, wrong, e)

# 2.A sampling
H('2.A', 3, "In a simple random sample, how is each member of the population treated?", "each member has an equal chance of being chosen", ["the first members listed are chosen", "volunteers are chosen", "only convenient members are chosen"], "Random selection reduces bias.")
H('2.A', 3, "A researcher surveys only the people who walk past her office. What type of sample is this?", "a convenience sample", ["a simple random sample", "a stratified sample", "a census"], "It uses whoever is easy to reach.")
H('2.A', 4, "A school splits students by grade level and then randomly selects some from each grade. What is this called?", "stratified random sampling", ["cluster sampling", "convenience sampling", "voluntary response sampling"], "Groups (strata) are each sampled.")
H('2.A', 3, "Why is a voluntary response sample often biased?", "people with strong opinions are more likely to respond", ["everyone is chosen at random", "it samples the whole population", "it removes all variability"], "Self-selected responders are not representative.")

# 2.B study types
H('2.B', 3, "Which kind of study assigns treatments to subjects?", "an experiment", ["an observational study", "a census", "a survey"], "Researchers impose the treatment.")
H('2.B', 3, "A researcher records the habits of students without changing anything. What is this?", "an observational study", ["an experiment", "a placebo trial", "a simulation"], "No treatment is imposed.")
H('2.B', 3, "A poll asks 1,000 voters about a candidate. What type of study is this?", "a survey", ["an experiment", "an observational study of a treatment", "a double-blind trial"], "It gathers responses to questions.")

# 2.C generalizations
H('2.C', 4, "A well-designed experiment with random assignment can support which kind of conclusion?", "a cause-and-effect conclusion", ["only a correlation", "no conclusion", "a conclusion about the whole world"], "Random assignment controls for confounding.")
H('2.C', 4, "An observational study finds that ice cream sales and sunburns rise together. What is the best conclusion?", "no cause is shown; a lurking variable such as hot weather may explain both", ["ice cream causes sunburns", "sunburns cause ice cream sales", "the data must be wrong"], "Association does not prove causation.")
H('2.C', 4, "Results from a sample can be generalized to a population only if the sample was what?", "randomly selected and representative", ["very small", "chosen by volunteers", "chosen by the researcher"], "Random selection supports generalization.")

# 2.D statistics and parameters
H('2.D', 2, "A number that describes a sample is called what?", "a statistic", ["a parameter", "a population", "a census"], "Statistics describe samples.")
H('2.D', 2, "A number that describes an entire population is called what?", "a parameter", ["a statistic", "a sample", "a variable only"], "Parameters describe populations.")
H('2.D', 3, "In a poll, 52% of 400 sampled voters support a measure. What is the 52%?", "a sample statistic", ["a population parameter", "a margin of error", "a z-score"], "It comes from the sample.")

# 2.E data project
H('2.E', 3, "What is the first step in a statistical investigation?", "ask a question that can be answered with data", ["calculate the mean", "draw a graph", "choose a conclusion"], "Start by formulating a question.")
H('2.E', 3, "Which question can be answered using data?", "How many hours do students at our school sleep on weeknights?", ["Is math the best subject?", "Is blue the prettiest color?", "Should everyone like pizza?"], "It asks about measurable values.")
H('2.E', 3, "After collecting data, what comes before drawing conclusions?", "analyzing the data", ["asking the question again", "choosing a sample", "writing a title"], "The data must be summarized and examined.")

# 2.F communicating
H('2.F', 3, "When reporting a study, which detail should be included so others can judge it?", "how the sample was selected", ["the researcher's favorite color", "the day of the week it was written", "nothing about methods"], "Methods affect the reliability of results.")
H('2.F', 3, "A good conclusion in a data project should be tied to what?", "the data and analysis that were collected", ["opinion only", "guesses about other data", "the research question only"], "Claims must be supported by evidence.")
H('2.F', 3, "Which graph is best for showing the shape of the distribution of one quantitative variable?", "a histogram", ["a pie chart for categories", "a bar chart of names", "a scatterplot of two variables"], "A histogram shows the spread and shape.")

# 2.G critique
H('2.G', 4, "A news report says 'Coffee drinkers live longer' based on an observational study. What is a key concern?", "confounding variables may explain the result", ["the sample is too random", "the study is an experiment", "correlation always shows causation"], "Other factors may be involved.")
H('2.G', 4, "A survey about school lunches only asks students who buy lunch. What is the problem?", "undercoverage: students who bring lunch are missing", ["too many students were sampled", "the sample was random", "the question was too long"], "Part of the population is left out.")
H('2.G', 4, "A poll asks 'Don't you agree that the wonderful new park should be built?' What is the problem?", "the wording is leading and biases the responses", ["the sample is too large", "the poll is unbiased", "it is not a survey"], "Question wording can push answers.")

# 3.A mathematical vs statistical models
H('3.A', 3, "Which describes a mathematical (deterministic) model?", "the same inputs always give the same output", ["outputs vary randomly around a pattern", "it uses sample data only", "it cannot be graphed"], "There is no random variation.")
H('3.A', 3, "Which describes a statistical model?", "it describes a pattern and also the random variation around it", ["it gives exact outputs with no variation", "it ignores data", "it only works for one point"], "Real data vary.")
H('3.A', 3, "The equation d = 50t gives the distance driven at 50 mph. What kind of model is it?", "a mathematical model", ["a statistical model", "a sampling model", "a survey"], "It ignores traffic and other variation.")

# 3.B constructing a statistical model
H('3.B', 4, "A line of best fit predicts a plant's height from sunlight hours, but real plants scatter around it. What does the scatter represent?", "variability around the model", ["a mistake in the line", "a perfect fit", "a population parameter"], "Residuals show the variation not explained.")
H('3.B', 4, "In a statistical model y = a + bx + error, what does the error term represent?", "random variation not explained by x", ["the slope", "the intercept", "the sample size"], "It is the unexplained part.")
H('3.B', 3, "Why might a statistical model be better than a mathematical model for predicting test scores from study time?", "scores vary even when study time is the same", ["study time has no effect", "scores never vary", "math cannot be used"], "Individual differences create variation.")

# 3.C sources of variability
H('3.C', 3, "Different students having different heights is an example of what kind of variability?", "natural variability", ["measurement variability", "induced variability", "sampling variability"], "It occurs in nature.")
H('3.C', 3, "Slightly different readings from a scale when weighing the same object are an example of what?", "measurement variability", ["natural variability", "induced variability", "sampling variability"], "The measuring process is imperfect.")
H('3.C', 4, "Different random samples from the same population give slightly different means. What is this called?", "sampling variability", ["measurement variability", "induced variability", "natural variability only"], "Each sample differs by chance.")
H('3.C', 3, "A researcher changes the fertilizer given to plants and sees growth change. What kind of variability is this?", "induced variability", ["natural variability", "measurement variability", "sampling variability"], "The researcher caused the change.")

# 3.D population and sampling distributions
H('3.D', 3, "What is a sampling distribution?", "the distribution of a statistic over many samples", ["the distribution of one sample only", "a list of all populations", "a graph of one individual"], "It shows how a statistic varies across samples.")
H('3.D', 4, "As the sample size increases, what happens to the spread of the sampling distribution of the mean?", "it decreases", ["it increases", "it stays the same", "it becomes uniform"], "The standard error is σ ÷ √n.")
H('3.D', 4, "The standard deviation of a population is 20. What is the standard error of the mean for samples of size 100?", "2", ["20", "0.2", "200"], "20 ÷ √100.")

# 4.A categorical vs quantitative
H('4.A', 2, "Which variable is categorical?", "eye color", ["height in inches", "age in years", "weight in pounds"], "It places individuals into groups.")
H('4.A', 2, "Which variable is quantitative?", "number of siblings", ["favorite color", "type of pet", "zip code label as a category"], "It is a count with numerical meaning.")
H('4.A', 3, "A survey asks for a student's grade level (9, 10, 11 or 12). How can this variable be treated?", "as categorical, since averages of labels are not meaningful here", ["as a continuous measurement only", "as a proportion", "as a z-score"], "The numbers act as labels for groups.")

# 4.B representing data
H('4.B', 3, "Which graph is best for comparing the percentage of students choosing each of four lunch options?", "a bar graph", ["a histogram of heights", "a scatterplot", "a boxplot of one variable"], "Bar graphs display categorical data.")
H('4.B', 3, "Which graph shows the five-number summary of a data set?", "a boxplot", ["a pie chart", "a bar graph", "a scatterplot"], "It shows min, Q1, median, Q3 and max.")
H('4.B', 3, "A dot plot is best used for what?", "small sets of quantitative data", ["very large sets of categories", "two-variable relationships", "time only"], "Each dot is one data value.")

# 4.C distribution characteristics
H('4.C', 3, "A distribution has a long tail to the right. What is its shape?", "skewed right", ["skewed left", "symmetric", "uniform"], "The tail points toward higher values.")
H('4.C', 3, "In a right-skewed distribution, how does the mean compare with the median?", "the mean is greater than the median", ["the mean is less than the median", "they are equal", "the mean cannot be found"], "The tail pulls the mean up.")
H('4.C', 4, "A data value is flagged as an outlier if it is more than how many IQRs beyond the quartiles?", "1.5", ["0.5", "3", "5"], "The 1.5 × IQR rule.")
H('4.C', 3, "Which statistic is resistant to outliers?", "the median", ["the mean", "the standard deviation", "the range"], "Extreme values barely change it.")

# 4.D compare representations
H('4.D', 3, "Which graph best shows the individual values in a small data set?", "a dot plot", ["a pie chart", "a box plot", "a bar graph of counts"], "Each value is visible.")
H('4.D', 4, "A boxplot and a histogram are made from the same data. Which shows the shape in more detail?", "the histogram", ["the boxplot", "neither", "both show exactly the same"], "Boxplots hide gaps and peaks.")
H('4.D', 3, "What does a boxplot show well that a bar graph of means does not?", "the spread of the data", ["the exact population", "the sample size only", "the cause of variation"], "Quartiles show variability.")

# 4.E summary statistics
H('4.E', 3, "Two data sets have the same mean but different standard deviations. What does that tell us?", "the set with the larger standard deviation is more spread out", ["the sets are identical", "the set with the larger standard deviation is more centered", "the medians must differ"], "Standard deviation measures spread.")
H('4.E', 3, "What is the mean of 2, 4, 6, 8?", "5", ["4", "6", "20"], "20 ÷ 4.")
H('4.E', 3, "What is the median of 3, 5, 7, 9, 11, 13?", "8", ["7", "9", "6"], "The average of the middle values, 7 and 9.")
H('4.E', 4, "For the data 10, 12, 14, 16, 18, what is the range?", "8", ["18", "14", "4"], "18 − 10.")

# 4.F two-way tables
H('4.F', 3, "In a two-way table, what is a marginal distribution?", "the totals for one variable alone", ["the intersection of both variables", "the mean of the table", "the standard deviation"], "It is found in the margins.")
H('4.F', 4, "In a two-way table, 20 of 80 students who play sports are seniors. What is the conditional relative frequency of seniors among athletes?", "25%", ["20%", "75%", "4%"], "20 ÷ 80.")
H('4.F', 3, "What does a two-way table display?", "the relationship between two categorical variables", ["the shape of one quantitative variable", "the mean of two groups", "the slope of a line"], "Categories are cross-classified.")

# 5.A probability
H('5.A', 2, "A fair six-sided die is rolled. What is P(rolling an even number)?", "1/2", ["1/3", "1/6", "2/3"], "3 of 6 outcomes.")
H('5.A', 3, "A bag has 3 red and 7 blue marbles. What is the probability of drawing a red marble?", "3/10", ["7/10", "3/7", "1/3"], "3 of 10 marbles are red.")
H('5.A', 3, "P(A) = 0.4 and P(B) = 0.3, and A and B are independent. What is P(A and B)?", "0.12", ["0.7", "0.1", "0.35"], "Multiply for independent events.")
H('5.A', 4, "P(A) = 0.5, P(B) = 0.4 and P(A and B) = 0.2. What is P(A or B)?", "0.7", ["0.9", "0.2", "0.45"], "0.5 + 0.4 − 0.2.")

# 5.B law of large numbers
H('5.B', 3, "According to the Law of Large Numbers, as the number of trials increases, what happens to the experimental probability?", "it gets closer to the theoretical probability", ["it moves away from the theoretical probability", "it always equals 1/2", "it stops changing at the start"], "Long-run relative frequency approaches the true value.")
H('5.B', 3, "A coin lands heads 6 times in 10 flips and 5,010 times in 10,000 flips. Which is closer to the theoretical value?", "the 10,000 flips", ["the 10 flips", "they are equally close", "neither is related"], "More trials give a better estimate.")
H('5.B', 3, "A fair coin has landed heads five times in a row. What is the probability of heads on the next flip?", "1/2", ["less than 1/2", "more than 1/2", "0"], "Flips are independent.")

# 5.C simulation distribution
H('5.C', 4, "A simulation tosses a coin 10 times and counts heads, repeated many times. What does the distribution of the counts represent?", "the distribution of the number of heads", ["the population mean", "a census", "a single trial"], "Each repeat yields one count.")
H('5.C', 3, "Why is simulation useful in statistics?", "it estimates probabilities that are hard to calculate exactly", ["it gives exact answers every time", "it removes randomness", "it replaces all data"], "Repeated trials approximate the true distribution.")
H('5.C', 3, "If 38 out of 100 simulated trials produce a success, what is the estimated probability?", "0.38", ["0.62", "38", "3.8"], "Relative frequency.")

# 5.D compare simulation to theory
H('5.D', 4, "A simulation of 1,000 samples gives a sample mean of 49.8 while the population mean is 50. What does this suggest?", "the simulation is close to the true value", ["the simulation is wrong", "the population mean is 49.8", "the standard deviation is zero"], "Small differences are expected.")
H('5.D', 4, "When comparing a simulated standard deviation to a theoretical one, what do you expect with more repetitions?", "closer agreement", ["greater disagreement", "no change", "a different mean"], "More repetitions reduce simulation error.")
H('5.D', 3, "A theoretical mean of a distribution is 10. A simulation gives 10.2. What explains the difference?", "random variation in the simulation", ["the theory is wrong", "the simulation is impossible", "the mean is undefined"], "Simulated results vary by chance.")

# 6.A confidence intervals
H('6.A', 3, "A confidence interval is built from a sample statistic and what?", "a margin of error", ["a population parameter", "the sample's median only", "a random digit"], "Interval = statistic ± margin of error.")
H('6.A', 3, "What does a 95% confidence level mean?", "about 95% of intervals constructed this way capture the true parameter", ["there is a 95% chance the sample is correct", "95% of the data are in the interval", "the parameter changes 95% of the time"], "It describes the long-run success rate.")
H('6.A', 3, "A sample mean is 50 with a margin of error of 4. What is the confidence interval?", "(46, 54)", ["(44, 56)", "(50, 54)", "(48, 52)"], "50 − 4 to 50 + 4.")

# 6.B margin of error factors
H('6.B', 3, "If the sample size increases and other things stay the same, what happens to the margin of error?", "it decreases", ["it increases", "it stays the same", "it becomes zero"], "More data give more precision.")
H('6.B', 3, "If the confidence level increases from 90% to 99%, what happens to the margin of error?", "it increases", ["it decreases", "it stays the same", "it is zero"], "A wider interval is needed for more confidence.")
H('6.B', 4, "If the population standard deviation increases, what happens to the margin of error?", "it increases", ["it decreases", "it stays the same", "it becomes negative"], "More variability means less precision.")

# 6.C CI for mean
H('6.C', 4, "A sample of 100 has mean 80 and population σ = 10. What is the standard error of the mean?", "1", ["10", "0.1", "100"], "σ ÷ √n.")
H('6.C', 4, "Using z* = 2 for roughly 95% confidence, a sample mean is 80 with standard error 1. What is the interval?", "(78, 82)", ["(79, 81)", "(70, 90)", "(80, 82)"], "80 ± 2(1).")
H('6.C', 4, "Which z* value is closest to 95% confidence for a normal distribution?", "1.96", ["1.28", "2.58", "0.95"], "The middle 95% lies within about 1.96 standard errors.")

# 6.D CI for proportion
H('6.D', 4, "In a sample of 100 voters, 60 support a measure. What is the sample proportion?", "0.60", ["0.40", "60", "0.06"], "60 ÷ 100.")
H('6.D', 4, "What is the standard error of p̂ = 0.6 when n = 100?", "about 0.049", ["about 0.6", "about 0.4", "about 0.5"], "√(0.6 × 0.4 ÷ 100).")
H('6.D', 4, "Which interval is a 95% confidence interval for a proportion when p̂ = 0.60 and the margin of error is 0.096?", "(0.504, 0.696)", ["(0.404, 0.796)", "(0.6, 0.696)", "(0.5, 0.7)"], "p̂ ± margin of error.")

# 6.E interpreting CIs
H('6.E', 3, "A 95% confidence interval for a mean is (10, 14). Which interpretation is correct?", "we are 95% confident the true mean is between 10 and 14", ["95% of the data are between 10 and 14", "the sample mean is between 10 and 14 with 95% probability", "the true mean is 12 with 95% probability"], "It is a statement about the parameter.")
H('6.E', 4, "A confidence interval for a difference in means is (−2, 5). What does this suggest?", "zero is a plausible difference", ["the means are definitely different", "the means are definitely equal", "the interval is invalid"], "The interval includes 0.")
H('6.E', 4, "Two confidence intervals for a proportion, (0.40, 0.50) and (0.55, 0.65), do not overlap. What does this suggest?", "the two population proportions are probably different", ["the proportions are the same", "the intervals are wrong", "the sample sizes are equal"], "No plausible common value.")

# 6.F evidence against a claim
H('6.F', 3, "A coin lands heads 90 out of 100 times. What does this suggest about the claim that the coin is fair?", "it provides evidence against the claim", ["it supports the claim", "it proves the claim", "it means nothing"], "Such a result is very unlikely if p = 0.5.")
H('6.F', 4, "A claim is tested using a sample statistic. Why might the statistic differ from the claimed value even if the claim is true?", "sampling variability", ["the claim is false", "measurement is impossible", "the population has no mean"], "Samples vary by chance.")
H('6.F', 4, "When a sample result would be very unlikely if the claim were true, what do we conclude?", "the claim is questionable", ["the claim is true", "the sample is wrong", "no conclusion is possible"], "Unlikely outcomes are evidence against it.")

# 6.G hypotheses
H('6.G', 3, "A company claims the mean battery life is 20 hours. Which is the null hypothesis?", "H₀: μ = 20", ["H₀: μ ≠ 20", "H₀: μ > 20", "H₀: x̄ = 20"], "The null states no change.")
H('6.G', 3, "You want to test whether a new teaching method raises the mean score above 70. What is the alternative hypothesis?", "Hₐ: μ > 70", ["Hₐ: μ = 70", "Hₐ: μ < 70", "Hₐ: μ ≠ 70"], "The research claim is the alternative.")
H('6.G', 3, "Hypotheses are statements about what?", "population parameters", ["sample statistics", "the sample size", "the p-value"], "They concern the population, not the sample.")

# 6.H p-value
H('6.H', 4, "What does the p-value measure?", "the probability of a result at least as extreme as observed, if H₀ is true", ["the probability that H₀ is true", "the probability that Hₐ is true", "the sample size"], "It assumes the null is true.")
H('6.H', 3, "At α = 0.05, a test gives p = 0.02. What is the decision?", "reject H₀", ["fail to reject H₀", "accept H₀", "the test is invalid"], "p is less than α.")
H('6.H', 3, "At α = 0.05, a test gives p = 0.30. What is the decision?", "fail to reject H₀", ["reject H₀", "accept Hₐ", "the p-value is wrong"], "The evidence is not strong enough.")
H('6.H', 4, "A smaller p-value provides what kind of evidence against H₀?", "stronger evidence", ["weaker evidence", "no evidence", "evidence for H₀"], "The result is less compatible with the null.")

# 6.I technology results
H('6.I', 4, "A technology output for a one-sample t test shows t = 2.5 and p = 0.015. At α = 0.05, what do we conclude?", "there is significant evidence against H₀", ["there is not significant evidence against H₀", "H₀ is proven true", "the test cannot be used"], "p < α.")
H('6.I', 4, "A large sample is required for which kind of test?", "a z test for a proportion using a normal approximation", ["any test", "no test", "a test of a single data point"], "Conditions such as np and n(1 − p) being large must hold.")
H('6.I', 4, "A technology output reports a 95% confidence interval for μ of (4.1, 5.9) and a test of H₀: μ = 4 gives p = 0.04. Are these consistent?", "yes, 4 is just outside the interval and p < 0.05", ["no, they contradict", "yes, because p = 0.04 means 4 is inside the interval", "no, because the interval is too wide"], "A value outside a 95% interval is rejected at α = 0.05.")

# 6.J Type I and II
H('6.J', 3, "What is a Type I error?", "rejecting a true null hypothesis", ["failing to reject a false null hypothesis", "rejecting a false null hypothesis", "failing to reject a true null hypothesis"], "A false positive.")
H('6.J', 3, "What is a Type II error?", "failing to reject a false null hypothesis", ["rejecting a true null hypothesis", "rejecting a false null hypothesis", "failing to reject a true null hypothesis"], "A false negative.")
H('6.J', 4, "The significance level α equals the probability of what?", "a Type I error", ["a Type II error", "a correct decision", "the power of the test"], "α is the chance of rejecting a true null.")
H('6.J', 4, "In a medical test for a disease, a false positive result corresponds to which error?", "Type I error", ["Type II error", "no error", "sampling error only"], "The test says the disease is present when it is not.")

# 7.A scatterplots
H('7.A', 3, "A scatterplot shows points rising from left to right in a tight line. How would you describe the association?", "strong positive linear", ["weak negative", "strong negative linear", "no association"], "Both variables increase together.")
H('7.A', 3, "What does an outlier in a scatterplot look like?", "a point far from the overall pattern", ["a point on the line", "the mean point", "a cluster"], "It does not fit the trend.")
H('7.A', 4, "An influential point in a scatterplot is one that does what?", "greatly changes the regression line when removed", ["lies exactly on the line", "is the mean point", "has no effect"], "Its removal shifts the fit.")
H('7.A', 3, "Points on a scatterplot curve upward like a bowl. Is a linear model appropriate?", "no, the pattern is not linear", ["yes, always", "yes, if r is positive", "yes, for outliers"], "A curved pattern needs a different model.")

# 7.B line of best fit
H('7.B', 3, "A line of best fit has slope 2.5 and y-intercept 10. Which equation is it?", "ŷ = 10 + 2.5x", ["ŷ = 2.5 + 10x", "ŷ = 10x", "ŷ = 2.5x − 10"], "ŷ = intercept + slope · x.")
H('7.B', 3, "For ŷ = 3 + 2x, what is the predicted y when x = 5?", "13", ["10", "8", "15"], "3 + 2(5).")
H('7.B', 4, "In a model for height (cm) predicted from age, the slope is 6. What does that mean?", "height is predicted to increase 6 cm per year of age", ["height is 6 cm at age 0", "age increases 6 years per cm", "there is no relationship"], "The slope is change in y per unit x.")

# 7.C comparing models
H('7.C', 3, "Which measure tells how well a linear model explains variation in y?", "r², the coefficient of determination", ["the mean of y", "the range", "the sample size"], "r² is the proportion of variation explained.")
H('7.C', 4, "Two linear models have r² = 0.45 and r² = 0.82. Which fits better?", "the model with r² = 0.82", ["the model with r² = 0.45", "they fit equally", "neither can be compared"], "Higher r² means more variation explained.")
H('7.C', 4, "A residual plot with a clear curved pattern suggests what?", "a linear model is not appropriate", ["the linear model is perfect", "the data are random", "the residuals are zero"], "A good linear fit has residuals scattered randomly.")

# 7.D median-median, absolute value
H('7.D', 4, "Compared with least squares, how is the median-median line affected by outliers?", "it is less affected", ["it is more affected", "it is equally affected", "it ignores all data"], "Medians resist extreme values.")
H('7.D', 4, "A least-squares line minimizes the sum of what?", "the squared residuals", ["the absolute values of x", "the products of residuals", "the data values"], "That is the least-squares criterion.")
H('7.D', 4, "A line fit by minimizing the sum of absolute residuals is generally less sensitive to what?", "outliers", ["the sample size", "the slope", "the units"], "Absolute values do not square large residuals.")

# 7.E influential points
H('7.E', 4, "A point far to the right of the other data in a scatterplot, away from the line, is likely to do what to the regression line?", "pull the line toward it", ["leave the line unchanged", "make the slope zero", "remove the intercept"], "High-leverage points have strong influence.")
H('7.E', 4, "Removing an influential point from a data set leads to what?", "a noticeably different line of best fit", ["the same line of best fit", "r² staying the same", "no residuals"], "That is why the point is influential.")
H('7.E', 3, "Using dynamic graphing technology, you drag one point and the line moves a lot. What does this show?", "that point is influential", ["the data are exact", "the line is perfect", "the correlation is zero"], "The fit depends strongly on it.")

# 7.F interpret attributes
H('7.F', 4, "A model predicts a car's value from age. The y-intercept is $25,000. What does this represent?", "the predicted value of a car at age 0", ["the value after 25 years", "the yearly loss", "the car's color"], "The intercept is the predicted y at x = 0.")
H('7.F', 4, "A model predicts weight from height. Predicting a weight for a height far outside the data range is called what?", "extrapolation", ["interpolation", "residual analysis", "sampling"], "Predictions outside the data range are risky.")
H('7.F', 3, "The correlation coefficient r = −0.9. What does this indicate?", "a strong negative linear relationship", ["a weak positive relationship", "no relationship", "a strong positive relationship"], "The sign shows the direction and the size shows the strength.")
H('7.F', 3, "A residual is defined as what?", "the observed y minus the predicted y", ["the predicted y minus the observed y", "the slope times x", "the mean of y"], "residual = y − ŷ.")

B.balance()
B.save(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'batches', 'hs_stats.jsonl'))
