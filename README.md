# ETL Pipeline para Análise de Repositórios Python no GitHub

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para processar e analisar dados de repositórios Python do GitHub. O sistema extrai dados de um dataset do Kaggle, realiza transformações para calcular métricas de engajamento e exporta os resultados em formatos estruturados.

## Funcionalidades

- **Extração**: Download automático do dataset do Kaggle
- **Transformação**: 
  - Limpeza de dados
  - Cálculo de métricas de engajamento
  - Normalização de valores
  - Filtro para repositórios Python
- **Carregamento**: Exportação em formatos CSV e Excel

## Tecnologias Utilizadas
- Python 3.9
- kagglehub
- numpy
- openpyxl
- outras (ver requirements.txt)

## Estrutura do Projeto

```
projeto/
│
├── config/
│   └── config.py         # Configurações globais
│
├── src/
│   ├── extraction/       # Módulos de extração
│   ├── transformation/   # Módulos de transformação
│   ├── loading/         # Módulos de carregamento
│   └── utils/           # Utilitários (logging, etc)
│
├── data/
│   ├── raw/             # Dados brutos
│   └── final/          # Dados finais
│
├── logs/                # Arquivos de log
├── requirements.txt     # Dependências
└── main.py             # Ponto de entrada
```

## Pré-requisitos

- Python 3.8+
- Dependências listadas em `requirements.txt`

## Instalação

1. Clone o repositório:
```bash
git clone https://github.com/lucasaguiar-la/ETL_GitHub
cd ETL_GitHub
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso

Execute o pipeline através do arquivo principal:

```bash
python main.py
```

## Métricas Calculadas

- Normalização logarítmica de métricas base
- Taxa de commits por idade do projeto
- Taxa de pull requests
- Taxa de forks
- Score de engajamento ponderado

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
