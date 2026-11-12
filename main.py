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

print(f"Average goals out of {shots} shots: {math.floor(avg_goals)}")
print(f"Standard deviation: {std_dev:.2f}")
print(f"Best case in simulation: {best_case}")
print(f"Worst case in simulation: {worst_case}")

