import numpy as np
import matplotlib.pyplot as plt
from spot import bidSPOT
import pandas as pd

# f = '2015Well_1.csv'
# r = pd.read_csv(f)
# r = r['water_level'].dropna()

f = 'AG_NO3.csv'
r = pd.read_csv(f)
r = r['NO3N'].dropna()
r = pd.to_numeric(r,errors='coerce')

X = r.values

n_init = 1000
init_data = X[:n_init] 	# initial batch
data = X[n_init:]  		# stream

q = 1e-3 				# risk parameter
d = 450  				# depth parameter
s = bidSPOT(q,d)     	# biDSPOT object
s.fit(init_data,data) 	# data import
s.initialize() 	  		# initialization step
results = s.run()    	# run
s.plot(results) 	 	# plot

plt.show()