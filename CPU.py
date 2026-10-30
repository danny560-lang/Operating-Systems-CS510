import psutil

# Display CPU usage percentage
cpu_usage = psutil.cpu_percent(interval=1)
print(f"CPU Usage Percentage: {cpu_usage}%")

# Display number of CPU cores
cpu_count = psutil.cpu_count(logical=True)
print(f"CPU Count: {cpu_count}")

# Display total memory available
memory_info = psutil.virtual_memory()
total_memory = memory_info.total / (1024 ** 3)  # Convert bytes to GB
print(f"Total Memory Available: {total_memory:.2f} GB")

# Display memory usage percentage
memory_usage = memory_info.percent
print(f"Memory Usage: {memory_usage}%")