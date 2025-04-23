Algoritmo de Anonimização para Privacidade em Tendências de Compras: Proteção dos Dados no Varejo 4.0 e Conformidade com a LGPD 

Este projeto foi desenvolvido como parte do Trabalho de Conclusão de Curso (TCC) do MBA em Data Science e Analytics da ESALQ/USP. 
O objetivo é aplicar técnicas de anonimização de dados sensíveis em contextos de Varejo 4.0, garantindo privacidade e conformidade com a Lei Geral de Proteção de Dados (LGPD).
Descrição

## O algoritmo implementa duas técnicas consagradas de anonimização:
- k-Anonimato: Garante que cada registro seja indistinguível de pelo menos `k-1` outros.
- l-Diversidade: Garante diversidade de valores em atributos sensíveis dentro dos grupos k-anonimizados.

Essas técnicas são aplicadas a um dataset de tendências de compras (disponibilizado gratuitamente no site kaggle) para preservar a utilidade analítica dos dados, minimizando riscos de reidentificação.

Referencia: SOURAV BANERJEE · Customer Shopping Trends Dataset. 2023. Base de dados para teste da anonimização. 
Disponível em: https://www.kaggle.com/datasets/iamsouravbanerjee/customer-shopping-trends-dataset?resource=download

## Tecnologias Utilizadas
- Python 3.x
- pandas

## 📁 Estrutura do Projeto

```
├── shopping_trends.csv               # Dataset original (não incluído por questões de privacidade)
├── Script_Anonimizacao2.py           # Script principal com aplicação do algoritmo
├── shopping_trends_anonimizados.csv  # Saída esperada (gerada ao executar o script)
└── Compara_arquivos.py               # Compara os arquivos Orignal e anonimizados
```
## Como Usar

1. Clone este repositório:
```bash
git clone https://github.com/jenifferazevedo01/anonimizacao-lgpd-mba.git
cd anonimizacao-lgpd-mba
```

2. Instale as dependências:
```bash
pip install pandas
```

3. Coloque seu arquivo `shopping_trends.csv` no diretório do projeto.

4. Execute o script:
```bash
python Script_Anonimizacao2.py
```

5. O arquivo `shopping_trends_anonimizados.csv` será gerado com os dados anonimizados.

## Licença
Este projeto é livre para uso acadêmico e educacional, conforme os termos da licença MIT.

## Autora
Jeniffer Costa de Azevedo Rodrigues  
MBA em Data Science e Analytics - ESALQ/USP  
Contato: jenifferazevedo01@gmail.com


