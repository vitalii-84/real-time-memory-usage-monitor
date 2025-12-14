import time
import psutil
import streamlit as st
import pandas as pd

# Function to get memory usage
def memory_usage():
    return psutil.virtual_memory().percent

# Function to simulate high memory load for 10 seconds
def simulate_memory_load(duration=10):
    load_data = []
    end_time = time.time() + duration
    while time.time() < end_time:
        # Significantly increase data block size to increase memory usage (around 100MB per iteration)
        load_data.append([0] * 10**6)  # Approximately 100MB of data per iteration
        time.sleep(0.1)  # Control the load rate to sustain the load over time

# Title of the app
st.title("Real-Time Memory Usage Monitor")

# Button to trigger memory load simulation
if st.button("Simulate Memory Load for 10 Seconds"):
    st.write("Simulating memory usage for 10 seconds...")
    simulate_memory_load()

# Initialize the metric display and chart
memory_metric = st.metric(label="Current Memory Usage", value="0%")
memory_chart = st.line_chart([])

# List to store memory usage data over time
memory_data = []

# Real-time update loop
while True:
    # Get current memory usage
    current_memory = memory_usage()
    
    # Update metric display
    memory_metric.metric(label="Current Memory Usage", value=f"{current_memory}%")
    
    # Append current memory usage to the list
    memory_data.append(current_memory)
    
    # Convert memory data to DataFrame for the chart
    memory_df = pd.DataFrame(memory_data, columns=["Memory Usage (%)"])
    
    # Update the chart
    memory_chart.line_chart(memory_df)
    
    # Pause for 1 second
    time.sleep(5)
