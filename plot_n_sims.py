import sys
import numpy as np
import matplotlib.pyplot as plt
from run_sim import run_sim
from strategist import build_E_flip_table

if __name__ == "__main__":
	# usage: python plot_n_sims [number of sims to plot]
	n = int(sys.argv[1])
	# M = build_E_flip_table()
	M = None

	results = [run_sim(verbose = False, keep_list = True, matrix = M) for _ in range(n)]
	scores = [x[0] for x in results]
	max_score = max(scores)
	print("The max score was", max_score)
	print("The average score was", int(np.mean(scores)), "+-", int(np.std(scores)))


	for i in range(n):
		plt.plot(results[i][2], results[i][1])

	plt.xlabel("Score")
	plt.ylabel("Flips")
	plt.show()