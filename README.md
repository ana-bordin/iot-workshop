# IoT Workshop

## Visão Geral
Este projeto é um workshop prático sobre IoT e Indústria 4.0, usando Python. O objetivo é ensinar conceitos básicos e habilidades práticas, incluindo leitura de dados de sensores, envio de dados para um servidor MQTT e criação de uma interface web simples.

## Estrutura do Projeto
- `src/`: Código-fonte principal
- `templates/`: Templates HTML para a interface web
- `data/`: Arquivos de dados e logs
- `docs/`: Documentos relacionados ao workshop
- `tests/`: Testes para os componentes do projeto

## Instalação
Instale as dependências com:
bash
pip install -r requirements.txt

Execução
Execute o publicador MQTT:
bash
python src/mqtt_publisher.py

Execute a aplicação web:
bash
python src/web_interface.py

Abra o navegador e acesse:

arduino
http://127.0.0.1:5000/