import logging
import pandas as pd
import numpy as np
from datetime import datetime

class DataTransformer:
    def __init__(self, data):
        self.data = data
        self.logger = logging.getLogger('app_logger')

    def transform(self):
        logging.info('Iniciando transformação dos dados...')

        df = self.data.copy()

        df = self.clean_data(df)
        # Todo
        '''
        df = self.convert_data_types(df)
        df = self.create_feature(df)
        df = self.remove_outliners(df)'
        '''

    def clean_data(df):
        logging.info('Realizando a limpeza de dados.')

        try:
            duplicates = df.duplicated().sum()
            if duplicates > 0:
                logging.info(f'Removendo {duplicates} linhas duplicadas.')
                df = df.drop_duplicates()

            null_counts = df.isnull().sum()
            if null_counts > 0:
                logging.info(f'Tratando valores nulos em {sum(null_counts > 0)} colunas.')

                numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
                for col in numeric_cols:
                    if df[col].isnull().sum() > 0:
                        median_value = df[col].median()
                        df[col] = df[col].fillna(median_value)
                        logging.info(f"Colina '{col}': valores nulos substituídos pela mediana ({median_value})")

                text_col = df.select_types(include=['object']).columns
                for col in text_col:
                    if df[col].isnull().sum() > 0:
                        df[col] = df[col].fillna('Desconhecido')
                        logging.info(f"Coluna '{col}': valores nulos substituídos por 'Desconhecido'")

            return df
        except Exception as e:
            logging.error(f'Erro na etapa de limpeza de dados: {e}')
            raise