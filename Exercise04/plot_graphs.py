import csv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def load(path):
    np_, t = [], []
    with open(path) as f:
        for row in csv.DictReader(f):
            np_.append(int(row["np"]))
            t.append(float(row["time"]))
    return np_, t

series = {"Sum (Ex2)": load("sum_times.csv"), "Monte Carlo Pi (Ex3)": load("pi_times.csv")}

plt.figure()
for label, (n, t) in series.items():
    plt.plot(n, t, marker="o", label=label)
plt.xlabel("Number of processes")
plt.ylabel("Time (seconds)")
plt.title("Time vs Number of Processes")
plt.xticks([1, 2, 4, 8])
plt.legend()
plt.grid(True)
plt.savefig("time_vs_processes.png", dpi=150)

plt.figure()
for label, (n, t) in series.items():
    plt.plot(n, [t[0] / x for x in t], marker="o", label=label)
plt.plot([1, 2, 4, 8], [1, 2, 4, 8], "--", label="Ideal")
plt.xlabel("Number of processes")
plt.ylabel("Speedup (T1 / Tn)")
plt.title("Speedup vs Number of Processes")
plt.xticks([1, 2, 4, 8])
plt.legend()
plt.grid(True)
plt.savefig("speedup.png", dpi=150)
print("saved time_vs_processes.png and speedup.png")
