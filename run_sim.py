import numpy as np
from strategist import p_fair, E_guess, E_flip

def flip(p_h):
	if np.random.random() < p_h:
		return "h"
	else:
		return "t"

def get_identity():
	# returns pair (p_h, p_t)
	identity = np.random.randint(2) # 0 = fair, 1 = cheater
	if identity == 0:
		return (0.5, 0.5)
	else:
		return (0.75, 0.25)

def run_sim(verbose = False, keep_list = True):
	H = 0
	T = 0
	score = 0
	flips = 100
	if keep_list:
		flip_list = [100]
		score_list = [0]
	else:
		flip_list = None
		score_list = None

	p_h, p_t = get_identity()

	while flips >= 0:
		if E_flip(H, T) > E_guess(H, T) and flips != 0: # flip a coin
			flips -= 1
			f = flip(p_h)
			if f == "h":
				H += 1
			else:
				T += 1

			if verbose: print("(H, T):", H, T)

		else: # make a guess
			if p_fair(H,T) > 0.5: # guess fair
				if p_h == 0.5: # is fair
					flips += 15
					score += 1
					if verbose: print("Correctly guessed fair")
				else:
					flips -= 30
					if verbose: print("Incorrectly guessed fair")

			else: # guess cheater
				if p_h == 0.75: # is cheater
					flips += 15
					score += 1
					if verbose: print("Correctly guessed cheater")

				else:
					flips -= 30
					if verbose: print("Incorrectly guessed cheater")


			p_h, p_t = get_identity()
			H = 0
			T = 0
			if verbose: print("Score:", score, "Flips:", flips)
			if keep_list: flip_list.append(max(flips, 0))
			if keep_list: score_list.append(score)


	return score, flip_list, score_list



if __name__ == "__main__":
	out, _, _ = run_sim(verbose = True, keep_list = False)
	print("The final score is " + str(out) + "!")