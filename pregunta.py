"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------
Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.
"""
import pandas as pd

def clean_data():

    data = pd.read_csv("solicitudes_credito.csv", sep=";")

    data.rename(columns = {'Unnamed: 0': 'index'}, inplace = True)
    data.set_index('index', inplace = True)

    data.sexo = data.sexo.str.lower()
    data.sexo = data.sexo.astype('category')

    data.tipo_de_emprendimiento = data.tipo_de_emprendimiento.str.lower()
    data.tipo_de_emprendimiento = data.tipo_de_emprendimiento.astype('category')

    data.idea_negocio = data.idea_negocio.str.lower().str.strip('_').str.strip('-').str.strip().str.replace('_',' ').str.replace('-',' ')
    data.idea_negocio = data.idea_negocio.astype('category')

    data.barrio = data.barrio.str.lower().str.replace('_','-').str.replace("-", " ")

    data.comuna_ciudadano = data.comuna_ciudadano.astype('Int64')
    data.comuna_ciudadano = data.comuna_ciudadano.astype('category')

    data["fecha_de_beneficio"] = pd.to_datetime(data["fecha_de_beneficio"], format='mixed', dayfirst=True)

    data.monto_del_credito = data.monto_del_credito.str.replace('$','').str.replace(',','')
    data.monto_del_credito = data.monto_del_credito.astype(float)

    data.línea_credito = data.línea_credito.str.lower().str.strip('_').str.strip('-').str.strip().str.replace('_',' ').str.replace('-',' ')

    data.dropna(inplace = True)
    data.drop_duplicates(inplace = True)

    return data