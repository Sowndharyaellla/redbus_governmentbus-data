
Project Title
Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit
Skills take away From This Project
Web Scraping using Selenium, Python, Streamlit , SQL
Domain
Transportation


Problem Statement:
The "Redbus Data Scraping and Filtering with Streamlit Application" aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

Overview
The provided code aims to extract bus data from the Redbus website for 10 Government state buses and store it in a database. It utilizes Selenium for web automation, Pandas for data manipulation, and PyMySQL for database interaction.

Breakdown of the Code
Import Necessary Libraries:

streamlit: For building interactive web applications (not used in the core scraping logic).
pymysql: For interacting with MySQL database.
pandas: For data manipulation and analysis.
selenium and its associated modules: For web browser automation and interaction.

Establish Database Connection:
Connects to a MySQL database named 'project_redbus' using provided credentials.

Define State Names:
Creates a list of state names for potential future use .

Function to Get Route Names:
Takes a state name as input.
Queries the database for distinct route names within that state.
Returns a list of route names.

Function to Get Bus Types:
Takes a route name as input.
Queries the database for distinct bus types for that route.
Returns a list of bus types.

Sidebar Selection:
Uses Streamlit to create a sidebar with options for state, route, and bus type rating and price selection.
Calls the get_route_name and get_bus_type functions to populate dropdown options.
sliding is used for price and rating.

Main Logic:
Upon clicking the "SEARCH" button:
Constructs an SQL query based on selected filters.
Executes the query and fetches data.
Creates a Pandas DataFrame from the fetched data.
Connects to the MySQL database and creates a table to store the data.
Inserts the data from the DataFrame into the database.

