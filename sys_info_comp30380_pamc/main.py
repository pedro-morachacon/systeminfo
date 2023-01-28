import psutil
import os
import platform
import socket

# Get machine name
machine_name = socket.gethostname()

# Get operating system name
os_name = platform.system()

# Get operating system version
os_version = platform.release()

# Get number of CPU's
num_cpus = os.cpu_count()

# Get amount of memory
memory = psutil.virtual_memory()  #.total / (1024.0 ** 3)

# Get IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Print the #1 to 6 information
print("1. Machine Name: ", machine_name)
print("2. Operating System: ", os_name)
print("3. Operating System Version: ", os_version)
print("4. Number of CPU's: ", num_cpus)
print("5. Amount of Memory:", memory, "GB")
print("6. IP Address: ", ip_address)

# For #7 information using the sample code 1 at page 5 of the practical slides 
import timeit 
import math 
import itertools

def bench_pidigits(ndigits=1000, loops=100):

	def calc_ndigits(n) :
		# Adapted from code on http://shootout.alioth.debian.org/
		def gen_x() :
			return map(lambda k: (k, 4*k + 2, 0, 2*k + 1), itertools.count(1)) 

		def compose(a, b):
			aq, ar, as_, at = a
			bq, br, bs, bt = b
			return (aq * bq,
				aq * br + ar * bt, 
				as_ * bq + at * bs, 
				as_ * br + at * bt)

		def extract(z, j):
			q, r, s, t = z
			return (q*j + r) // (s*j + t)

		def pi_digits():
			z = (1, 0, 0, 1)
			x = gen_x()
			while 1:
				y = extract(z, 3)
				while y != extract(z, 4):
					z = compose(z, next(x))
					y = extract(z, 3)
				z = compose((10, -10*y, 0, 1), z)
				yield y

		return list(itertools.islice(pi_digits(), n))

	for _ in range(loops):
		calc_ndigits(ndigits)
	#print ('Pi:', , "' •Join (map(str, calc_ndigits (ndigits))))
	return

	#return perf.perf_counter() - to

if __name__ == '__main__':
	t_default = 6.388216104
	start_time = timeit.default_timer()
	bench_pidigits(ndigits=1000, loops=100)
	elapsed_time = timeit.default_timer() - start_time
	print('7. CPU strength score(relative elapsed):', elapsed_time/t_default)
print()