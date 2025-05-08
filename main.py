# pandas para ler csv e transformar em dataframe
import pandas as pd

# pandas profile (ydata profiling) para gerar o relatório
from ydata_profiling import ProfileReport

df = pd.read_csv('data.csv')

profile = ProfileReport(df, title="Pandas Profiling Report", explorative=True)
profile.to_file("output.html")
# profile.to_widgets() # para visualizar no jupyter notebook
