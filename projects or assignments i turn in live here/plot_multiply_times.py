# Not part of the karatsuba.py submission -- run separately after the
# benchmark (`python karatsuba.py`) has produced multiply_times.csv.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
data = pd.read_csv('multiply_times.csv')
plot = sns.relplot(data=data, kind='line', x='n', y='time', hue='algorithm', marker='o')
plot.set(xscale='log', yscale='log')
plot.savefig('multiply_times.png')

# TODO: also compute and print the measured exponent per algorithm
# (slope of the log-log line) -- see the np.polyfit snippet in the
# assignment spec, and compare it to your predicted exponents in your
# write-up.
