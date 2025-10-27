autores = ["Renzo Vecchioni", "Matheus Mendes"]

# =============================================================
# AULA 3 --- Integração com NumPy e Matplotlib - Versão do Aluno
#
# Você irá simular um estudo de consumo de energia residencial ao longo de 180 dias, criando 
# dados sintéticos com comportamento realista e depois analisando e visualizando padrões desse 
# conjunto. Baseado em um conjunto de dados do Kaggle.
#
# O cenário é um conjunto de dados ambientais e de consumo energético, modelando como a 
# temperatura influencia o uso de energia em um ambiente doméstico:
#
# Temperatura diária (temp): simulada como uma série senoidal (representando ciclos de 
# aquecimento e resfriamento, como as variações sazonais do clima) acrescida de ruído aleatório.
#
# Consumo de energia (energy): criado como uma função da temperatura --- quanto mais distante do
# “conforto térmico” (22 °C), maior o consumo de energia (para aquecimento ou refrigeração).
#
# Anomalias (“spikes”): representam picos de consumo atípicos, simulando eventos reais
# (equipamentos defeituosos, dias de uso intenso, etc.).
#
# HDD/CDD (Heating/Cooling Degree Days): métricas derivadas amplamente usadas em engenharia 
# térmica e modelagem energética, que quantificam quanto a temperatura de um dia se desvia do 
# ideal de conforto.
#
# Média móvel (MA7): suaviza flutuações e ajuda a observar tendências sazonais ou de longo prazo.
# =============================================================

# -----------------------------
# PARTE A --- Setup e Dados
# -----------------------------

# 1) IMPORTS E SEMENTE
# TODO: importe numpy como np, pandas como pd e matplotlib.pyplot como plt
# TODO: importe AutoDateLocator e ConciseDateFormatter
# TODO: fixe a semente aleatória com np.random.seed(42)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateLocator, ConciseDateFormatter
np.random.seed(42)

# 2) PARÂMETROS DO EXPERIMENTO
# TODO: defina N=180, base_temp=22.0, amp=8.0, noise_temp=1.5, noise_energy=10.0
N = 180
base_temp = 22.0
amp = 8.0
noise_temp = 1.5
noise_energy = 10.0

# 3) EIXO TEMPORAL
# TODO: crie um índice de datas diárias começando em "2025-01-01" com N períodos (date_range)
# TODO: crie um vetor t com np.arange(N)
dates = pd.date_range(start="2025-01-01", periods=N)
t = np.arange(N)

# 4) TEMPERATURA SINTÉTICA (NumPy)
# TODO: calcule temp = base_temp + amp*np.sin(2*np.pi*t/30) + ruído normal(0, noise_temp, N)
# Dica: use np.random.normal(0, noise_temp, N)
temp = base_temp+amp*np.sin(2*np.pi*t/30) + np.random.normal(0, noise_temp, N)

# 5) CONSUMO DE ENERGIA SINTÉTICO (NumPy)
# Relação pragmática (sem estatística): quanto mais distante do conforto, maior o consumo.
# TODO: energy = 200 + 5*np.abs(temp - base_temp) + ruído normal(0, noise_energy, N)
energy = 200 + 5 * np.abs(temp - base_temp) + np.random.normal(0, noise_energy, N)

# 6) SPIKES (ANOMALIAS)
# TODO: escolha 3 índices aleatórios distintos com np.random.choice(N, 3, replace=False)
# TODO: some 80.0 ao consumo nesses índices
idx_spike = np.random.choice(N, 3, replace=False)
energy[idx_spike] += 80.0

# 7) DATAFRAME COM ÍNDICE TEMPORAL
# TODO: crie df = pd.DataFrame({"temp": temp, "energy": energy}, index=dates)
# TODO: exiba head() e describe().T
df = pd.DataFrame({"temp": temp, "energy": energy}, index=dates)

print(df.head(), "\n")
print(df.describe().T, "\n")

# 8) COLUNAS DERIVADAS (NumPy + pandas)
# TODO: Pesquise e utilize clip() para HDD e CDD

df["HDD"] = np.clip(base_temp - df["temp"], 0, None)
df["CDD"] = np.clip(df["temp"] - base_temp, 0, None)

# TODO: calcule média móvel de 7 dias de "temp" com convolução NumPy (kernel de uns/7)
kernel = np.ones(7) / 7
df["temp_ma7"] = np.convolve(df["temp"], kernel, mode="same")
print(df.head(10))

# ----------------------------------------------
# PARTE B --- Visualizações Avançadas
# ----------------------------------------------

# 9) PREPARAR FIGURA E FORMATADORES DE DATA
# TODO: crie uma figura com tamanho (12, 8)
# TODO: pesquise e utilize gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25)
# TODO: pesquise e utilize locator = AutoDateLocator() e fmt = ConciseDateFormatter(locator)
fig = plt.figure(figsize=(12, 8))
gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.25)
locator = AutoDateLocator()
fmt = ConciseDateFormatter(locator)

# 10) (Ax1) SÉRIE TEMPORAL: LINHA + MÉDIA MÓVEL + ÁREAS
# TODO: ax1 = fig.add_subplot(gs[0, 0])
# TODO: plote temperatura com espessura de linha de 1.0
# TODO: plote df["temp_ma7"] (lw=2.0, label="Média móvel (7d)")
# TODO: use fill_between para destacar regiões acima/abaixo de base_temp com alpha=0.15
# TODO: configure título, ylabel="°C", formatação de datas (locator, fmt) e legenda
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(df.index, df["temp"], lw=1.0, label="Temperatura")
ax1.plot(df.index, df["temp_ma7"], lw=2.0, label="Média móvel (7d)")
ax1.fill_between(df.index, base_temp, df["temp"],
                 where=(df["temp"] > base_temp), alpha=0.15)
ax1.fill_between(df.index, base_temp, df["temp"],
                 where=(df["temp"] < base_temp), alpha=0.15)
ax1.set_title("Temperatura Diária e Média Móvel (7 dias)")
ax1.set_ylabel("°C")
ax1.xaxis.set_major_locator(locator)
ax1.xaxis.set_major_formatter(fmt)
ax1.legend()

# 11) (Ax2) DISPERSÃO: ENERGIA vs TEMPERATURA + MARCAÇÃO DE SPIKES
# TODO: ax2 = fig.add_subplot(gs[0, 1])
# TODO: scatter de Temperatura e energy com alpha=0.7
# TODO: configurar título, xlabel, ylabel e legenda
# TODO: para cada elemento em idx_spikes, anotar "spike" no ponto correspondente (use annotate + 
# arrowprops). Exemplo:
# ax2.annotate("spike", (df["temp"].iloc[i], df["energy"].iloc[i]),
#              xytext=(8, 8), textcoords="offset points",
#              arrowprops=dict(arrowstyle="->", lw=0.8))
ax2 = fig.add_subplot(gs[0, 1])
ax2.scatter(df["temp"], df["energy"], alpha=0.7, label="Dados")
for i in idx_spike:
    ax2.annotate("spike", (df["temp"].iloc[i], df["energy"].iloc[i]),
                 xytext=(8, 8), textcoords="offset points",
                 arrowprops=dict(arrowstyle="->", lw=0.8))
ax2.set_title("Dispersão: Temperatura vs Consumo de Energia")
ax2.set_xlabel("Temperatura (°C)")
ax2.set_ylabel("Energia (kWh)")
ax2.legend()

# 12) (Ax3) HISTOGRAMA SIMPLES DE TEMPERATURA
# TODO: ax3 = fig.add_subplot(gs[1, 0])
# TODO: histograma da temperatura com alpha=0.7
# TODO: configurar título, xlabel, ylabel e legenda

ax3 = fig.add_subplot(gs[1, 0])
ax3.hist(df["temp"], bins=20, alpha=0.7)
ax3.set_title("Distribuição de Temperaturas")
ax3.set_xlabel("Temperatura (°C)")
ax3.set_ylabel("Frequência")
ax3.legend()

# 13) (Ax4) AGREGAÇÃO SEMANAL + TWIN AXES
# Agregamos por semana para reduzir ruído diário e comparamos consumo (barras) com clima (linha) 
# na mesma linha do tempo, sem misturar escalas.
# Pesquise resample
#
# TODO: weekly = df.resample("W").agg({"energy":"sum", "temp":"mean"})
# TODO: ax4 = fig.add_subplot(gs[1, 1])
# TODO: barras de weekly["energy"] (width=5, align="center", label="Energia (semanal)")
# TODO: formatação do eixo x de datas com locator e fmt; ylabel adequado
# TODO: crie ax4_t = ax4.twinx() e plote weekly["temp"] como linha (marker="o", lw=1.8, label="Temp média (semanal)")
# TODO: títulos e legendas para ambos os eixos (ax4.legend, ax4_t.legend)

weekly = df.resample("W").agg({"energy": "sum", "temp": "mean"})
ax4 = fig.add_subplot(gs[1, 1])
ax4.bar(weekly.index, weekly["energy"], width=5, align="center", label="Energia (semanal)")

ax4.set_ylabel("Energia (kWh)")
ax4.xaxis.set_major_locator(locator)
ax4.xaxis.set_major_formatter(fmt)

# Eixo secundário (temperatura média semanal)
ax4_t = ax4.twinx()
ax4_t.plot(weekly.index, weekly["temp"], marker="o", lw=1.8, color="tab:red", label="Temp média (semanal)")
ax4_t.set_ylabel("Temperatura média (°C)")

ax4.set_title("Energia Semanal vs Temperatura Média")
ax4.legend(loc="upper left")
ax4_t.legend(loc="upper right")

# 14) SALVAR E EXIBIR
# TODO: utilize tight_layout e salve a figura como "numpy_matplotlib.png" com 150 dpi
# TODO: exibir visualização
plt.tight_layout()
plt.savefig("numpy_matplotlib.png", dpi=150)
plt.show()