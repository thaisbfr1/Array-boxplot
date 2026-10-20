import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\ssilva.thais\OneDrive - SENAC RIO\DADOS\funcionarios.csv")

print(df)

salario = df["salario"].to_numpy()

print(salario)

Q1 = np.percentile(salario, 25)
Q2 = np.percentile(salario, 50)
Q3 = np.percentile(salario, 75)

print ("primeiro Quartil\n")
print (Q1)
print ("\nMediana\n")
print (Q2)
print ("terceiro Quartil\n")
print (Q3)