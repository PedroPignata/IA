import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

column_names = ["Date", "Time", "Home_Team", "Score", "Away_Team", "Audience", "Stadium"]
df = pd.read_csv("/home/ubuntu/upload/Brasileiro2024(SrieA)-Dataset-Final.csv", header=None, names=column_names)

df["Audience"] = df["Audience"].str.replace(",", "", regex=False).astype(float)

df[["Home_Score", "Away_Score"]] = df["Score"].str.split("–", expand=True)
df["Home_Score"] = pd.to_numeric(df["Home_Score"])
df["Away_Score"] = pd.to_numeric(df["Away_Score"])
df["Total_Goals"] = df["Home_Score"] + df["Away_Score"]

# Calcular a matriz de correlação
correlation_matrix = df[["Audience", "Home_Score", "Away_Score", "Total_Goals"]].corr()

# Criar o mapa de calor
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Mapa de Calor das Correlações\n entre Variáveis Numéricas')
plt.savefig('correlation_heatmap.png')
print('Mapa de calor salvo como correlation_heatmap.png')

