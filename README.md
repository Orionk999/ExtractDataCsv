# Extract Data CSV


This repository extract data from file .csv

## 1. **First Point**

Clone the repository and check the code.

 **How It Works**

I have processed the input .csv file, and if the data is correct, two output files will be generated: one containing 
the correct records and another containing the incorrect ones, without altering the original file.

Each validation takes the data from the column and verifies whether the data is correct or not.

## 2. **Second Point** 


The architecture outlined below can have frontend-generated events as a data source.

Additionally, the Amazon S3 
service can be used as a backup.

Spark Streaming is utilized to calculate metrics and business indicators.

Cassandra, Hadoop, and Mongo are used for storing user data.

This can be done this way because Kafka allows us to handle messages from any data source, such as events.


![Secondpoint.png](assets%2FSecondpoint.png)


## 3. **Third point**

**The following diagram illustrates how the database should be developed for the proper storage of information.**

![ThirdPoint.png](assets%2FThirdPoint.png)

In this diagram, the "ProductDetails" table is added, which is responsible for storing the characteristics of the 
products
such as width, height, weight, and even color, as long as a numerical value can be assigned.

Additionally, the "userProfile_Id" relationship is assigned to the user table, which will be responsible for the 
connection with the profiles table.

Product manages a one-to-many connection for the characteristics of each product.