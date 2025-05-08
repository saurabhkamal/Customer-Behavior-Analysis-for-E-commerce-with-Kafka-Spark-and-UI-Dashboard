# Customer-Behavior-Analysis-for-E-commerce-with-Kafka-Spark-and-UI-Dashboard

This project is designed to track and understand how customers interact with an e-commerce platform in real-time, using a combination of data simulation, processing, and visual reporting tools.

### Step 1: Simulating Customer Behavior
A simple web interface allows you to mimic a customer visiting the website—selecting a product, clicking on items, or checking out. These actions are sent instantly to a system that handles real-time data (Kafka).

### Step 2: Storing Customer Activity
Once the simulated customer actions are sent, a background program listens to them continuously and saves this data into a database (MongoDB), so it can be analyzed later.

### Step 3: Visual Dashboard for Insights
A live dashboard reads this stored data and shows key insights like:
- How active customers are over time
- Which products are most popular
- What actions customers take (like viewing, adding to cart, etc.)
- Who the most active customers are

The dashboard also includes filters so users can zoom in on specific dates, activities, or products.

This project mimics how a modern online business tracks customer behavior to:
- Improve marketing and product strategy
- Identify top-performing products or power users
- Detect changes in customer interest or behavior in real time

It's a miniature version of the systems used by Amazon, Flipkart, or any major online retailer to stay competitive and customer-focused.


### 1.	“customer_data_producer.py”:
“customer_data_producer.py” is a Kafka producer application built using Streamlit (for the UI), Kafka (Confluent Cloud), and Python. Its primary purpose is to simulate and send customer behavior events (clickstream data) to a Kafka topic named "customer_click_data".

#### Streamlit UI: •	A simple web form is created using Streamlit where a user can:
- Input a user_id
- Select an activity (like view_product, checkout, etc.)
-	Select a product (like Laptop, mobile, etc.)

![image](https://github.com/user-attachments/assets/5dc79e7a-1a1d-4713-a2d4-b6d6165b803d)

#### Data Sending Function (send_event): When the "send data" button is clicked
1. A JSON event is created containing:
-	user_id, activity, product, and timestamp
2.	This event is serialized into JSON and sent to Kafka using the producer.produce() method.
3.	producer.flush() ensures the message is actually pushed out (not stuck in buffer).
4.	A success message is displayed showing the sent event.

![image](https://github.com/user-attachments/assets/8c1a3d9a-3990-49bb-82e0-9102dff71a77)

This code is useful when:
-	You're simulating customer behavior (like clicking or adding to cart).
-	You want to stream this behavior in real-time to Kafka, which can then be processed using Apache Spark, stored in a database, or visualized in PowerBI dashboards.

### 2.	“customer_data_processor.py”
customer_data_processor.py is a Kafka consumer application that continuously listens to real-time customer events from Kafka and stores them into MongoDB for persistent storage and later analysis.

![image](https://github.com/user-attachments/assets/4833c408-5532-4fd8-887e-59f9f63baef4)

customer_data_processor.py is a Kafka consumer that continuously reads customer clickstream events from the Kafka topic customer_click_data, enriches them with Kafka metadata, and stores them into a MongoDB collection for further use in dashboards, analytics, or machine learning pipelines.

### 3.	“customer_analytics.py”
customer_analytics.py is a Streamlit-based analytics dashboard that connects to MongoDB, reads customer interaction data (produced via Kafka and stored earlier), and presents interactive visualizations and metrics about customer behavior on the e-commerce platform.

It is used for real-time business intelligence and monitoring customer behavior trends like:
•	Product interest
•	User activity frequency
•	Popular actions (e.g., view, add_to_cart)
•	Most active users

 ![image](https://github.com/user-attachments/assets/5fa06515-5958-498d-b767-bafea5914f89)

 ![image](https://github.com/user-attachments/assets/9782ab87-6dab-4d12-8ea7-a3afd1261e46)

![image](https://github.com/user-attachments/assets/4b895f2b-8da0-4ed4-9881-e11627028703)

#### Charts and Visual Insights
-	Activity Timeline: Shows number of activities over time (e.g., daily engagement trends).
-	Product Distribution: Shows what products users interacted with most
-	Activity Types: How many times each action was performed (e.g., "view_product" vs "checkout").
-	Top 10 Active Users: Shows the most active users on your site (likely your power users).
-	Sidebar Filters: 
(a). Filter by date range
(b). Filter by activity type (e.g., only “checkout”)
(c). Filter by product (e.g., only “Laptop”)



