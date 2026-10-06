import numpy as np
from scipy import stats

dados = np.random.normal(0, 1, 1000)

media = 0
std = 1

ppf = stats.norm.ppf(0.25, loc = media, scale = std)

pct_neg = stats.norm.cdf(0, loc = media, scale = std)

print(pct_neg)

print(ppf)

