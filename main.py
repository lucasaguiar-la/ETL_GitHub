from config import config
from datetime import datetime
from src.utils.logger import setup_logging
from src.extraction.extractor import DataExtractor
from src.transformation.transformer import DataTransformer
from src.loading.loader import DataLoader

import os
import logging

def main():
    # Configuração dos caminhos
    log_dir = os.path.join(config.LOG_DIR_PATH)
    data_dir = os.path.join(config.DATA_DIR_PATH)

    os.makedirs(log_dir, exist_ok=True)
    os.makedirs(data_dir, exist_ok=True)

    timestamp = datetime.now().strftime('%d%m%Y_%H%M%S')
    log_file = os.path.join(log_dir, f'pipeline_{timestamp}.log')

    setup_logging(log_file)
    logger = logging.getLogger('app_logger')

    file_path = os.path.join(data_dir, 'repository_data.csv')

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
        transformer.transform()
        transformed_data = transformer.get_data()

        if transformed_data is not None and not transformed_data.empty:
            logger.info(f'Tratamento concluído com sucesso!')
        else:
            logger.warning('O DataFrame resultante está vazio ou nulo após a transformação.')
    except Exception as e:
        logger.error(f'Erro durante o tratamento de dados: {str(e)}')

    # Etapa de CARREGAMENTO
    if transformed_data is not None:
        logger.info('Iniciando a etapa de carregamento dos dados...')

        try:
            dataset = DataLoader(transformed_data)
            save_dataset = dataset.load(format='excel')

            if save_dataset:
                logger.info('Dados carregados com sucesso!')
        except Exception as e:
            logger.error(f'Erro durante o carregamento de dados: {str(e)}')

if __name__ == '__main__':
    main()