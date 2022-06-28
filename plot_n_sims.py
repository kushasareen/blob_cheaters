import sys
import numpy as np
import matplotlib.pyplot as plt
from run_sim import run_sim

if __name__ == "__main__":
	# usage: python plot_n_sims [number of sims to plot]
	n = int(sys.argv[1])

	results = [run_sim(verbose = False, keep_list = True) for _ in range(n)]
	max_score = max([x[0] for x in results])
	print("The max score was", max_score)

	for i in range(n):
		plt.plot(results[i][2], results[i][1])

	plt.xlabel("Score")
	plt.ylabel("Flips")
	plt.show()