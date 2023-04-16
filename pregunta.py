"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------
Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.
"""
import pandas as pd

def clean_data():

    data = pd.read_csv("solicitudes_credito.csv", sep=";")

    data.dropna(inplace = True)
    data.drop_duplicates(inplace = True)

    return df
