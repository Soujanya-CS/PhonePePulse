import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector
import geopandas as gpd

# Load your data
data = {
    "State": ["Andhra Pradesh", "Maharashtra", "Tamil Nadu", "Karnataka", "Kerala", "Andaman & Nicobar Island", "Arunanchal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Daman & Diu", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jammu & Kashmir", "Jharkhand", "Lakshadweep", "Madhya Pradesh", "Manipur", "Chandigarh", "Puducherry", "Punjab", "Rajasthan", "Sikkim", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Odisha", "Dadara & Nagar Havelli", "Meghalaya", "Mizoram", "Nagaland", "NCT of Delhi", "Telangana"],
    "Value": [28, 27, 33, 29, 32, 35, 12, 18, 10, 22, 25, 30, 24, 6, 2, 1, 20, 31, 23, 14, 4, 34, 3, 8, 11, 16, 9, 5, 19, 21, 26, 17, 15, 13, 7, 0]
}
df = pd.DataFrame(data)

geojson_path = r"C:\Users\Soujanya\Downloads\states_india.geojson"
gdf = gpd.read_file(geojson_path)

# Merge the data with the GeoJSON based on state names
merged_gdf = gdf.merge(df, left_on="st_nm", right_on="State", how="left")

# Connect to the MySQL database
def connect_to_db(database_name):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Ammu@2397',
        database=database_name
    )
    return conn

# Fetch data from the database
def fetch_data(conn, table_name):
    query = f"SELECT * FROM {table_name}"
    data = pd.read_sql(query, conn)
    return data

# Fetch data using a custom query
def fetch_query_data(conn, query):
    data = pd.read_sql(query, conn)
    return data

# Streamlit app for topdf database
def topdf_app():
    st.title("Top Visualization")
    conn = connect_to_db('topdf')

    # Select a table to visualize
    table_name = st.selectbox("Select a table", ["districts_table", "pincodes_table", "userdistricts_table", "userpincodes_table"])

    # Fetch data
    data = fetch_data(conn, table_name)

    st.write(f"Showing data from '{table_name}' table:")
    st.write(data)

    # Visualization options
    st.sidebar.header("Visualization Options")
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])
    x_col = st.sidebar.selectbox("Select X-axis Column", data.columns)
    y_col = st.sidebar.selectbox("Select Y-axis Column", data.columns)

    st.header("Data Visualization")
    if chart_type == "Bar Chart":
        fig = px.bar(data, x=x_col, y=y_col, title=f"{chart_type} - {x_col} vs {y_col}")
    elif chart_type == "Pie Chart":
        fig = px.pie(data, names=x_col, values=y_col, title=f"{chart_type} - {x_col} vs {y_col}")
    else:
        fig = px.line(data, x=x_col, y=y_col, title=f"{chart_type} - {x_col} vs {y_col}")

    st.plotly_chart(fig)

    # Inbuilt query results
    st.header("Inbuilt Query Results")
    query = "SELECT State, COUNT(*) as Count FROM districts_table GROUP BY State"
    query_data = fetch_query_data(conn, query)

    st.write("Query Result:")
    st.write(query_data)

    # Visualize query result
    query_chart = px.bar(query_data, x='State', y='Count', title="State-wise Distribution")
    st.plotly_chart(query_chart)

    conn.close()

# Streamlit app for mapsdf database
def mapsdf_app():
    st.title("Maps Visualization")
    conn = connect_to_db('mapsdf')

    # Select a table to visualize
    table_name = st.selectbox("Select a table", ["hoverstable", "hoversdatatable"])

    # Fetch data
    data = fetch_data(conn, table_name)

    st.write(f"Showing data from '{table_name}' table:")
    st.write(data)

    # Visualization options
    st.sidebar.header("Visualization Options")
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart", "India Choropleth Map"])
    x_col = st.sidebar.selectbox("Select X-axis Column", data.columns)
    y_col = st.sidebar.selectbox("Select Y-axis Column", data.columns)

    st.header("Data Visualization")
    if chart_type == "Bar Chart":
        fig = px.bar(data, x=x_col, y=y_col, title=f"{chart_type} - {x_col} vs {y_col}")
    elif chart_type == "Pie Chart":
        fig = px.pie(data, names=x_col, values=y_col, title=f"{chart_type} - {x_col} vs {y_col}")
    elif chart_type == "India Choropleth Map":
        # Choropleth map code goes here (see below)
        pass
    else:
        fig = px.line(data, x=x_col, y=y_col, title=f"{chart_type} - {x_col} vs {y_col}")

    st.plotly_chart(fig)

    conn.close()

# Streamlit app for aggregatedf database
def aggregatedf_app():
    st.title("Aggregated Visualization")
    conn = connect_to_db('aggregatedf')

    table_name = st.selectbox("Select a table", ["aggregated", "districts_table", "pincodes_table", "users_by_device"])

    # Fetch data
    data = fetch_data(conn, table_name)

    st.write(f"Showing data from '{table_name}' table:")
    st.write(data)

    # Visualization options
    st.sidebar.header("Visualization Options")
    chart_type = st.sidebar.selectbox("Select Chart Type", ["Bar Chart", "Line Chart", "Pie Chart"])
    x_col = st.sidebar.selectbox("Select X-axis Column", data.columns)
    y_col = st.sidebar.selectbox("Select Y-axis Column", data.columns)

    st.header("Data Visualization")
    if chart_type == "Bar Chart":
        fig = px.bar(data, x=x_col, y=y_col, title=f"{chart_type} - {x_col} vs {y_col}")
    elif chart_type == "Pie Chart":
        fig = px.pie(data, names=x_col, values=y_col, title=f"{chart_type} - {x_col} vs {y_col}")
    else:
        fig = px.line(data, x=x_col, y=y_col, title=f"{chart_type} - {x_col} vs {y_col}")

    st.plotly_chart(fig)

    conn.close()

def Indian_Choropleth_map():
    st.title("PhonePe Users in India")
    conn = connect_to_db('tops_total')

    table_name = st.selectbox("Select a table", ["totaltransaction", "topstotalusers"])

    data = fetch_data(conn, table_name)

    st.write(f"Showing data from '{table_name}' table:")
    st.write(data)

    # Merge the data with the GeoDataFrame based on the "State" column
    merged_data = merged_gdf.merge(data, left_on="State", right_on="State", how="right")

    x_col = st.sidebar.selectbox("Select X-axis Column", data.columns)
    y_col = st.sidebar.selectbox("Select Y-axis Column", data.columns)

    fig = px.choropleth(
        merged_data,
        geojson=merged_gdf.geometry,
        locations=merged_data.index,
        color=y_col,  
        hover_name=x_col,
        title=f"{x_col} vs {y_col}",
        color_continuous_scale="YlGnBu"
    )
    fig.update_geos(fitbounds='locations', visible=False)

    # Streamlit UI
    st.plotly_chart(fig)


def topsdf_choropleth_map():
    st.title("TopSDF Choropleth Map")
    conn = connect_to_db('topdf')  # Connect to the 'topsdf' database

    table_name = st.selectbox("Select a table", ["totaltransaction", "topstotalusers"])

    data = fetch_data(conn, table_name)

    st.write(f"Showing data from '{table_name}' table:")
    st.write(data)

    # Merge the data with the GeoDataFrame based on the "State" column
    merged_data = merged_gdf.merge(data, left_on="State", right_on="State", how="right")

    x_col = st.sidebar.selectbox("Select X-axis Column", data.columns)
    y_col = st.sidebar.selectbox("Select Y-axis Column", data.columns)

    fig = px.choropleth(
        merged_data,
        geojson=merged_gdf.geometry,
        locations=merged_data.index,
        color=y_col,  # Adjust this to the column you want to use for color
        hover_name=x_col,  # Adjust this to the column you want to use for hover text
        title=f"{x_col} vs {y_col}",
        color_continuous_scale="YlGnBu"
    )
    fig.update_geos(fitbounds='locations', visible=False)

    # Streamlit UI
    st.plotly_chart(fig)

def mapsdf_choropleth_map():
    st.title("MapsDF Choropleth Map")
    conn = connect_to_db('mapsdf')  # Connect to the 'mapsdf' database

    table_name = st.selectbox("Select a table", ["hoverstable", "hoversdatatable"])

    data = fetch_data(conn, table_name)

    st.write(f"Showing data from '{table_name}' table:")
    st.write(data)

    # Merge the data with the GeoDataFrame based on the "State" column
    merged_data = merged_gdf.merge(data, left_on="State", right_on="State", how="right")

    x_col = st.sidebar.selectbox("Select X-axis Column", data.columns)
    y_col = st.sidebar.selectbox("Select Y-axis Column", data.columns)

    fig = px.choropleth(
        merged_data,
        geojson=merged_gdf.geometry,
        locations=merged_data.index,
        color=y_col,  # Adjust this to the column you want to use for color
        hover_name=x_col,  # Adjust this to the column you want to use for hover text
        title=f"{x_col} vs {y_col}",
        color_continuous_scale="YlGnBu"
    )
    fig.update_geos(fitbounds='locations', visible=False)

    # Streamlit UI
    st.plotly_chart(fig)

def aggregateddf_choropleth_map():
    st.title("AggregatedDF Choropleth Map")
    conn = connect_to_db('aggregatedf')  # Connect to the 'aggregateddf' database

    table_name = st.selectbox("Select a table", ["aggregated", "districts_table", "pincodes_table", "users_by_device"])

    data = fetch_data(conn, table_name)

    st.write(f"Showing data from '{table_name}' table:")
    st.write(data)

    # Merge the data with the GeoDataFrame based on the "State" column
    merged_data = merged_gdf.merge(data, left_on="State", right_on="State", how="right")

    x_col = st.sidebar.selectbox("Select X-axis Column", data.columns)
    y_col = st.sidebar.selectbox("Select Y-axis Column", data.columns)

    fig = px.choropleth(
        merged_data,
        geojson=merged_gdf.geometry,
        locations=merged_data.index,
        color=y_col,  # Adjust this to the column you want to use for color
        hover_name=x_col,  # Adjust this to the column you want to use for hover text
        title=f"{x_col} vs {y_col}",
        color_continuous_scale="YlGnBu"
    )
    fig.update_geos(fitbounds='locations', visible=False)

    # Streamlit UI
    st.plotly_chart(fig)

def main():
    pages = {
        'Top Visualization': topdf_app,
        'Maps Visualization': mapsdf_app,
        'Aggregated Visualization': aggregatedf_app,
        'PhonePe Users in India': Indian_Choropleth_map,
        'TopSDF Choropleth Map': topsdf_choropleth_map,
        'MapsDF Choropleth Map': mapsdf_choropleth_map,
        'AggregatedDF Choropleth Map': aggregateddf_choropleth_map
    }
    st.sidebar.title('Navigation')
    selected_page = st.sidebar.radio('Go to', tuple(pages.keys()))

    if selected_page in pages:
        pages[selected_page]()

if __name__ == "__main__":
    logo_image = "phonepeimg.jpeg"
    st.image(logo_image, use_column_width=True)
    # Set page title and description
    st.title("PhonePe Pulse Data Visualization")
    st.markdown("A data visualization app that aims to extract, transform, and visualize data from the PhonePe Pulse GitHub repository.")
    main()