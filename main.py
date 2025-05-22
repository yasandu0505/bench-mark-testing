import requests
import time

url = "http://localhost:8080/ministries/paginated?limit=100000&offset=0"

start_time = time.time()
response = requests.get(url)
end_time = time.time()

elapsed = end_time - start_time
print(f"⏱️ Time taken: {elapsed:.4f} seconds")

# Optional: print a sample of the response
print("Status:", response.status_code)
 
