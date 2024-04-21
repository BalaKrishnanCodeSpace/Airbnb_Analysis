![HEADING](https://github.com/BalaKrishnanCodeSpace/airbnb/blob/290d9333b34ebeed685e250e34fa683e5904364a/Misc/Title.PNG)

<div align="center"> A user-friendly application to visualize Airbnb Data to gain insights into pricing variations, availability patterns, and location-based trends.</div>



## Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Run/Test My App  (Deployed in Cloud)](#run/test-my-app-(Deployed-in-Cloud))
- [Prerequisites](#prerequisites)
- [Testing the Application Locally](#testing-the-application-locally)
- [Demo/Presentation Video](#demopresentation-video)
- [Conclusion](#conclusion)
- [Contact](#contact)


## Overview:

This project simplifies the process of extracting and managing information from business cards using optical character recognition (OCR) and a user-friendly Streamlit interface. It empowers users to:

- Upload business card images
- Extract relevant information using easyOCR
- View extracted information in a clear format
- Save information to a database (SQLite or MySQL)
- Read, update, and delete stored data through the Streamlit UI

## Problem Statement:

This project aims to analyze Airbnb data using MongoDB Atlas, perform data cleaning and preparation, develop interactive geospatial visualizations, and create dynamic plots to gain insights into pricing variations, availability patterns, and location-based trends. Finally, build a comprehensive dashboard using Tableau or Power BI, combining various visualizations to present key insights from the analysis.

## Run/Test My App (Deployed in Cloud):
I deployed my app in Streamlit cloud to access directly from [here](https://santhosh-airbnb-analysis.streamlit.app/).

## Prerequisites:

Before you begin, ensure you have met the following requirements:

- Python: Version 3.11.0 or higher. [Download Python](https://www.python.org/downloads/)
- Required packages : <img alt="Static Badge" src="https://img.shields.io/badge/Streamlit_easyOCR-Install_using_pip-red">
- Git: Version control tool. [Download Git](https://git-scm.com/downloads)
- Install dependencies: `pip install -r requirements.txt`

## Testing the Application Locally:
To clone and run this application, you'll need [![Git Badge](https://img.shields.io/badge/Git-red?style=flat-square&logo=git&logoColor=%23F05032&label=Install)](https://git-scm.com/) installed on your computer. 

1. Clone the repository:

      ``` bash
        git clone https://github.com/Santhosh-Analytics/BizCardX-Extracting-Business-Card-Data-with-OCR

3. Navigate to the project directory:
    ``` bash
    cd BizCardX-Extracting-Business-Card-Data-with-OCR
5. Install dependencies:
      ``` bash
    pip install -r requirements.txt
      
7. Run the application:
     ``` bash
    streamlit run BizCard_main.py
10. **Ensure you use your SQL user credentials in the** [SQL Root Config file](https://github.com/Santhosh-Analytics/BizCardX-Extracting-Business-Card-Data-with-OCR/blob/main/SQL_root_config.py).


## Demo/Presentation Video:


## Conclusion:
In conclusion, this Streamlit application addresses the challenge of efficiently extracting and managing business card information. By leveraging Python, Streamlit, easyOCR, and a chosen database system, it provides a seamless user experience. The project not only showcases adeptness in image processing, OCR, and GUI development but also emphasizes scalability, maintainability, and extensibility. Continuous improvements, such as feature additions and security enhancements, underscore the commitment to delivering a robust and user-friendly solution, making it a valuable asset for those seeking an effective business card data extraction and management tool.

## Contact
If you have any questions or feedback, feel free to reach out at [email](mailto:santhosh90612@gmail.com).
