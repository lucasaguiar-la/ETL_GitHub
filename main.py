from datetime import datetime
from src.utils.logger import setup_logging
from src.extraction.extractor import DataExtractor
from src.transformation.transformer import DataTransformer

import logging
import os

def main():
    timestamp = datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = f'logs\\pipeline_{timestamp}.log'
    os.makedirs('logs', exist_ok=True)

    setup_logging(log_file)
    logger = logging.getLogger('app_loger')

    file_path = 'data\\raw\\repository_data.csv'
    os.makedirs("data", exist_ok=True)

    # Etapa de EXTRAÇÃO
    logger.info('Iniciando etapa de extração dos dados...')
    extractor = DataExtractor(file_path)

    try:
        if extractor.extract():
            raw_data = extractor.check_extraction()
            logger.info(f'Extração concluída. {len(raw_data)} registros encontrados.')
    except Exception as e:
        logger.error(f'Erro durante a extração de dados: {str(e)}')

    # Etapa de TRANSFORMAÇÃO
    logger.info('Iniciando etapa de tratamento dos dados...')
    transformer = DataTransformer(raw_data)

    try:
        if transformer.transform():
            logging.info(f'Tratamento concluído com sucesso!')
    except Exception as e:
        logger.error(f'Erro durante o tratamento de dados: {str(e)}')


if __name__ == '__main__':
    main()