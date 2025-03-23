from config.config import LOADER_OUTPUT_PATH
from pathlib import Path

import logging
import os

class DataLoader:
    def __init__(self, data):
        self.data = data
        self.logger = logging.getLogger('app_logger')

    def load(self, format='csv'):
        output_dir = os.path.dirname(LOADER_OUTPUT_PATH)
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        self.logger.info(f'Salvando {len(self.data)} registros no formato: {format}')

        if format.lower() == 'csv':
            self.data.to_csv(self.data, index=False)
            logging.info(f'Dados salvos em: {self.output_dir}')
        elif(format.lower() == 'excel'):
            excel_path = self.data
            if not excel_path.endswith(('.xlsx', '.xls')):
                excel_path = os.path.splitext(self.data)[0] + '.xlsx'
            self.data.to_excel(excel_path, index=False)
            self.logger.info(f'Dados salvo em: {self.excel_path}')
        else:
            self.logger.error(f"Format '{format}' não suportado.")
            return False