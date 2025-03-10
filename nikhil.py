import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data

df = pd.read_csv('Time-Wasters on Social Media.csv')

# Title and Introduction
st.title("User Engagement Dashboard")
st.write("Explore insights and KPIs from user engagement data.")

# Key Metrics at the top
st.subheader("Key Metrics")
st.metric("Total Time Spent (hours)", int(df['Total Time Spent'].sum()))
st.metric("Total Engagement", int(df['Engagement'].sum()))
st.metric("Average Satisfaction", round(df['Satisfaction'].mean(), 2))

# Sidebar for Filters
st.sidebar.header("Filters")

# Gender Filter (with Select All Option)
gender_options = ['All'] + list(df['Gender'].unique())  
selected_gender = st.sidebar.selectbox("Select Gender", gender_options)

# Age Range Filter
age_range = st.sidebar.slider("Select Age Range", 0, 100, (20, 50))


# Platform Filter (with Select All Option)
platform_options = ['All'] + list(df['Platform'].unique())  # Add "All" to the platform filter
platform_filter = st.sidebar.multiselect("Select Platform", options=platform_options, default=df.Platform.unique())


# Filter data based on selections
filtered_df = df[(df['Gender'] == selected_gender) & (df['Age'].between(age_range[0], age_range[1]))&(df['Platform'].isin(platform_filter))]

# Apply Filter
if selected_gender != 'All':
    filtered_df = df[df['Gender'] == selected_gender]
else:
    filtered_df = df.copy()

# 1. **Most Watched Videos by Time of Day**
st.subheader("Most Watched Videos by Time of Day")
fig, ax = plt.subplots(figsize=(8, 5))  # Define fig, ax
ax.bar(df['Watch Time'], df['Video ID'], color='skyblue')
ax.set_title('Most Watched Videos by Time of Day')
ax.set_xlabel('Time of Day')
ax.set_ylabel('Number of Views')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

# 2. **Platform with Most Engagement**
st.subheader("Platform with Most Engagement")
platform_engagement = filtered_df.groupby('Platform')['Engagement'].sum().reset_index()
fig, ax = plt.subplots()
ax.bar(platform_engagement['Platform'], platform_engagement['Engagement'], color='green')
ax.set_title('Platform with Most Engagement')
ax.set_xlabel('Platform')
ax.set_ylabel('Total Engagement')
plt.xticks(rotation=45)
st.pyplot(fig)

# 3. **Short vs Long Videos**
st.subheader("Short vs Long Videos")
filtered_df['Video Length Category'] = filtered_df['Video Length'].apply(lambda x: 'Short Video' if x <= 10 else 'Long Video')
video_length = filtered_df.groupby('Video Length Category')['Video ID'].count().reset_index()
fig, ax = plt.subplots()
ax.bar(video_length['Video Length Category'], video_length['Video ID'], color='purple')
ax.set_title('Short vs Long Videos')
ax.set_xlabel('Video Length Category')
ax.set_ylabel('Number of Views')
st.pyplot(fig)

# 4. **Satisfaction by Profession**
st.subheader("Satisfaction by Profession")
satisfaction_by_profession = filtered_df.groupby('Profession')['Satisfaction'].mean().reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(x='Satisfaction', y='Profession', data=satisfaction_by_profession, ax=ax, palette='coolwarm')
ax.set_title('Satisfaction by Profession')
ax.set_xlabel('Average Satisfaction')
ax.set_ylabel('Profession')
st.pyplot(fig)

# 5. **Engagement by Location**
st.subheader("Engagement by Location")
location_engagement = filtered_df.groupby('Location').agg({'Engagement': 'sum'}).reset_index()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(location_engagement['Location'], location_engagement['Engagement'], color='orange')
ax.set_title('Engagement by Location')
ax.set_xlabel('Location')
ax.set_ylabel('Total Engagement')
plt.xticks(rotation=45)
st.pyplot(fig)

# 6. **Number of Sessions**
st.subheader("Number of Sessions")
sessions_count = filtered_df.groupby('Number of Sessions')['Video ID'].count().reset_index()
fig, ax = plt.subplots()
ax.plot(sessions_count['Number of Sessions'], sessions_count['Video ID'], marker='o', color='blue')
ax.set_title('Sessions vs Video Views')
ax.set_xlabel('Number of Sessions')
ax.set_ylabel('Number of Views')
st.pyplot(fig)

# 7. **Satisfaction Rate**
st.subheader("Satisfaction Rate")
satisfaction = filtered_df.groupby('Satisfaction')['Video ID'].count().reset_index()
fig, ax = plt.subplots()
sns.barplot(x='Satisfaction', y='Video ID', data=satisfaction, ax=ax, palette='coolwarm')
ax.set_title('Satisfaction Rate')
ax.set_xlabel('Satisfaction Level')
ax.set_ylabel('Number of Views')
st.pyplot(fig)







