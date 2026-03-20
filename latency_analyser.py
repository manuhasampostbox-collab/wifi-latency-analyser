import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time

def simulate_ping(host, count=50):
    delays = []
    print(f"Simulating {count} pings...")
    for i in range(count):
        delay = np.random.exponential(scale=20) + np.random.uniform(1, 5)
        delays.append(delay)
        time.sleep(0.05)
    return delays

def analyse_latency(delays, label="Network"):
    delays = np.array(delays)
    print(f"\n--- {label} Latency Analysis ---")
    print(f"Min delay:    {np.min(delays):.2f} ms")
    print(f"Max delay:    {np.max(delays):.2f} ms")
    print(f"Mean delay:   {np.mean(delays):.2f} ms")
    print(f"Median delay: {np.median(delays):.2f} ms")
    print(f"Std deviation:{np.std(delays):.2f} ms")
    print(f"95th percentile: {np.percentile(delays, 95):.2f} ms")
    return delays

delays_light = simulate_ping("light-load", count=100)
delays_heavy = [d * 3.5 + np.random.uniform(0,10)
                for d in simulate_ping("heavy-load", count=100)]

analyse_latency(delays_light, "Light Traffic")
analyse_latency(delays_heavy, "Heavy Traffic")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(delays_light, color='steelblue', linewidth=0.8)
plt.axhline(np.mean(delays_light), color='red',
            linestyle='--', label='Mean')
plt.title('Light Traffic Latency')
plt.xlabel('Packet number')
plt.ylabel('Delay (ms)')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(delays_heavy, color='tomato', linewidth=0.8)
plt.axhline(np.mean(delays_heavy), color='blue',
            linestyle='--', label='Mean')
plt.title('Heavy Traffic Latency')
plt.xlabel('Packet number')
plt.ylabel('Delay (ms)')
plt.legend()

plt.suptitle('Wi-Fi Latency Analysis: Light vs Heavy Traffic', fontsize=13)
plt.tight_layout()
plt.savefig('latency_results.png')
print("\nChart saved as latency_results.png")

