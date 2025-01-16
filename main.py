import streamlit as st
import pandas as pd


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
filtered_df = df[(df['Gender'] == selected_gender) & (df['Age'].between(age_range[0], age_range[1]))&(df['Platform'].isin(platform_filter))]

st.subheader("Key Performance Indicators")
st.metric("Total Time Spent (hours)", int(filtered_df['Total Time Spent'].sum()))
st.metric("Average Productivity Loss", round(filtered_df['ProductivityLoss'].mean(), 2))
st.metric("Average Addiction Level", round(filtered_df['Addiction Level'].mean(), 2))


# 1. User Demographics Distribution
st.subheader("User Demographics")
gender_counts = filtered_df['Gender'].value_counts()
st.bar_chart(gender_counts)

# 2. Income vs. Debt
st.subheader("Income vs. Debt")
income_debt_data = filtered_df[['Income', 'Debt']]
st.write("Income vs. Debt Scatter Plot")
st.scatter_chart(income_debt_data)

# 3. Engagement by Platform
st.subheader("Engagement by Platform")
platform_engagement = df.groupby('Platform')['Engagement'].sum().reset_index()
st.bar_chart(platform_engagement.set_index('Platform')['Engagement'])

# 4. Average Time Spent on Videos by Category
st.subheader("Average Time Spent on Videos by Category")
avg_time = df.groupby('Video Category')['Time Spent On Video'].mean().reset_index()
st.line_chart(avg_time.set_index('Video Category')['Time Spent On Video'])

# 5. Average Satisfaction Score
st.subheader("Average Satisfaction Score by Profession")
avg_satisfaction = df.groupby('Profession')['Satisfaction'].mean().reset_index()
st.bar_chart(avg_satisfaction.set_index('Profession')['Satisfaction'])

# 6. Debt to Income Ratio
st.subheader("Debt to Income Ratio Distribution")
df['Debt to Income Ratio'] = df['Debt'] / df['Income'].replace(0, 1)  # Avoid division by zero
st.line_chart(df['Debt to Income Ratio'])

# 7. Video Watch Time by Device Type
st.subheader("Watch Time by Device Type")
device_watch_time = df.groupby('DeviceType')['Watch Time'].sum().reset_index()
st.bar_chart(device_watch_time.set_index('DeviceType')['Watch Time'])

# 8. Scroll Rate by Video Length
st.subheader("Scroll Rate by Video Length")
scroll_rate_length = df[['Video Length', 'Scroll Rate']].groupby('Video Length').mean().reset_index()
st.line_chart(scroll_rate_length.set_index('Video Length')['Scroll Rate'])

# 9. Engagement Over Time
st.subheader("Engagement Over Time")
engagement_over_time = df.groupby('Platform')['Engagement'].mean().reset_index()
st.line_chart(engagement_over_time.set_index('Platform')['Engagement'])

