import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\ssilva.thais\OneDrive - SENAC RIO\DADOS\funcionarios.csv")

print(df)

lucro = df["lucro"].to_numpy()


Q1 = np.percentile(lucro, 25)
Q2 = np.percentile(lucro, 50)
Q3 = np.percentile(lucro, 75)

print("\n")
print (Q1)
print(Q2)
print(Q3)

i = Q3 - Q1
Limite_inferior = Q1 - 1.5 * i

Limite_max = Q3 + 1.5 * i

outliers = lucro[(lucro < Limite_inferior) | (lucro > Limite_max)]

dentro = lucro[(lucro >= Limite_inferior) & (lucro <= Limite_max)]
bigode_inf = dentro.min()
bigode_sup = dentro.max()

print("Limite inferior: \n")
print(Limite_inferior)
print("\nLimite Superior: \n")
print(Limite_max)
print("\nOutliers: \n")
print(outliers)
print("\nBigode inferior: \n")
print(bigode_inf)
print("\nBigode superior: \n")
print(bigode_sup)