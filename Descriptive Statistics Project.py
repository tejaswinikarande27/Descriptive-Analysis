#!/usr/bin/env python
# coding: utf-8

# # Descriptive Statistics with Python Project
# 
# 
# **Descriptive Statistics** is the subject matter of this project. Descriptive statistics gives us the basic summary measures about the dataset.  The summary measures include measures of central tendency (mean, median and mode) and measures of variability (variance, standard deviation, minimum/maximum values, IQR (Interquartile Range), skewness and kurtosis). I have used the fortune 500 dataset from the data world website for this project.

# ## Table of Contents
# 
# 
# 1.	Introduction to descriptive statistics
# 
# 2.	Measures of central tendency
#     -	Mean
#     
#     -	Median
#     
#     -	Mode
#     
#     
# 3.	Measures of dispersion
#     -	Variance
#     
#     -	Standard deviation
#     
#     -	Coefficient of variation
#     
#     -	IQR (Interquartile range)
#     
#     -	Skewness
#     
#     -	Kurtosis
#     
#     
# 4.	Dataset description
# 
# 5.	Import libraries
# 
# 6.	Import dataset
# 
# 7.	Exploratory data analysis
# 
# 8.	Descriptive statistics with `describe()` function
#     -	Summary statistics of numerical columns
#     
#     -	Summary statistics of character columns
#     
#     -	Summary statistics of all the columns
#     
#     
# 9.	Computation of measures of central tendency
#     -	Mean
#     
#     -	Median
#     
#     -	Mode
#     
#     
# 10.	Computation of measures of dispersion or variability
#     -	Minimum and maximum values
#     
#     -	Range
#     
#     -	Variance
#     
#     -	Standard deviation
#     
#     -	Median
#     
#     -	Interquartile Range
#     
#     
# 11.	Computation of measures of shape of distribution
#     -	Skewness
#     
#     -	Kurtosis
#     
#     
# 12.	Results and conclusion
# 
# 

# # 1. Introduction to descriptive statistics
# 
# 
# Descriptive statistics are numbers that are used to describe and summarize the data. They are used to describe the basic features of the data under consideration. They provide simple summary measures which give an overview of the dataset. Summary measures that are commonly used to describe a data set are measures of central tendency and measures of variability or dispersion. 
# 
# 
# Measures of central tendency include the `mean`, `median` and `mode`. These measures summarize a given data set by providing a single data point. These measures describe the center position of a distribution for a data set. We analyze the frequency of each data point in the distribution and describes it using the mean, median or mode. They provide the average of a data set. They can be either a representation of entire population or a sample of the population.
# 
# 
# Measures of variability or dispersion include the `variance` or `standard deviation`, `coefficient of variation`,  `minimum` and `maximum` values, `IQR (Interquartile Range)`,  `skewness and `kurtosis`. These measures help us to analyze how spread-out the distribution is for a dataset. So, they provide the shape of the data set.
# 

# ## 2. Measures of central tendency
# 
# 
# **Central tendency** means a central value which describe a probability distribution. It may also be called a center or location of the distribution. The most common measures of central tendency are **mean**, **median** and **mode**. The most common measure of central tendency is the **mean**. For skewed distribution or when there is concern about outliers, the **median** may be preferred. So, median is more robust measure than the mean.
# 
# 
# 
# ### Mean
# 
# - The most common measure of central tendency is the mean.
# - Mean is also known as the simple average.
# - It is denoted by greek letter µ for population and by ¯x for sample.
# - We can find mean of a number of elements by adding all the elements in a dataset and then dividing by the number of elements  in the dataset.
# - It is the most common measure of central tendency but it has a drawback.
# - The mean is affected by the presence of outliers.
# - So, mean alone is not enough for making business decisions.
# 
# 
# ### Median
# 
# - Median is the number which divides the dataset into two equal halves.
# - To calculate the median, we have to arrange our dataset of n numbers in ascending order.
# - The median of this dataset is the number at (n+1)/2 th position, if n is odd.
# - If n is even, then the median is the average of the (n/2)th number and (n+2)/2 th number.
# - Median is robust to outliers.
# - So, for skewed distribution or when there is concern about outliers, the median may be preferred.
# 
# 
# ### Mode
# 
# - Mode of a dataset is the value that occurs most often in the dataset.
# - Mode is the value that has the highest frequency of occurrence in the dataset.
# 
# 
# There is no best measure that give us the complete picture. So, these measures of central tendency (mean, median and mode) should be used together to represent the full picture. 
# 
# 

# ## 3. Measures of dispersion or variability
# 
# 
# **Dispersion** is an indicator of how far away from the center, we can find the data values. The most common measures of dispersion are **variance**, **standard deviation** and **interquartile range (IQR)**. **Variance** is the standard measure of spread. The **standard deviation** is the square root of the variance. The **variance** and **standard deviation** are two useful measures of spread. 
# 
# 
# 
# ### Variance
# 
# -	Variance measures the dispersion of a set of data points around their mean value.
# 
# -	It is the mean of the squares of the individual deviations.
# 
# -	Variance gives results in the original units squared.
# 
# 
# 
# ### Standard deviation
# 
# -	Standard deviation is the most common used measure of variability.
# 
# -	It is the square-root of the variance.
# 
# -	For Normally distributed data, approximately 95% of the values lie within 2 s.d. of the mean. 
# 
# -	Standard deviation gives results in the original units.
# 
# 
# ### Coefficient of Variation (CV)
# 
# -	Coefficient of Variation (CV) is equal to the standard deviation divided by the mean.
# 
# -	It is also known as `relative standard deviation`.
# 
# 
# ### IQR (Interquartile range)
# 
# -	A third measure of spread is the **interquartile range (IQR)**.
# 
# -	The IQR is calculated using the boundaries of data situated between the 1st and the 3rd quartiles.
# 
# -	The interquartile range (IQR) can be calculated as follows:-
#        IQR = Q3 – Q1
#        
# -	In the same way that the median is more robust than the mean, the IQR is a more robust measure of spread than variance and standard deviation and should therefore be preferred for small or asymmetrical distributions. 
# 
# -	It is a robust measure of spread.
# 
# 
# 
# ### Measures of shape
# 
# Now, we will take a look at measures of shape of distribution. There are two statistical measures that can tell us about the shape of the distribution. These measures are **skewness** and **kurtosis**. These measures can be used to convey information about the shape of the distribution of the dataset.
# 
# 
# ### Skewness
# -	**Skewness** is a measure of a distribution's symmetry or more precisely lack of symmetry. 
# 
# -	It is used to mean the absence of symmetry from the mean of the dataset. 
# 
# -	It is a characteristic of the deviation from the mean. 
# 
# -	It is used to indicate the shape of the distribution of data.
# 
# 
# #### Negative skewness
# 
# -	Negative values for skewness indicate negative skewness. 
# 
# -	In this case, the data are skewed or tail to left.
# 
# -	By skewed left, we mean that the left tail is long relative to the right tail. 
# 
# -	The data values may extend further to the left but concentrated in the right.
# 
# -	So, there is a long tail and distortion is caused by extremely small values which pull the mean downward so that it is less than the median. 
# 
# -	Hence, in this case we have
#       **Mean < Median < Mode**
#       
# 
# #### Zero skewness
# 
# -	Zero skewness means skewness value of zero. 
# 
# -	It means the dataset is symmetrical.
# 
# -	A data set is symmetrical if it looks the same to the left and right to the center point. 
# 
# -	The dataset looks bell shaped or symmetrical. 
# 
# -	A perfectly symmetrical data set will have a skewness of zero. 
# 
# -	So, the normal distribution which is perfectly symmetrical has a skewness of 0. 
# -	So, in this case, we have
#       **Mean = Median = Mode**
#       
# 
# #### Positive skewness
# 
# -	Positive values for skewness indicate positive skewness. 
# 
# -	The dataset are skewed or tail to right.
# 
# -	By skewed right, we mean that the right tail is long relative to the left tail.
# 
# -	The data values are concentrated in the right. 
# 
# -	So, there is a long tail to the right that is caused by extremely large values which pull the mean upward so that it is greater than the median. 
# 
# -	So, we have
#        **Mean > Median > Mode**
#        
# 
# #### Reference range on skewness values
# 
# The rule of thumb for skewness values are:
# 
# -	If the skewness is between -0.5 and 0.5, the data are fairly symmetrical.
# 
# -	If the skewness is between -1 and – 0.5 or between 0.5 and 1, the data are moderately skewed.
# 
# -	If the skewness is less than -1 or greater than 1, the data are highly skewed.
# 
# 
# ### Kurtosis
# 
# -	Kurtosis is the degree of peakedness of a distribution. 
# 
# -	Data sets with high kurtosis tend to have a distinct peak near the mean, decline rather rapidly and have heavy tails.
# 
# -	Data sets with low kurtosis tend to have a flat top near the mean rather than a sharp peak. 
# 
# 
# #### Reference range for kurtosis
# -	The reference standard is a normal distribution, which has a kurtosis of 3.
# 
# -	Often, **excess kurtosis** is presented instead of kurtosis, where **excess kurtosis** is simply **kurtosis - 3**. 
# 
# #### Mesokurtic curve
# -	A normal distribution has kurtosis exactly 3 (**excess kurtosis** exactly 0). 
# 
# -	Any distribution with kurtosis ≈3 (excess ≈ 0) is called **mesokurtic**.
# 
# #### Platykurtic curve
# -	A distribution with kurtosis < 3 (**excess kurtosis** < 0) is called **platykurtic**. 
# 
# -	As compared to a normal distribution, its central peak is lower and broader, and its tails are shorter and thinner.
# 
# ####Leptokurtic curve
# 
# -	A distribution with kurtosis > 3 (**excess kurtosis** > 0) is called **leptokurtic**. 
# 
# -	As compared to a normal distribution, its central peak is higher and sharper, and its tails are longer and fatter.
# 
# 
# #### Summary
# 
# 
# So far, we have looked at the measures of central tendency of the data which include `mean`, `median` and `mode`. Also, we have taken a look at measures of spread of the data which consists of `variance`, `standard deviation`, `interquartile range (IQR)`, `minimum` and `maximum` values. We have also discussed `skewness` and `kurtosis` as measures of shape. These quantities can only be used for quantitative variables not for categorical variables.
# 

# # 5. Import libraries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# ### Ignore warnings

# In[2]:


import warnings
warnings.filterwarnings('ignore')
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)


# ## 6. Import dataset

# In[3]:


df = pd.read_csv('fortune500.csv')


# ## 7. Exploratory data analysis
# 
# 
# Now, I will explore the data to gain insights about the data.

# ### View dimensions of dataset

# In[4]:


#Shape of the dataset
df.shape


# We can see that there are 25500 instances and 5 variables in the data set.

# ### Preview the dataset

# In[5]:


#top 5 rows of dataset
df.head(5)


# ### View summary of dataset

# In[6]:


#summary of dataset
df.info()


# ### Observations
# 
# - We can see that the `Year` and `Rank` variables have integer data types as expected. The `Company` variable is of object data type. 
# 
# - The `Revenue (in millions)` variable is of float data type.
# 
# - The `Profit (in millions)` variable is of object data type. 

# ### Check for missing values

# In[7]:


# check for null values
df.isnull().sum()


# The above command shows that there are no missing values in the dataset.

# ## 8. Descriptive statistics with `describe()` function
# 
# 
# 
# Descriptive or summary statistics in python – pandas, can be obtained by using the `describe()` function. The `describe()` function gives us the `count`, `mean`, `standard deviation(std)`, `minimum`, `Q1(25%)`, `median(50%)`, `Q3(75%)`, `IQR(Q3 - Q1)` and `maximum` values.
# 
# 
# I will demonstrate the usage of `describe()` function as follows.

# ### Summary statistics of numerical columns

# In[8]:


#all statistical measure
df.describe()


# We can see that the `describe()` function excludes the character columns and gives summary statistics of numeric columns only.

# ### Summary statistics of character columns
# 
# 
# - The `describe()` function with an argument named `include` along with `value` object(include='object') gives the summary statistics of the character columns.

# In[9]:


#summary statistics of character column
df.describe(include='object')


# ### Summary statistics of all the columns
# 
# 
# - The `describe()` function with include='all' gives the summary statistics of all the columns.
# 
# 
# - We need to add a variable named include='all' to get the summary statistics or descriptive statistics of both numeric and character columns.

# In[10]:


#summary statistics of all the column
df.describe(include='all')


# ## 9. Computation of measures of central tendency 
# 
# 
# - In this section, I will compute the measures of central tendency - mean, median and mode. 
# 
# - These statistics give us a approximate value of the middle of a numeric variable.
# 
# - I will use the `Revenue (in millions)` variable for calculations.

# ### Mean

# In[11]:


#Mean of revenue(in millions)
Mean=df['Revenue (in millions)'].mean()

print(Mean)


# ### Median

# In[12]:


#Median of Revenue(in millions)
Median=df['Revenue (in millions)'].median()
print(Median)


# ### Mode

# In[13]:


#Mode of Revenue
Mode=df['Revenue (in millions)'].mode()
print(Mode)


# ### Observation
# 
# 
# - We can see that `mean > median > mode`. So, the distribution of `Revenue (in millions)` is positively skewed. I will plot its distribution to confirm the same.

# ### Plot the distribution 

# In[14]:


#Plot the distribution
data = df['Revenue (in millions)']

sns.distplot(data, bins=10, hist=True, kde=True, label = 'Revenue (in millions)')


# The above plot confirms that the `Revenue (in millions)` is positively skewed.

# ## 10. Computation of measures of dispersion or variability
# 
# 
# - In this section, I will compute the measures of dispersion or variability - minimum and maximum values, range, variance, standard-deviation, IQR. 
# 
# - Again, I will use the `Revenue (in millions)` variable for calculations.
# 

# ### Minimum value

# In[15]:


#check min of Revenue(in millions)
Min=df['Revenue (in millions)'].min()
print(Min)


# ### Maximum value

# In[16]:


#check max of Revenue(in millions)
Max=df['Revenue (in millions)'].max()
print(Max)


# ### Range

# In[17]:


#Range of Revenue (in millions)
Range=Max - Min
print(Range)


# ### Variance

# In[18]:


#check varience of Revenue(in millions)
df['Revenue (in millions)'].var()


# ### Standard deviation

# In[19]:


#check standard deviation  of Revenue(in millions)
df['Revenue (in millions)'].std()


# ### Median (Q2 or 50th percentile)

# In[20]:


#check Q2 of Revenue (in millions)
Q2=np.percentile(df['Revenue (in millions)'],50,interpolation='midpoint')
print(Q2)


# ### Q3 or 75th percentile

# In[21]:


#check Q3 of Revenue (in millions)
Q3=np.percentile(df['Revenue (in millions)'],75,interpolation='midpoint')
print(Q3)


# ### Q1 or 25th percentile

# In[22]:


#check Q1 of Revenue (in millions)
Q1=np.percentile(df['Revenue (in millions)'],25,interpolation='midpoint')
print(Q1)


# ### Interquartile Range
# 

# In[23]:


#check IQR
IQR=Q3-Q1
print(IQR)


# ### Draw boxplot

# In[24]:


#Draw boxplot of Revenue (in millions)
plt.figure()
plt.boxplot(df['Revenue (in millions)'])
plt.show()


# ## 11. Computation of measures of shape of distribution
# 
# 
# - In this section, I will compute the measures of shape of distribution - skewness and kurtosis. 
# 
# - Again, I will use the `Revenue (in millions)` variable for calculations.
# 

# ### Skewness
# 

# In[25]:


#Skewness of Revenue (in millions)
df['Revenue (in millions)'].skew()


# ### Interpretation
# 
# I find the skewness to be 9.3267. So, it is greater than 1. Hence, we can conclude that the `Revenue (in millions)` data is highly skewed.

# ### Kurtosis

# In[26]:


# kurtosis of Revenue (in millions)
df['Revenue (in millions)'].kurt()


# ### Interpretation
# 
# I find the kurtosis to be 132.0456. So, it is greater than 3 and so excess kurtosis > 0. Hence, we can conclude that the `Revenue (in millions)` curve is a leptokurtic curve. As compared to a normal distribution, its central peak is higher and sharper, and its tails are longer and fatter.

# ## 12. Results and conclusion
# 
# 
# 1.	In this project, I describe the descriptive statistics that are used to summarize a dataset. 
# 
# 2.	In particular, I have described the measures of central tendency (mean, median and mode). I have also described the measures of dispersion or variability (variance, standard deviation, coefficient of variation, minimum and maximum values, IQR) and measures of shape (skewness and kurtosis).
# 
# 3.	I have demonstrated how to calculate the summary statistics with `describe()` function.
# 
# 4.	I have computed the measures of central tendency-mean, median and mode for the `Revenue (in millions)`variable. I have found `mean > median > mode`. So, the distribution of `Revenue (in millions)` is positively skewed. I have plotted its distribution to confirm the same.
# 
# 5.	I have computed the measures of dispersion or variability-range, variance, standard-deviation, median and IQR for the `Revenue (in millions)`variable.
# 
# 6.	I have also computed the measures of shape-skewness and kurtosis for the `Revenue (in millions)`variable.
# 7.	I find the skewness to be 9.3267. So, it is greater than 1. Hence, we can conclude that the `Revenue (in millions)` data is highly skewed.
# 
# 8.	I find the kurtosis to be 132.0456. So, it is greater than 3 and so excess kurtosis > 0. Hence, we can conclude that the `Revenue (in millions)` curve is a leptokurtic curve. As compared to a normal distribution, its central peak is higher and sharper, and its tails are longer and fatter.
# 

# In[27]:


#valuecounts of Revenue (in millions)
df['Revenue (in millions)'].value_counts()


# In[28]:


#valuecounts of Profit (in millions)
df['Profit (in millions)'].value_counts()


# In[29]:


df.dtypes


# In[31]:


df["Profit (in millions)"] = df["Profit (in millions)"].replace('NaN', 0)


# In[32]:


df.describe()


# In[33]:


df["Profit (in millions)"] = pd.to_numeric(df["Profit (in millions)"], errors='coerce')


# In[34]:


df.describe()

