import numpy as np 
import math
import matplotlib.pyplot as plt


rng = np.random.default_rng(seed=5)

shots = 100
goal_prob = 0.176
simulations = 1000

bin_results = rng.binomial(shots, goal_prob, size=simulations)

avg_goals = np.mean(bin_results)
std_dev = np.std(bin_results)
best_case = np.max(bin_results)
worst_case = np.min(bin_results)
expected_goals = shots * goal_prob

print(f"Average goals out of {shots} shots: {math.floor(avg_goals)}")
print(f"Standard deviation: {std_dev:.2f}")
print(f"Best case in simulation: {best_case}")
print(f"Worst case in simulation: {worst_case}")
print(f"Expected goals: {expected_goals:.1f}")

bins = np.arange(bin_results.min(), bin_results.max() + 2) - 0.5
plt.hist(bin_results, bins=bins, color="mediumturquoise", edgecolor="black", alpha=0.8)
plt.axvline(avg_goals, color="midnightblue", linestyle="dashed", linewidth=3)
plt.text(avg_goals + 0.5, plt.ylim()[1] * 0.93, f"avg {avg_goals:.1f}", color="midnightblue") # (x, y, text)
plt.title("Tye Kartye Goals Over 100 Shots")
plt.xlabel("Number of Goals")
plt.ylabel("Number of Simulations")
plt.text(0.05, 0.95,
         f"Expected Goals: {expected_goals:.1f}\nSim Avg: {avg_goals:.1f}",
         transform=plt.gca().transAxes,  #axis coords
         va="top",
         bbox=dict(facecolor="white", alpha=0.8))
plt.show()