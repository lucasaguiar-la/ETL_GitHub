from pathlib import Path

import os
import shutil
import logging
import kagglehub
import pandas as pd

class DataExtractor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.logger = logging.getLogger('app_logger')

    def extract(self):
        try:
            path = kagglehub.dataset_download("nikhil25803/github-dataset")
            dest_path = os.path.join("data\\raw\\", os.path.basename(path))
            shutil.move(path, dest_path)

            folder_path = os.path.join(dest_path)
            if os.path.exists(folder_path) and os.path.isdir(folder_path):
                for file_name in os.listdir(folder_path):
                    src_file = os.path.join(folder_path, file_name)
                    dest_file = os.path.join("data\\raw", file_name)
                    shutil.move(src_file, dest_file)

                os.rmdir(folder_path)
                self.logger.info(f'Dataset salvo em: {dest_file}')

                return True
        except Exception as e:
            self.logger.error(f'Algo deu errado ao baixar do dataset: {str(e)}')
            raise False

    def check_extraction(self):
            try:
                self.logger.debug(f'Tentando ler o arquivo: {self.file_path}')

                if not Path(self.file_path).exists():
                    self.logger.error(f'Arquivo não encontrado: {self.file_path}')
                    raise FileNotFoundError(f'Arquivo não encontrado: {self.file_path}')

                df = pd.read_csv(self.file_path)
                self.logger.info('Arquivo lido com sucesso!')
                self.logger.info(f'Colunas no dataset: {', '.join(df.columns.tolist())}')
                self.logger.info(f'Tipos de dados: \n{df.dtypes}')

                null_counts = df.isnull().sum()
                if null_counts.sum() > 0:
                    self.logger.warning(f'Valores nulus encontrado:\n{null_counts[null_counts > 0]}')

                return df

            except FileNotFoundError as e:
                self.logger.error(f'Arquivo não encontrado: {str(e)}')
                raise
            except Exception as e:
                self.logger.error(f'Erro durante a extração de dados: {str(e)}')
                raise
