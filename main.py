import requests
import time
import matplotlib.pyplot as plt

# Store results
ministry_limits = []
times_taken = []

print("📡 Ministry/Department API Benchmarking Tool")

while True:
    try:
        limit = int(input("\n🔢 Enter number of ministries to fetch (limit): "))
    except ValueError:
        print("❌ Please enter a valid integer.")
        continue

    url = f"http://localhost:8080/ministries/paginated?limit={limit}&offset=0"

    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    elapsed = end_time - start_time

    if response.status_code == 200:
        data = response.json()
        ministry_count = len(data)

        print(f"✅ Status: {response.status_code}")
        print(f"📊 Fetched {ministry_count} ministries")
        print(f"⏱️ Time taken: {elapsed:.4f} seconds")

        ministry_limits.append(f"{ministry_count}M")
        times_taken.append(elapsed)
    else:
        print(f"❌ Request failed with status: {response.status_code}")
        continue

    choice = input("🔁 Do you want to test again? (y/n): ").strip().lower()
    while choice not in ["y", "n"]:
        choice = input("Please enter 'y' to continue or 'n' to exit: ").strip().lower()

    if choice == "n":
        break

# Plotting
plt.figure(figsize=(10, 6))
points = plt.plot(ministry_limits, times_taken, marker='o', linestyle='-', color='blue')
plt.title("⏱️ API Time vs Ministries Fetched")
plt.xlabel("Ministries Fetched (M = Ministry)")
plt.ylabel("Time Taken (seconds)")
plt.grid(True)

# Add time value annotations above each point
for i, txt in enumerate(times_taken):
    plt.annotate(f"{txt:.2f}s", (ministry_limits[i] , times_taken[i]), textcoords="offset points", xytext=(0, 8), ha='center')

plt.tight_layout()
plt.show()
