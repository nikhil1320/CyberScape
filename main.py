import streamlit as st
import pandas as pd
import altair as alt

# Load dataset
file_path = "/mnt/data/Time-Wasters on Social Media.csv"
df = pd.read_csv(file_path)

# Convert necessary columns to appropriate data types
df['Watch Time'] = pd.to_datetime(df['Watch Time'], errors='coerce').dt.hour  # Convert to numeric hours
df['Debt'] = df['Debt'].astype(int)  # Convert boolean to integer

# Title and Introduction
st.title("User Engagement Dashboard")
st.write("Explore insights and KPIs from user engagement data.")

# Sidebar for Filters
st.sidebar.header("Filters")
selected_gender = st.sidebar.selectbox("Select Gender", df['Gender'].unique())
age_range = st.sidebar.slider("Select Age Range", 0, 100, (20, 50))
platform_filter = st.sidebar.multiselect("Select Platform", options=df.Platform.unique(), default=df.Platform.unique())

# Filter data based on selections
filtered_df = df[(df['Gender'] == selected_gender) & (df['Age'].between(age_range[0], age_range[1])) & (df['Platform'].isin(platform_filter))]

# Key Performance Indicators (KPIs)
st.subheader("Key Performance Indicators")
st.metric("Total Time Spent (hours)", int(filtered_df['Total Time Spent'].sum()))
st.metric("Average Productivity Loss", round(filtered_df['ProductivityLoss'].mean(), 2))
st.metric("Average Addiction Level", round(filtered_df['Addiction Level'].mean(), 2))

# User Demographics Distribution
st.subheader("User Demographics")
gender_counts = filtered_df['Gender'].value_counts().reset_index()
gender_chart = alt.Chart(gender_counts).mark_bar().encode(
    x=alt.X('index:N', title='Gender'),
    y=alt.Y('Gender:Q', title='Count'),
    color='index:N'
).properties(width=600, height=400)
st.altair_chart(gender_chart, use_container_width=True)

# Income vs. Debt
st.subheader("Income vs. Debt")
st.scatter_chart(filtered_df[['Income', 'Debt']], use_container_width=True)

# Engagement by Platform
st.subheader("Engagement by Platform")
platform_engagement = df.groupby('Platform')['Engagement'].sum().reset_index()
platform_chart = alt.Chart(platform_engagement).mark_bar().encode(
    x=alt.X('Platform:N', title='Platform'),
    y=alt.Y('Engagement:Q', title='Total Engagement')
).properties(width=600, height=400)
st.altair_chart(platform_chart, use_container_width=True)

# Average Time Spent on Videos by Category
st.subheader("Average Time Spent on Videos by Category")
avg_time = df.groupby('Video Category')['Time Spent On Video'].mean().reset_index()
time_chart = alt.Chart(avg_time).mark_line(point=True).encode(
    x=alt.X('Video Category:N', title='Video Category'),
    y=alt.Y('Time Spent On Video:Q', title='Avg Time Spent (minutes)')
).properties(width=600, height=400)
st.altair_chart(time_chart, use_container_width=True)

# Average Satisfaction Score
st.subheader("Average Satisfaction Score by Profession")
avg_satisfaction = df.groupby('Profession')['Satisfaction'].mean().reset_index()
satisfaction_chart = alt.Chart(avg_satisfaction).mark_bar().encode(
    x=alt.X('Profession:N', title='Profession'),
    y=alt.Y('Satisfaction:Q', title='Avg Satisfaction Score')
).properties(width=600, height=400)
st.altair_chart(satisfaction_chart, use_container_width=True)

# Debt to Income Ratio
st.subheader("Debt to Income Ratio Distribution")
df['Debt to Income Ratio'] = df['Debt'] / df['Income'].replace(0, 1)  # Avoid division by zero
debt_chart = alt.Chart(df).mark_line().encode(
    x=alt.X('index:Q', title='Users'),
    y=alt.Y('Debt to Income Ratio:Q', title='Debt to Income Ratio')
).properties(width=600, height=400)
st.altair_chart(debt_chart, use_container_width=True)

# Video Watch Time by Device Type
st.subheader("Watch Time by Device Type")
device_watch_time = df.groupby('DeviceType')['Watch Time'].sum().reset_index()
device_chart = alt.Chart(device_watch_time).mark_bar().encode(
    x=alt.X('DeviceType:N', title='Device Type'),
    y=alt.Y('Watch Time:Q', title='Total Watch Time (hours)')
).properties(width=600, height=400)
st.altair_chart(device_chart, use_container_width=True)

# Scroll Rate by Video Length
st.subheader("Scroll Rate by Video Length")
scroll_rate_length = df.groupby('Video Length')['Scroll Rate'].mean().reset_index()
scroll_chart = alt.Chart(scroll_rate_length).mark_line(point=True).encode(
    x=alt.X('Video Length:Q', title='Video Length (minutes)'),
    y=alt.Y('Scroll Rate:Q', title='Avg Scroll Rate')
).properties(width=600, height=400)
st.altair_chart(scroll_chart, use_container_width=True)

# Engagement Over Time
st.subheader("Engagement Over Time")
engagement_over_time = df.groupby('Platform')['Engagement'].mean().reset_index()
time_engagement_chart = alt.Chart(engagement_over_time).mark_line(point=True).encode(
    x=alt.X('Platform:N', title='Platform'),
    y=alt.Y('Engagement:Q', title='Avg Engagement')
).properties(width=600, height=400)
st.altair_chart(time_engagement_chart, use_container_width=True)
