from datetime import datetime
from src.utils.logger import setup_logging
from src.extraction.extractor import DataExtractor
from src.transformation.transformer import DataTransformer

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
        extractor = DataExtractor('data/raw/repository_data.csv') # DATASET ORIGINAL (mais pesasado)
        # extractor = DataExtractor('data/raw/github_dataset.csv') # DATASET DE TESTES (mais leve)
        raw_data = extractor.extract()
        logger.info(f'Extração concluída. {len(raw_data)} registros encontrados.')

        logger.info('Iniciando etapa de extração')
        transformer = DataTransformer(raw_data)
        processed_date = transformer.transform()
    
    except Exception as e:
        logger.error(f'Erro durante a execução do pipeline: {str(e)}')
        raise

if __name__ == '__main__':
    main()