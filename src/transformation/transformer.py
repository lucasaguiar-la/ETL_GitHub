from config.config import FILTER_KEY
from datetime import datetime

import logging
import pandas as pd
import numpy as np

class DataTransformer:
    def __init__(self, data):
        self.data = data
        self.logger = logging.getLogger('app_logger')

    def transform(self):
        self.logger.info('Iniciando transformação dos dados...')

        df = self.data.copy()

        if not pd.api.types.is_datetime64_any_dtype(df['created_at']):
            df['created_at'] = pd.to_datetime(df['created_at'])
        if df['created_at'].dt.tz is None:
            df['created_at'] = df['created_at'].dt.tz_localize('UTC', ambiguous='infer')

        date_now = pd.Timestamp.now(tz='UTC')
        df['time_age'] = (date_now - df['created_at']).dt.days

        df = self.clean_data(df)
        df = self.apply_filter(df)
        # df = self.calculate_engagement(df)

    def clean_data(self, df):
        self.logger.info('Realizando a limpeza de dados.')

        try:
            duplicates = df.duplicated().sum()
            if duplicates > 0:
                self.logger.info(f'Removendo {duplicates} linhas duplicadas.')
                df = df.drop_duplicates()

            null_counts = df.isnull().sum()
            if null_counts.any():
                self.logger.info(f'Tratando valores nulos em {sum(null_counts > 0)} colunas.')

                numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
                for col in numeric_cols:
                    if df[col].isnull().sum() > 0:
                        median_value = df[col].median()
                        df.loc[:, col] = df[col].fillna(median_value)
                        self.logger.info(f"Colina '{col}': valores nulos substituídos pela mediana ({median_value})")

                text_col = df.select_dtypes(include=['object']).columns
                for col in text_col:
                    if df[col].isnull().sum() > 0:
                        df.loc[:, col] = df[col].fillna('Desconhecido')
                        self.logger.info(f"Coluna '{col}': valores nulos substituídos por 'Desconhecido'")

            return df
        except Exception as e:
            self.logger.error(f'Erro na etapa de limpeza de dados: {str(e)}')
            raise

    def apply_filter(self, df):
        self.logger.info(f'Aplicando filtro de linguagem: {FILTER_KEY}')
        return df[df['primary_language'] == FILTER_KEY]

    def calculate_engagement(self, df):
        self.logger.info('Calculando métricas de engajamento...')

        try:
            self.logger.info('Normalizando métricas com log para lidar com outliers.')

            for col in ['stars_count', 'forks_count', 'watchers', 'pull_requests', 'commit_count']:
                df[f'{col}_norm'] = np.log1p(df)
                self.logger.info(f"Coluna '{col}': normalizada com log1p")

            self.logger.info('Calculando taxas por idade do projeto.')
            df['commit_rate'] = df['commit_count'] / (df['time_age'] + 1)
            df['pr_rate'] = df['pull_requests'] / (df['time_age'] + 1)
            df['fork_rate'] = df['forks_count'] / (df['time_age'] + 1)

            self.logger.info('Calculando score final de engajamento com pesos.')
            df['engagement_score'] = (
                df['stars_count_norm'] * 0.35 +
                df['forks_count_norm'] * 0.20 +
                df['watchers_norm'] * 0.10 +
                df['pull_requests_norm'] * 0.15 +
                df['commit_count_norm'] * 0.10 +
                df['commit_rate'] * 100 * 0.05 +
                df['pr_rate'] * 100 * 0.05
            )

            self.logger.info('Cálculo de engajamento concluído com sucesso!')
            return df
        
        except Exception as e:
            self.logger.error(f'Erro no cálculo de métricas de engajametno: {str(e)}')
            raise
