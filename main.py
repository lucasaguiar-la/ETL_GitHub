from datetime import datetime
from src.utils.logger import setup_logging
from src.extraction.extractor import DataExtractor
from src.transformation.transformer import DataTransformer
from src.loading.loader import DataLoader

import logging
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    log_dir = os.path.join(base_dir, 'logs')
    data_dir = os.path.join(base_dir, 'data', 'raw')

    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = os.path.join(log_dir, f'pipeline_{timestamp}.log')

    setup_logging(log_file)
    logger = logging.getLogger('app_logger')

    file_path = os.path.join(data_dir, 'repository_data.csv')

    # Etapa de EXTRAÇÃO
    logger.info('Iniciando etapa de extração dos dados...')
    extractor = DataExtractor(base_dir, file_path)

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

    # Etapa de CARREGAMENTO
    #logger.info('Iniciando a etapa de carregamento dos dados...')
    #loader = DataLoader(transformer)

    #try:
    #    if loader.load():
    #        logging.info(f'Carregamento concluído com sucesso!')
    #except Exception as e:
    #    logger.error(f'Erro durante o carregamento de dados: {str(e)}')

if __name__ == '__main__':
    main()