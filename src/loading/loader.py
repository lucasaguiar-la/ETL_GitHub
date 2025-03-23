from config.config import LOADER_OUTPUT_PATH
from pathlib import Path

import logging
import os

class DataLoader:
    def __init__(self, data):
        self.data = data
        self.output_dir = LOADER_OUTPUT_PATH
        self.logger = logging.getLogger('app_logger')

    def load(self, format='csv'):
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        self.logger.info(f'Salvando registros no formato: {format}')

        for col in self.data.select_dtypes(include=['datetime64[ns, UTC]', 'datetimetz']).columns:
            self.data[col] = self.data[col].dt.tz_localize(None)

        if format.lower() == 'csv':
            output_file = os.path.join(self.output_dir, 'output.csv')
            self.data.to_csv(output_file, index=False)
            self.logger.info(f'Dados salvos em: {output_file}')
        elif(format.lower() == 'excel'):
            excel_file = os.path.join(self.output_dir, 'output.xlsx')
            self.data.to_excel(excel_file, index=False)
            self.logger.info(f'Dados salvo em: {excel_file}')
        else:
            self.logger.error(f"Format '{format}' não suportado.")
            return False
        return True