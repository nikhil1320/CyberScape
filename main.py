import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
df = pd.read_csv('Time-Wasters on Social Media.csv')

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

st.subheader("Key Performance Indicators")
st.metric("Total Time Spent (hours)", int(filtered_df['Total Time Spent'].sum()))
st.metric("Average Productivity Loss", round(filtered_df['ProductivityLoss'].mean(), 2))
st.metric("Average Addiction Level", round(filtered_df['Addiction Level'].mean(), 2))

# 1. User Demographics Distribution
st.subheader("User Demographics")
gender_counts = filtered_df['Gender'].value_counts()
fig = px.bar(gender_counts, x=gender_counts.index, y=gender_counts.values, labels={'x': 'Gender', 'y': 'Count'}, title='Gender Distribution')
st.plotly_chart(fig)

# 2. Income vs. Debt
st.subheader("Income vs. Debt")
fig = px.scatter(filtered_df, x='Income', y='Debt', labels={'x': 'Income', 'y': 'Debt'}, title='Income vs. Debt')
st.plotly_chart(fig)

# 3. Engagement by Platform
st.subheader("Engagement by Platform")
platform_engagement = df.groupby('Platform')['Engagement'].sum().reset_index()
fig = px.bar(platform_engagement, x='Platform', y='Engagement', labels={'x': 'Platform', 'y': 'Engagement'}, title='Engagement by Platform')
st.plotly_chart(fig)

# 4. Average Time Spent on Videos by Category
st.subheader("Average Time Spent on Videos by Category")
avg_time = df.groupby('Video Category')['Time Spent On Video'].mean().reset_index()
fig = px.line(avg_time, x='Video Category', y='Time Spent On Video', labels={'x': 'Video Category', 'y': 'Time Spent On Video'}, title='Time Spent on Videos')
st.plotly_chart(fig)

# 5. Average Satisfaction Score
st.subheader("Average Satisfaction Score by Profession")
avg_satisfaction = df.groupby('Profession')['Satisfaction'].mean().reset_index()
fig = px.bar(avg_satisfaction, x='Profession', y='Satisfaction', labels={'x': 'Profession', 'y': 'Satisfaction'}, title='Satisfaction by Profession')
st.plotly_chart(fig)

# 6. Debt to Income Ratio
st.subheader("Debt to Income Ratio Distribution")
df['Debt to Income Ratio'] = df['Debt'] / df['Income'].replace(0, 1)
fig = px.line(df, x=df.index, y='Debt to Income Ratio', labels={'x': 'Index', 'y': 'Debt to Income Ratio'}, title='Debt to Income Ratio Distribution')
st.plotly_chart(fig)

# 7. Video Watch Time by Device Type
st.subheader("Watch Time by Device Type")
device_watch_time = df.groupby('DeviceType')['Watch Time'].sum().reset_index()
fig = px.bar(device_watch_time, x='DeviceType', y='Watch Time', labels={'x': 'Device Type', 'y': 'Watch Time'}, title='Watch Time by Device Type')
st.plotly_chart(fig)

# 8. Scroll Rate by Video Length
st.subheader("Scroll Rate by Video Length")
scroll_rate_length = df.groupby('Video Length')['Scroll Rate'].mean().reset_index()
fig = px.line(scroll_rate_length, x='Video Length', y='Scroll Rate', labels={'x': 'Video Length', 'y': 'Scroll Rate'}, title='Scroll Rate by Video Length')
st.plotly_chart(fig)

# 9. Engagement Over Time
st.subheader("Engagement Over Time")
engagement_over_time = df.groupby('Platform')['Engagement'].mean().reset_index()
fig = px.line(engagement_over_time, x='Platform', y='Engagement', labels={'x': 'Platform', 'y': 'Engagement'}, title='Engagement Over Time')
st.plotly_chart(fig)
