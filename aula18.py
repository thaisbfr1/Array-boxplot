import pandas as pd

df1 = pd.read_csv(r"C:\Users\ssilva.thais\OneDrive - SENAC RIO\DADOS\funcionarios.csv")
df2 = pd.read_csv(r"C:\Users\ssilva.thais\OneDrive - SENAC RIO\DADOS\funcionarios_v2.csv")


resultado_vertical = pd.concat([df1,df2])

print (resultado_vertical)