# PhonePePulse Data Visualisation
The PhonePe Pulse Data Visualization Project focuses on extracting data from the PhonePe Pulse GitHub repository, processing it, and presenting valuable insights through an interactive dashboard.

**Project Steps**
Data Extraction: The GitHub repository is cloned using scripting to fetch the data from the PhonePe Pulse GitHub repository and store it in a suitable format such as CSV or JSON.

Data Transformation: Python is used, along with libraries like Pandas, for data manipulation and pre-processing. This step involves data cleaning, handling missing values, and transforming the data into a format suitable for analysis and visualization.

Database Insertion: The transformed data is inserted into a MySQL database for efficient storage and retrieval. The "mysql-connector-python" library is used for database interactions.

Dashboard Creation: The interactive dashboard is created using Streamlit and Plotly in Python. Plotly's geo map functions are used to display data on a map, and Streamlit provides a user-friendly interface with dropdown options for users to select different facts and figures to display.

Data Retrieval: Data from the MySQL database is fetched into a Pandas dataframe using the "mysql-connector-python" library. This data is used to dynamically update the dashboard.

**Approach**
-->Clone the repository: git clone https://github.com/your-username/phonepe-pulse-visualization.git

-->Install required dependencies: pip install -r requirements.txt

-->Set up a MySQL database and update database configuration in the code.

-->Run the data extraction, transformation, and insertion scripts.

-->Launch the dashboard: streamlit run dashboard.py

**Results**
A live geo visualization dashboard that displays insights and information from the PhonePe Pulse GitHub repository in an interactive and visually appealing manner. The dashboard includes at least 10 dropdown options for users to select different facts and figures for display. Data is stored in a MySQL database for efficient retrieval, and the dashboard dynamically updates to reflect the latest data.

Users can access the dashboard through a web browser, interact with various visualizations, and gain valuable insights from the PhonePe Pulse data.
