from datetime import datetime
from src.utils.helpers import setup_logging
from src.extraction.extractor import DataExtractor

import logging
import os

def main():
    timestamp = datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = f'logs/pipeline_{timestamp}.log'
    os.makedirs('logs', exist_ok=True)

    setup_logging(log_file)
    logger = logging.getLogger('app_loger')

    logger.info('Iniciando pipeline ETL para dados do GitHub...')

    try:
        logger.info('Iniciando etapa de extração')
        extractor = DataExtractor('data/raw/github_dataset.csv')
        raw_data = extractor.extract()
        logger.info(f'Extração concluída. {len(raw_data)} registros encontrados.')
    
    except Exception as e:
        logger.error(f'Erro durante a execução do pipeline: {str(e)}')
        raise

if __name__ == '__main__':
    main()