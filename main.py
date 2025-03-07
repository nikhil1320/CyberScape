import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


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
fig, ax = plt.subplots()
gender_counts.plot(kind='bar', ax=ax)
ax.set_xlabel("Gender")
ax.set_ylabel("Count")
st.pyplot(fig)

# 2. Income vs. Debt
st.subheader("Income vs. Debt")
fig, ax = plt.subplots()
ax.scatter(filtered_df['Income'], filtered_df['Debt'])
ax.set_xlabel("Income")
ax.set_ylabel("Debt")
st.pyplot(fig)

# 3. Engagement by Platform
st.subheader("Engagement by Platform")
platform_engagement = df.groupby('Platform')['Engagement'].sum().reset_index()
fig, ax = plt.subplots()
platform_engagement.plot(kind='bar', x='Platform', y='Engagement', ax=ax, legend=False)
ax.set_xlabel("Platform")
ax.set_ylabel("Engagement")
st.pyplot(fig)

# 4. Average Time Spent on Videos by Category
st.subheader("Average Time Spent on Videos by Category")
avg_time = df.groupby('Video Category')['Time Spent On Video'].mean().reset_index()
fig, ax = plt.subplots()
avg_time.plot(kind='line', x='Video Category', y='Time Spent On Video', ax=ax, legend=False)
ax.set_xlabel("Video Category")
ax.set_ylabel("Time Spent On Video")
st.pyplot(fig)

# 5. Average Satisfaction Score
st.subheader("Average Satisfaction Score by Profession")
avg_satisfaction = df.groupby('Profession')['Satisfaction'].mean().reset_index()
fig, ax = plt.subplots()
avg_satisfaction.plot(kind='bar', x='Profession', y='Satisfaction', ax=ax, legend=False)
ax.set_xlabel("Profession")
ax.set_ylabel("Satisfaction")
st.pyplot(fig)

# 6. Debt to Income Ratio
st.subheader("Debt to Income Ratio Distribution")
df['Debt to Income Ratio'] = df['Debt'] / df['Income'].replace(0, 1)  # Avoid division by zero
fig, ax = plt.subplots()
df['Debt to Income Ratio'].plot(kind='line', ax=ax)
ax.set_xlabel("Index")
ax.set_ylabel("Debt to Income Ratio")
st.pyplot(fig)

# 7. Video Watch Time by Device Type
st.subheader("Watch Time by Device Type")
device_watch_time = df.groupby('DeviceType')['Watch Time'].sum().reset_index()
fig, ax = plt.subplots()
device_watch_time.plot(kind='bar', x='DeviceType', y='Watch Time', ax=ax, legend=False)
ax.set_xlabel("Device Type")
ax.set_ylabel("Watch Time")
st.pyplot(fig)

# 8. Scroll Rate by Video Length
st.subheader("Scroll Rate by Video Length")
scroll_rate_length = df[['Video Length', 'Scroll Rate']].groupby('Video Length').mean().reset_index()
fig, ax = plt.subplots()
scroll_rate_length.plot(kind='line', x='Video Length', y='Scroll Rate', ax=ax, legend=False)
ax.set_xlabel("Video Length")
ax.set_ylabel("Scroll Rate")
st.pyplot(fig)

# 9. Engagement Over Time
st.subheader("Engagement Over Time")
engagement_over_time = df.groupby('Platform')['Engagement'].mean().reset_index()
fig, ax = plt.subplots()
engagement_over_time.plot(kind='line', x='Platform', y='Engagement', ax=ax, legend=False)
ax.set_xlabel("Platform")
ax.set_ylabel("Engagement")
st.pyplot(fig)
