# Walmart Sales Data Analysis

## About

The project entails data cleaning,data wrangling,exploratory data analysis,data modelling and data modelling code and visualization that will be uploaded soon

The Weather dataset is a time-series data set with per hour information about the weather conditions at a particular location. It records Temperature,Dew point Temperature,Relative Humidity,Wind speed,
visisbility,Presssure and Conditions.
The data is avaiilable as a csv file.The datais being analyzed using pandas a python library.

## Purposes Of The Project

The major aim of thie project is to gain insight into the weather parterns and conditions that can be used to predict the weather conditions.
## About Data

The dataset was obtained from the [Kaggle Walmart Sales Forecasting Competition](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting). This dataset contains sales transactions from a three different branches of Walmart, respectively located in Mandalay, Yangon and Naypyitaw. The data contains 17 columns and 1000 rows:

| Column                  | Description                             | Data Type      |
| :---------------------- | :-------------------------------------- | :------------- |
| invoice_id              | Invoice of the sales made               | VARCHAR(30)    |
| branch                  | Branch at which sales were made         | VARCHAR(5)     |
| city                    | The location of the branch              | VARCHAR(30)    |
| customer_type           | The type of the customer                | VARCHAR(30)    |
| gender                  | Gender of the customer making purchase  | VARCHAR(10)    |
| product_line            | Product line of the product solf        | VARCHAR(100)   |
| unit_price              | The price of each product               | DECIMAL(10, 2) |
| quantity                | The amount of the product sold          | INT            |
| VAT                 | The amount of tax on the purchase           | FLOAT(6, 4)    |
| total                   | The total cost of the purchase          | DECIMAL(10, 2) |
| date                    | The date on which the purchase was made | DATE           |
| time                    | The time at which the purchase was made | TIMESTAMP      |
| payment_method          | The total amount paid                   | DECIMAL(10, 2) |
| cogs                    | Cost Of Goods sold                      | DECIMAL(10, 2) |
| gross_margin_percentage | Gross margin percentage                 | FLOAT(11, 9)   |
| gross_income            | Gross Income                            | DECIMAL(10, 2) |
| rating                  | Rating                                  | FLOAT(2, 1)    |


### Model
![Data Model](https://lucid.app/publicSegments/view/70a34985-32d9-4731-93a0-1ef1df23c541/image.png)

## Dashboard
![pp](https://github.com/kayikalvin/Weather-dataset-Analysis/assets/161039123/763af298-3ea7-403c-812a-da17862d11dc)



### Analysis List

1. Product Analysis

> Conduct analysis on the data to understand the different product lines, the products lines performing best and the product lines that need to be improved.

2. Sales Analysis

> This analysis aims to answer the question of the sales trends of product. The result of this can help use measure the effectiveness of each sales strategy the business applies and what modificatoins are needed to gain more sales.

3. Customer Analysis

> This analysis aims to uncover the different customers segments, purchase trends and the profitability of each customer segment.

## Approach Used

1. **Data Wrangling:** This is the first step where inspection of data is done to make sure **NULL** values and missing values are detected and data replacement methods are used to replace, missing or **NULL** values.

> 1. This project was done entirely using PYTHON

2. **Feature Engineering:** This will help use generate some new columns from existing ones.

> 1. Add a new column named `time_of_day` to give insight of sales in the Morning, Afternoon and Evening. This will help answer the question on which part of the day most sales are made.

> 2. Add a new column named `day_name` that contains the extracted days of the week on which the given transaction took place (Mon, Tue, Wed, Thur, Fri). This will help answer the question on which week of the day each branch is busiest.

> 3. Add a new column named `month_name` that contains the extracted months of the year on which the given transaction took place (Jan, Feb, Mar). Help determine which month of the year has the most sales and profit.

2. **Exploratory Data Analysis (EDA):** Exploratory data analysis is done to answer the listed questions and aims of this project.

3. **Conclusion:**

## Business Questions To Answer

### Generic Question

1. Find all the unique 'Wind Speed' values in the data
2. Find out all the Null Values in the data


## project solutions
  - Q1. Find the number of items when the "Weather is clear"
  - Q2. Find the number of times when the 'Wind Speedd was exactly 4 km/h' 
  - Q3. Rename the column name 'Weather' of the dataframe to 'Weather Condition'
  - Q4. What is the mean Visisbility
  - Q5. What is the standard deviation of 'Pressure' in the data
  - Q6. What is the variance of 'Relative Humidity' in this data
  - Q7. Find all instances when 'Snow' was recorded
  - Q8. Find all the instances where 'Wind Speed is above 24' and 'Visibility is 25'
  - Q9. What is the mean value of each column against each 'Weather Condition'
  - Q10. What is the Minimum and Maximun value of each column against 'Weather Condition'
  - Q11. Show all the records when the weather is 'Fog'
  - Q12. Find all instances where weather is 'Clear' or 'Visibility is above 40'
  - Q13. Find all instances when :
  'Weather is clear' and 'Relative Humidity is greater than 50'
  or
  'Visibility is above 40'



