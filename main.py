from datetime import datetime
from src.utils.helpers import setup_logging

import logging
import os

def main():
    timestamp = datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = f'logs/pipeline_{timestamp}.log'
    os.makedirs('logs', exist_ok=True)
    setup_logging(log_file)

    logging.info('Iniciando pipeline ETL para dados do GitHub...')
