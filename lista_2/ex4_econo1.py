beta0 = 0.000448
beta1 = 198.478453

delta_selic = [0.01, 0.05, 0.1, 0.3]

for selic in delta_selic:
    print()
    print(f"Previsão para {selic}")
    print(beta0 + beta1*selic)