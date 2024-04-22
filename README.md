![HEADING](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/290d9333b34ebeed685e250e34fa683e5904364a/Misc/Title.PNG)


<div align="center"> 
  <h3>An intuitive application designed to visually analyze Airbnb data, providing valuable insights into fluctuations in pricing, patterns of availability, and trends based on location.</h3>
</div>
</br>
</br>



## Overview
This project explores the world of Airbnb rentals through a data-driven lens. By leveraging various data science techniques and industry-standard tools, the project aims to uncover valuable insights for stakeholders and potential Airbnb hosts.</br></br></br>

## Project Objectives
- **<em><ins>Data Acquisition and Cleaning</ins></em>**
  - Establish a connection to the MongoDB Atlas database and retrieve the Airbnb dataset.
  - <b><em>Implement data cleaning procedures to address missing values:</em></b> Identify and handle missing entries in the data.
  - <b>Remove duplicates:</b> Eliminate redundant data points.
  - <b>Ensure data consistency:</b> Standardize data formats and address any inconsistencies.

- **<em><ins>Exploratory Data Analysis (EDA)</ins></em>**
  - Utilize Python libraries like Pandas and NumPy: Leverage these libraries for data manipulation and analysis.
  - Conduct in-depth data analysis: Explore the data to identify trends, patterns, and relationships between variables.

- **<em><ins>Geospatial Visualization</ins></em>**
  - Construct an interactive web application using Streamlit.
  - Leverage geospatial data from Airbnb listings: Utilize location data to create informative maps.
  - Employ GeoPandas or Folium libraries (optional): These libraries can be used for advanced geospatial processing and visualization.

- **<em><ins>Data Storytelling</ins></em>**
  - Develop comprehensive data visualizations using Tableau or Power BI.
  - Effectively communicate key takeaways and insights: Create visualizations that clearly present the findings from the data analysis.

- **<em><ins>Problem-Solving and Decision Making</ins></em>**
  - Apply analytical thinking: Utilize data analysis techniques to investigate factors influencing Airbnb listings.
  - Investigate factors influencing pricing, availability, and other aspects: Analyze factors that impact these aspects of Airbnb listings.
  - Empower stakeholders with data-driven insights: Provide stakeholders with actionable information to guide decision-making.</br></br></br>


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


## User Guide
1. Home Page
![HomePage](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Home_Page.png)




2. Export Page
![ExportPage](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Export_Page.png)


3. Visualization Page
![VisualizationPage1](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Visualization_Page%20-%20Power%20BI.png)
![VisualizationPage2](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Visualization_Page%20-%20EDA.png)


4. Contact Page
![ContactPage]((https://github.com/BalaKrishnanCodeSpace/airbnb/blob/76167a23cbe1adb3b9d6737a1a32baffc8e4b288/Misc/Contact_Page.png)))
