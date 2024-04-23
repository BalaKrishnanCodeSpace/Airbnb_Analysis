![HEADING](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/290d9333b34ebeed685e250e34fa683e5904364a/Misc/Title.PNG)
<div align="center"> 
  <h3>An interactive application designed to visually analyze Airbnb data. Explore pricing trends, discover availability patterns and uncover location-driven insights - all through a visually intuitive interface.</h3>
</div></br>



## Table of Contents

- [Overview](#overview)
- [Project Objectives](#project-objectives)
- [Developer Guide](#developer-guide)
- [Features](#features)
- [Interface](#interface)
- [About the Developer](#about-the-developer)
</br>

## Overview
This project explores the world of Airbnb rentals through a data-driven lens. By leveraging various data science techniques and industry-standard tools, the project aims to uncover valuable insights for stakeholders and potential Airbnb hosts.</br></br>

## Project Objectives
- **<em><ins>Data Acquisition and Cleaning</ins></em>**
  - <b>MongoDB Connection:</b> Establish a connection to the MongoDB Atlas database and retrieve the Airbnb dataset.
  - <b>Implement data cleaning procedures to address missing values:</b> Identify and handle missing entries in the data.
  - <b>Remove duplicates:</b> Eliminate redundant data points.
  - <b>Ensure data consistency:</b> Standardize data formats and address any inconsistencies.

- **<em><ins>Exploratory Data Analysis (EDA)</ins></em>**
  - <b>Utilize Python libraries like Pandas and NumPy:</b> Leverage these libraries for data manipulation and analysis.
  - <b>Conduct in-depth data analysis:</b> Explore the data to identify trends, patterns, and relationships between variables.

- **<em><ins>Geospatial Visualization</ins></em>**
  - <b>User Interface:</b> Construct an interactive web application using Streamlit.
  - <b>Leverage geospatial data from Airbnb listings:</b> Utilize location data to create informative maps.
  - <b>Employ GeoPandas or Folium libraries (optional):</b> These libraries can be used for advanced geospatial processing and visualization.

- **<em><ins>Data Storytelling</ins></em>**
  - <b>Power BI:</b> Develop comprehensive data visualizations using Tableau or Power BI.
  - <b>Effectively communicate key takeaways and insights:</b> Create visualizations that clearly present the findings from the data analysis.

- **<em><ins>Problem-Solving and Decision Making</ins></em>**
  - <b>Apply analytical thinking:</b> Utilize data analysis techniques to investigate factors influencing Airbnb listings.
  - <b>Investigate factors influencing pricing, availability, and other aspects:</b> Analyze factors that impact these aspects of Airbnb listings.
  - <b>Empower stakeholders with data-driven insights:</b> Provide stakeholders with actionable information to guide decision-making.</br></br></br>


## Developer Guide
To run the Streamlit web application, you'll need to follow these steps:

1. Install Dependencies
Navigate to the project directory and install the required dependencies using pip:

```python
pip install -r requirements.txt
```

2. Get MongoDB URI
Log in to your MongoDB Atlas account and navigate to your cluster. Copy the connection string (URI) provided by Atlas.

3. Set Up Connection in Python:
create an account in [**MongoDB Atlas**](https://account.mongodb.com/account/login) and set up a cluster. MongoDB Atlas provides cloud-hosted MongoDB databases that allow you to store and manage your data in a scalable and secure manner. Creating a cluster is necessary to deploy and manage your MongoDB database in the cloud. Use the pymongo library to establish a connection to MongoDB Atlas in your Python script. Here's an example:

```python
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Atlas connection URI
uri = "mongodb+srv://<username>:<password><database>?retryWrites=true&w=majority&appName=<cluster>"

# Create a new client and connect to the server using the provided URI
Client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
Client.admin.command('ping')

# Accessing the desired database and collection
Database = Client.sample_airbnb
Collection = Database.listingsAndReviews
```

3. Run the Application
Once the cluster is created modify it in the code in the python file airbnb.py then you can run the Streamlit application with the following command:

```python
streamlit run airbnb.py
```

4. Access the Application
Once the Streamlit server is running, you can access the application by opening a web browser and navigating to the URL provided by Streamlit, typically http://localhost:8501.

5. Explore the Application
You can now explore the different features and functionalities of the Streamlit application as per your requirements.


## Features
- Data Visualization: Visualize Airbnb data using interactive charts and maps.
- Streamlit Integration: Utilize Streamlit to create a user-friendly web interface for data exploration.
- MongoDB Connectivity: Connect to MongoDB Atlas to retrieve and analyze Airbnb data stored in the cloud.
- Power BI Integration: Embed Power BI visualizations within the Streamlit app for enhanced data presentation.


## Interface
1. ### <em><ins><b>Home Page<b></ins></em></br>
   The home page provides an overview of Airbnb analysis, including a brief description of the application's purpose, skills developed, and domain expertise. It also features a YouTube video embedded to provide additional context.</br></br>
![HomePage](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Home_Page.png)




2. ### <em><ins><b>Export Page<b></ins></em></br>
   The export page allows users to extract fresh data from MongoDB Atlas and export it to a CSV file. Upon clicking the "Extract to CSV" button, the application retrieves data from MongoDB, converts it to a DataFrame, and exports it to a CSV file.</br></br>
![ExportPage](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Export_Page.png)


3. ### <em><ins><b>Visualization Page<b></ins></em></br>
   The Visualization Page offers two tabs:</br>
   -  Visualization Tab:</br>
         Provides interactive Power BI visualizations, showcasing comprehensive insights into Airbnb data, including property listings, availability trends, and pricing analysis.</br>
   -  EDA (Exploratory Data Analysis) Tab:</br>
         Presents visualizations generated within Streamlit using Python libraries such as pandas, Matplotlib, and Seaborn. Users can explore correlation heatmaps and outlier analysis plots to gain deeper insights into the dataset.</br></br>
![VisualizationPage1](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Visualization_Page%20-%20Power%20BI.png)
![VisualizationPage2](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Visualization_Page%20-%20EDA.png)


4. ### <em><ins><b>Contact Page<b></ins></em></br>
   The contact page provides users with information on how to contact the developers for inquiries or feedback. It includes details such as the developer's name, location, and links to their LinkedIn and GitHub profiles. Additionally, users can submit their details and remarks via a form for further communication.</br></br>
![ContactPage](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Contact_Page.png)</br></br>




## About the Developer
Hi there! 👋 I'm Balakrishnan Ravikumar, the developer behind this project. I'm deeply passionate about leveraging data-driven insights to solve real-world problems and drive decision-making. I believe that by harnessing the power of data analytics, we can unlock valuable insights that lead to smarter and more informed decisions. Whether it's optimizing business processes or improving customer experiences or addressing societal challenges, I'm dedicated to using data science techniques to make a positive impact on the world around us.</br>

## Contact Information
Feel free to reach out to me if you have any questions, feedback, or just want to connect! You can find me at:</br>

Name: Balakrishnan Ravikumar</br>
Location: Chennai, Tamil Nadu, India</br>
LinkedIn: [LinkedIn Profile URL](https://www.linkedin.com/in/balakrishnan-ravikumar-8790732b6/)</br>
GitHub: [GitHub Profile URL](https://github.com/BalaKrishnanCodeSpace)</br>
