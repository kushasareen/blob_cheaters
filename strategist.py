import numpy as np
fudge_util = 0

# must instead build a table

def build_E_flip_table(max_heads = 100, max_tails = 50):
	E_flip_table = np.zeros((max_heads, max_tails))
	for h in reversed(range(max_heads-1)):
		for t in reversed(range(max_tails-1)):
			p = p_fair(h,t)
			p_head = 0.5*p + 0.75*(1-p)
			p_tail = 1 - p_head
			E_flip_table[h][t] = (max(E_guess(h+1,t), E_flip_table[h+1,t])*p_head + max(E_guess(h,t+1), E_flip_table[h,t+1])*p_tail) - 1

	return E_flip_table

def E_flip(h,t,m):
	return m[h,t]

def p_fair(h,t):
	# Baysian probability of a fair blob given number of heads and tails
	return (0.5**h*0.5**t)/(0.5**h*0.5**t + 0.75**h*0.25**t)

def E_guess(h,t,matrix = None):
	# Expected value of guessing
	p = p_fair(h,t)
	return max(p, 1-p)*15 - min(p, 1-p)*30

def E_flip_naive(h,t):
	# Expected value of flipping once more
	p = p_fair(h,t)
	p_head = 0.5*p + 0.75*(1-p)
	p_tail = 1 - p_head
	# return (E_guess(h+1,t)*p_head + E_guess(h,t+1)*p_tail - E_guess(h,t))
	return (E_guess(h+1,t)*p_head + E_guess(h,t+1)*p_tail) - 1

if __name__ == "__main__":

	H = 0
	T = 0
	M = build_E_flip_table()
	print("Welcome to the blob game stategist. Enter your flip to get the next move or q to quit.")

	while True:
		flip = input("(H:" + str(H) + ", T:" + str(T)+ ") Enter the next flip: ")
		if flip.lower() == "q": break

		if flip.lower() == "h" or flip.lower() == "heads":
			H += 1
		elif flip.lower() == "t" or flip.lower() == "tails":
			T += 1
		else:
			print("Invalid")
			continue


		if E_flip(H, T, M) > E_guess(H, T):
			print("flip")
		else:
			if p_fair(H,T) > 0.5:
				print("Guess fair")
			else:
				print("Guess cheater")

			H = 0
			T = 0
			input("Let's go again!")