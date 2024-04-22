import streamlit as st                                  # Importing Streamlit library for building web apps
from streamlit_option_menu import option_menu           # Importing option_menu from streamlit_option_menu for dropdown menus
import pandas as pd                                     # Importing pandas for data manipulation
from PIL import Image                                   # Importing Image module from PIL for working with images
from pymongo.mongo_client import MongoClient            # Importing MongoClient from pymongo for MongoDB interactions
from pymongo.server_api import ServerApi                # Importing ServerApi from pymongo for MongoDB server API interactions
import time                                             # Importing time module for time-related functions
import urllib.request                                   # Importing urllib.request for making HTTP requests
import io                                               # Importing io module for working with streams
import os                                               # Importing os module for operating system-related functions
import datetime                                         # Importing datetime module for date and time manipulation
import matplotlib.pyplot as plt                         # Importing matplotlib.pyplot for plotting
import seaborn as sns                                   # Importing seaborn for statistical data visualization
from streamlit_js_eval import streamlit_js_eval         # Importing streamlit_js_eval for evaluating JavaScript in Streamlit



# URL for the Airbnb icon image
image_icon = "https://cdn.iconscout.com/icon/free/png-256/free-airbnb-3771463-3149883.png?f=webp&w=128"

# Setting the page configuration for the Streamlit app
# - page_title: Title of the page displayed in the browser tab
# - page_icon: Icon displayed in the browser tab
# - layout: Layout style of the app ("wide" in this case)
st.set_page_config(page_title="Airbnb Analysis", page_icon=image_icon, layout="wide")


#   ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ Establish connection to MongoDB Atlas ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~   #
def mongoDb_connection():
    """
    Establishes a connection to MongoDB and returns a collection object.

    Returns:
        pymongo.collection.Collection: Collection object for accessing MongoDB documents.
    """

    # MongoDB connection URI
    uri = "mongodb+srv://<username>:<password><cluster>?retryWrites=true&w=majority&appName=<cluster>" # due to security reasons i have not supplied the credentials 
    
    try:
        # Create a new client and connect to the server using the provided URI
        Client = MongoClient(uri, server_api=ServerApi('1'))
        
        # Send a ping to confirm a successful connection
        Client.admin.command('ping')
        
        # Accessing the desired database and collection
        Database = Client.sample_airbnb
        Collection = Database.listingsAndReviews
        
    except Exception as e:
        # If there's an exception, display the error message
        st.write(e)
    
    # Return the MongoDB collection object
    return Collection


#   ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~ Convert Collection to DataFrame ~ - ~ - ~ - ~ - ~ - ~ - ~ - ~   #
def convert_to_dataframe(Collection):
    """
    Converts MongoDB documents from a collection into a DataFrame.

    Args:
        Collection (pymongo.collection.Collection): MongoDB collection object.

    Returns:
        pandas.DataFrame: DataFrame containing the converted MongoDB documents.
    """
    # Retrieve all documents from the MongoDB collection
    Cursor = Collection.find({})
    
    # Initialize an empty list to store the extracted values
    Values = []
    
    # Iterate through each document in the collection
    for item in Cursor:
        # Extract relevant fields from the document and create a dictionary
        Value = {
            'Id' : item['_id'],
            'Name' : item['name'],
            'Country' : item['address']['country'],
            'Latitude' : item['address']['location']['coordinates'][0],
            'Longitude' : item['address']['location']['coordinates'][1],
            'Government_Area' : item['address']['government_area'],
            'Market' : item['address']['market'],
            'Street' : item['address']['street'],
            'Suburb' : item['address']['suburb'],
            'Availability_30' : item['availability']['availability_30'],
            'Availability_365' : item['availability']['availability_365'],
            'Availability_60' : item['availability']['availability_60'],
            'Availability_90' : item['availability']['availability_90'],
            'Bathrooms' : item.get('bathrooms',0),
            'Bed_Type' : item['bed_type'],
            'Bedrooms' : item.get('bedrooms',0),
            'Beds' : item.get('beds',0),
            'Number_Of_Reviews' : item['number_of_reviews'],
            'Price' : item['price'],
            'Property_Type' : item['property_type'],
            'Review_Scores_Accuracy' : item['review_scores'].get('review_scores_accuracy',0),
            'Review_Scores_Checkin' : item['review_scores'].get('review_scores_checkin',0),
            'Review_Scores_Cleanliness' : item['review_scores'].get('review_scores_cleanliness',0),
            'Review_Scores_Communication' : item['review_scores'].get('review_scores_communication',0),
            'Review_Scores_Location' : item['review_scores'].get('review_scores_location',0),
            'Review_Scores_Rating' : item['review_scores'].get('review_scores_rating',0),
            'Review_Scores_Value' : item['review_scores'].get('review_scores_value',0),
            'Room_Type' : item['room_type'],
            'Security_Deposit' : item.get('security_deposit',0),
            'Accommodates' : item['accommodates'],
            'Image': item['images']['picture_url']
        }
        # Append the dictionary to the list
        Values.append(Value)
    
    # Create a DataFrame from the list of dictionaries
    Data_Frame = pd.DataFrame(Values)
    
    # Return the DataFrame
    return Data_Frame






        
# Dictionary containing names of properties as keys and corresponding image URLs as values
images = {
    "Vintage Heritage Home, Chickmagalur - India" : "https://a0.muscache.com/im/pictures/6b950473-60fd-44df-b61c-cfdff0137a41.jpg?im_w=1200",
    "Sangria Sun Villa, Wadduwa - India" : "https://a0.muscache.com/im/pictures/f7aebffd-229f-48e8-bc6d-a4117e4a526c.jpg?im_w=720",
    "Galkadawala Forest Lodge, Habarana - Sri Lanka" : "https://a0.muscache.com/im/pictures/8cf29ad3-e909-4520-b5e2-814b2a32f942.jpg?im_w=1200",
    "Boutique Hotel, Gokarna - India" : "https://a0.muscache.com/im/pictures/1d9c40a4-385c-4682-8f98-03a5c8cdd5bd.jpg?im_w=1200",
    "Vythiri Adora, Vythiri - India" : "https://a0.muscache.com/im/pictures/e546f349-341f-4f6f-9b0d-3c6db351efe5.jpg?im_w=1200",
    "Zostel Plus Panchgani, Dandeghar - India" : "https://a0.muscache.com/im/pictures/miso/Hosting-1049731144550365439/original/4ada4ea4-d694-40bb-b61e-b8bebd5dfc72.jpeg?im_w=1200",
    "Lakeview Villa, Koggala - Sri Lanka" : "https://a0.muscache.com/im/pictures/60d72a59-2778-4310-a7e2-09e7d0b8c1ad.jpg?im_w=1200",
    "Grand Hills, Kandy - Sri Lanka" : "https://a0.muscache.com/im/pictures/miso/Hosting-39492258/original/4f89f3ad-23a7-46e2-b074-c6aa3928b5ae.jpeg?im_w=720",
    "Cave House, Kalpetta, India" : "https://a0.muscache.com/im/pictures/hosting/Hosting-995433353546423140/original/b008b88c-ce95-4667-a4b7-070244f1b3fd.jpeg?im_w=720",
    "The Tree House, Munnar - India" : "https://a0.muscache.com/im/pictures/miso/Hosting-48837541/original/9b2665b5-5f8f-4694-ad4b-7e4e491a90b1.jpeg?im_w=1200"
    }



# Define image size for resizing
image_size = (450, 250)

# Maximum width and height for images
max_width, max_height = 1080, 720

# Initialize index for image iteration
index = 0

# Dictionary to cache images
cache = {}


def fetch_image(url):
    """
    Fetches an image from a URL and resizes it.

    Args:
        url (str): URL of the image to fetch.

    Returns:
        Image: Resized image object.
    """
    try:
        # Check if the image is already in the cache
        if url not in cache:
            # Fetch the image data from the URL
            with urllib.request.urlopen(url) as response:
                image_data = response.read()
                # Open the image data as an Image object
                img = Image.open(io.BytesIO(image_data))
                # Resize the image to fit within the maximum dimensions
                img.thumbnail((max_width, max_height))
                # Resize the image to the specified size
                img_resized = img.resize(image_size)
                # Cache the resized image
                cache[url] = img_resized
        # Return the cached image
        return cache[url]
    except Exception as e:
        # If there's an error loading the image, display an error message
        st.error(f"Error loading image: {e}")


def display_carousel():
    """
    Displays a carousel of images with navigation dots.

    The images and their URLs are taken from the 'images' dictionary.
    """
    global index    # Use the global index variable
    
    # Use a Streamlit container for layout
    with st.container():
        # Get the place name corresponding to the current index
        place_name = list(images.keys())[index]
        
        # Fetch the image corresponding to the place name
        img = fetch_image(images[place_name])
        
        # Display the image with specified width and caption
        st.image(img, use_column_width=False, width=image_size[0], caption=place_name)

        # Create navigation dots for each image in the carousel
        dots = [
            # Use a filled dot for the current index and an empty dot for others
            "<span style='font-size:24px;color:#d8dbe3;'>&#9679;</span>" if i != index else "<span style='font-size:24px;color:black;font-weight:bold;'>&#9679;</span>"
            for i in range(len(images))
        ]
        
        # Concatenate the navigation dots into HTML format
        dots_html = "<div style='text-align:center; margin-top: 2px;'>{}</div>".format(" ".join(dots))
        
        # Display the navigation dots
        st.markdown(dots_html, unsafe_allow_html=True)
    
    # Update the index for the next image
    index = (index + 1) % len(images)



def display_flying_airplane():
    """
    Displays a flying airplane icon with CSS animation and dynamically updates its position using JavaScript.
    """
    # CSS code for airplane animation
    css_code = """
    @keyframes fly {
        from {
            left: -100px;
            top: calc(100% + 400px);
        }
        to {
            left: calc(100% + 100px);
            top: -400px;
        }
    }

    .airplane {
        position: absolute;
        animation: fly 10s linear infinite;
    }
    """

    # Apply the CSS code to the Streamlit app
    st.markdown(f'<style>{css_code}</style>', unsafe_allow_html=True)

    # Display the flying airplane icon
    st.markdown('<img id="airplane" src="https://emojicdn.elk.sh/airplane?style=twitter" class="airplane">', unsafe_allow_html=True)

    # Execute JavaScript to dynamically update airplane's position
    st.markdown("""
        <script>
        setTimeout(() => {
            const airplane = document.getElementById('airplane');
            airplane.style.left = '-50px'; // Initial horizontal position
            airplane.style.top = 'calc(100% + 50px)'; // Initial vertical position
        }, 1000); // Delay animation start by 1 second
        </script>
    """, unsafe_allow_html=True)




# Adding empty lines using st.write() to create space between elements
st.write("")
st.write("")

# Adding custom CSS to adjust padding between Streamlit blocks
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

# Setting background color for the entire Streamlit app
background_color = "#FFFCFA"
st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {background_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Hiding the default Streamlit menu and footer
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)


colheading1, colheading2, colheading3 = st.columns([0.35,3,10])
with colheading1:
    st.image(image_icon,use_column_width = False, width=35)
with colheading2:
    # Display the Heading of the page with linear gradient color
    st.markdown("<p style='font-family:Arial, sans-serif; font-size: 23px; font-weight: bold; background-image: linear-gradient(to right, #FE5D62, #E24E52); -webkit-background-clip: text; background-clip: text; color: transparent; letter-spacing: 0.01em;'>airbnb analysis</p>", unsafe_allow_html=True)
    st.write("")
with colheading3:
    st.write()


# Creating menu using the streamlit_option_menu library
Selected_Option = option_menu(
    menu_title = None,                                                                              # Title of the menu (None in this case)
    options=["Home","Export","Visualization", "Contact"],                                           # List of menu options
    default_index= 0,                                                                               # Index of the default selected option
    icons =["house-heart-fill", "cloud-download-fill", "clipboard2-data-fill", "person-heart"],     # Icons for each option
    orientation="horizontal",                                                                       # Orientation of the menu (horizontal or vertical)
    styles={
    "container": {"background-color": "white", "padding": "0!important", "height": "38px", "width" : "1000px"}, # Styles for the menu container
    "icon": {"color": "black", "font-size": "17px"},                                                # Styles for the icons
    "nav-link": { "--hover-color": "#FFC5BD","color": "black","width":"190px",
                    "text-align":"center","padding":"0px 1",
                    "border-bottom":"1px solid transparent","transition":"border-bottom 0.3 ease","font-size":"15px", "margin": "-2px"},    # Styles for the menu links
    "nav-link:hover": {"color":"orange"},                                                           # Styles for hovered menu links
    "nav-link-selected": {"background-color": "white", "width":"190px", "height" :"38px", "border-bottom":"2px solid #FF8271","color":"#FF8271", "border-radius": "90px"}       # Styles for the selected menu link
    }
)


# Check if the selected option is "Home"
if Selected_Option == "Home":

    # Display the flying airplane icon
    display_flying_airplane()
    col1, col2, col3 = st.columns([9,1,5])
    with col1:
        # Adding custom CSS for styling
        # Set the background color and style for headers, subheaders, and paragraphs
        st.markdown(
            """
            <style>
            /* Set the background color to a light gray */
            body {
                background-color: #f5f5f5;
            }
            /* Style the headers */
            .header {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            /* Style the subheaders */
            .subheader {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 5px;
            }
            /* Style the paragraph */
            .paragraph {
                font-size: 16px;
                margin-bottom: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )

        # Display the content
        st.markdown("<div class='header'>Airbnb Analysis</div>", unsafe_allow_html=True)
        st.markdown("<div class='paragraph'>Airbnb is an American company headquartered in San Francisco. It operates an online marketplace for short- and long-term homestays and experiences. Acting as a broker, Airbnb charges a commission from each booking. Founded in 2008 by Brian Chesky, Nathan Blecharczyk, and Joe Gebbia, Airbnb initially began as AirBedandBreakfast.com. The company is renowned for revolutionizing the tourism industry, albeit receiving criticism from residents of tourism hotspot cities like Barcelona and Venice for contributing to unaffordable housing and a lack of regulation.</div>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<div class='subheader'>Skills Developed:</div>", unsafe_allow_html=True)
        st.markdown("<div class='paragraph'>Python Scripting, Data Preprocessing, Data Visualization, Exploratory Data Analysis (EDA), Streamlit, MongoDB, PowerBI, Tableau</div>", unsafe_allow_html=True)
        st.write("")
        st.markdown("<div class='subheader'>Domain Expertise:</div>", unsafe_allow_html=True)
        st.markdown("<div class='paragraph'>Travel Industry, Property Management, Tourism</div>", unsafe_allow_html=True)
        st.write("")
        st.write("")
        # Embedded airbnb advertisement YouTube video
        st.markdown(
            '<iframe width="560" height="315" src="https://www.youtube.com/embed/dA2F0qScxrI?si=_cAfePnqddGaQ8i0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
            unsafe_allow_html=True
        )
    with col2:
        st.write()
    with col3:
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        
        # Added a link to the official Airbnb page with an accompanying image
        img = "https://pro2-bar-s3-cdn-cf2.myportfolio.com/b492d4692a1c93964dbcca21ec2fd997/da0bdcc1-1f47-4883-996b-d6673de88721_rw_1920.jpg?h=8f44f2c4af0ae85515cf54ee001ed9bc"
        link = "https://www.airbnb.co.in/"
        st.markdown(f'<a href="{link}" target="_blank"><img src="{img}" style="max-width:100%; cursor:pointer;"></a> <span style="font-size: 12px; color: grey;"><u>Click the above image to visit airbnb official page</u></span>', unsafe_allow_html=True)
        
        st.write("")
        st.write("")
        st.write("")
        
        # Display the carousel and update it every 2 seconds
        placeholder = st.empty()
        while True:
            with placeholder.container():
                display_carousel()  # Function to display the carousel
            time.sleep(2)           # Pause for 2 seconds before updating the carousel


# Check if the selected option is "Export"
if Selected_Option == "Export":
    st.write("")
    st.write("")
    st.write("")
    
    # Display a styled header for the export section
    st.markdown("<p style='font-family:Arial, sans-serif; font-size: 23px; font-weight: bold; background-image: linear-gradient(to right, #FE5D62, #E24E52); -webkit-background-clip: text; background-clip: text; color: transparent; letter-spacing: 0.01em;'>Extract fresh data from MongoDB Atlas to CSV</p>", unsafe_allow_html=True)
    
    # Define the file path for the CSV file
    file_path = r"C:\My Folder\airbnb_data.csv"

    # Check if the file exists
    if os.path.exists(file_path):
        # Get the modification time of the file
        modification_time = os.path.getmtime(file_path)
        # Convert the modification time to a readable date format
        modified_date = datetime.datetime.fromtimestamp(modification_time)
        formatted_date = modified_date.strftime("%d-%m-%Y")
        # Display the last modified date of the file
        st.write(f"<font size='3' color='#050408'>Data Last modified on {formatted_date}</font>", unsafe_allow_html=True)
    else:
        # If the file doesn't exist, prompt the user to click the button to extract data
        print("The file does not exist. Please click Extract to extract convert to CSV")
    
    st.write("")
    st.write("")
    
    # Check if the "Extract to CSV" button is clicked
    if st.button('Extract to CSV'):
        with st.spinner('Please wait while we Extract data to CSV File'):
            # Establish connection to MongoDB
            Collection = mongoDb_connection()
            # Convert MongoDB data to DataFrame
            df = convert_to_dataframe(Collection)            
            # Export DataFrame to CSV file
            df.to_csv(r"C:\My Folder\airbnb_data.csv",index = False)
            # Display success message after exporting
            st.write("CSV file exported successfully")


# Check if the selected option is "Visualization"
if Selected_Option == "Visualization":
    # Define tabs for visualization and EDA (Exploratory Data Analysis)
    tab1, tab2 = st.tabs(["⠀⠀⠀⠀⠀Visualization⠀⠀⠀⠀⠀","⠀⠀⠀⠀⠀EDA⠀⠀⠀⠀⠀"])
    
    # Content of the first tab (Visualization)
    with tab1:
        # Embed Power BI report for visualization
        report_url = "https://app.powerbi.com/reportEmbed?reportId=651d7462-f3c5-4487-94f3-06bc1289d654&autoAuth=true&ctid=9a3061eb-e87d-4997-aefe-ee5e7692e94e"
        st.markdown(f'<iframe width="1370" height="600" src="{report_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
    
    # Content of the second tab (EDA)
    with tab2:
        df = pd.read_csv(r"C:\My Folder\airbnb_data.csv")                           # Read data from the CSV file
        df["Id"] = df["Id"].astype(str)                                             # Convert the "Id" column to string type
        numeric_df = df.select_dtypes(include=['int64'])                            # Select numeric columns for correlation analysis
        
        # ----> Create a heatmap of the correlation matrix
        correlation_matrix = numeric_df.corr()                                      
        plt.figure(figsize=(20, 15))                                                
        sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt=".2f")
        plt.title("Correlation Heatmap")
        plt.xticks(rotation=45, ha = 'right')
        plt.yticks(rotation=0)
        st.pyplot(plt)
        
        # ----> Create a outlier of the "Price"
        # Calculate quartiles and IQR for the "Price" column
        Q1_price = df['Price'].quantile(0.25)
        Q3_price = df['Price'].quantile(0.75)

        # Calculate the interquartile range (IQR) for the "Price" column
        IQR_price = Q3_price - Q1_price

        # Define a threshold for outliers
        threshold_price = 1.5

        # Identify outliers in the "Price" column using the IQR method
        outliers_price = ((df['Price'] < (Q1_price - threshold_price * IQR_price)) | (df['Price'] > (Q3_price + threshold_price * IQR_price)))

        # Create a scatter plot of Price vs Index, highlighting outliers
        plt.figure(figsize=(20, 20))
        sns.scatterplot(data=df, x=df.index, y='Price', color='blue', label='Data')
        sns.scatterplot(data=df[outliers_price], x=df[outliers_price].index, y='Price', color='red', label='Outliers')
        plt.xlabel('Index')
        plt.ylabel('Price')
        plt.title('Outliers in Price Column')
        plt.legend()
        st.pyplot(plt)
        
        
# Check if the selected option is "Contact"
if Selected_Option == "Contact":
    col1, col2 = st.columns([6,5])
    with col1:
        st.write('')
        st.write('')
        st.markdown('<h2 style="color: #615955; text-decoration: underline;">Contact Us</h2>', unsafe_allow_html=True)
        st.write('')
        st.subheader('*:red[Balakrishnan Ravikumar]*')
        st.write('*Mylapore, Chennai, Tamil Nadu, India*')
        st.write('')
        st.write('')
        st.write('')
        st.write('')
        st.markdown('<img src="https://static-00.iconduck.com/assets.00/linkedin-icon-1024x1024-net2o24e.png" width="25" height="25">&nbsp;&nbsp;[Click here to visit our LinkedIn page](https://www.linkedin.com/in/balakrishnan-ravikumar-8790732b6/)', unsafe_allow_html=True)
        st.markdown('<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="25" height="25">&nbsp;&nbsp;[Click here to visit our Github page](https://github.com/BalaKrishnanCodeSpace)', unsafe_allow_html=True)
        st.write('')
        st.write('')
        st.markdown("<iframe src='https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3890.3743995180666!2d80.26730301482026!3d13.032550190796538!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a5266b6f4de2397%3A0x39d2ffdb6a48ec92!2sThirumayilai%2C%20Mylapore%2C%20Chennai%2C%20Tamil%20Nadu%2C%20India!5e0!3m2!1sen!2sca!4v1647159863087!5m2!1sen!2sca' width='400' height='250' style='border:0;' allowfullscreen='' loading='lazy'></iframe>", unsafe_allow_html=True)
    with col2:
        st.write('')
        st.write('')
        st.write('')
        st.write('')

        # Function to validate email format
        def is_valid_email(email):
            # check for '@' and '.com' in email
            if "@" in email and ".com" in email:
                return True # Return True if conditions met
            return False    # Return False otherwise

        # Function to validate phone number format
        def is_valid_phone(phone_number):
            # Check if only digits and length is 10
            if phone_number.isdigit() and len(phone_number) == 10:
                return True # Return True if conditions met
            return False    # Return False otherwise

        st.markdown('<h3 style="color:#F6565A">Please fill out the form below to contact us.</h3>', unsafe_allow_html=True)
        st.write('')
        name = st.text_input("**Name**")
        email = st.text_input("**Email ID**")
        phone_number = st.text_input("**Phone Number**")
        remarks = st.text_area("**Remarks**")

        if st.button("Submit"):
            # Validation checks for input fields
            if name.strip() == "":
                st.error("Please enter your name.")
            elif email.strip() == "":
                st.error("Please enter your email ID.")
            elif not is_valid_email(email):
                st.error("Please enter a valid email ID.")
            elif phone_number.strip() == "":
                st.error("Please enter your phone number.")
            elif not is_valid_phone(phone_number):
                st.error("Please enter a valid phone number.")
            else:
                # Display success message if details are valid
                st.success("Your details have been submitted successfully!")
                time.sleep(3)
                streamlit_js_eval(js_expressions="parent.window.location.reload()")
