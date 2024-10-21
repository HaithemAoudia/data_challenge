## DATA PROCESSING ASSIGNMENT

To address this challenge, I created a Jupyter notebook to showcase my implementation step by step. Running the entire notebook will yield two files. One file outputs a post-processed dataset based on the pipeline I built. The second file is a text file, which is a short report of the data quality assessment and flags any issues if present.



### Suggestion for Further Refinement for Field Experts


#### 1. Identify an Appropriate Range for Experiment Measure Values:

In experiments, it is not uncommon to have erroneous data due to issues with the systems or unprecedented factors. I highly recommend to define acceptable ranges for each variable based on expert input. Experts can set thresholds for variables like Speed (RPM), additive weights, and Output A. Any values outside these predefined ranges could trigger warnings and suggest a further review.

#### 2. Identify an Appropriate Range for Weight Difference (Before and After Drying): 

Based on my understanding of the data, I assume that the difference between the weight before and after drying could be an important metric. In similar fashion to the previous point, experts can define a reasonable percentage or absolute range for the difference between "Weight before Drying" and "Weight after Drying," based on experimental expectations. For example, if the weight loss exceeds or falls below a typical level, it could trigger a quality flag.

#### 3. Handling Different Date and Time for Experiment Runs

In some cases, there may be inconsistencies regarding the date the experiment was run between different files. An assumption I made was that the feed dataset had the correct date. However, I recommend validating what the source of truth date for the field experiment is and adjusting the pipeline accordingly if needed.