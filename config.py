ASE_URL = (
    "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"
    "?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
)

SERIES = {
    "dolar": {
        "codigo": 1,
        "nome": "Dolar",
        "unidade": "R$",
        "periodicidade": "diaria",
        "observacoes": 280,
    },
    "euro": {
        "codigo": 21619,
        "nome": "Euro",
        "unidade": "R$",
        "periodicidade": "diaria",
        "observacoes": 280,
    },
    "poupanca": {
        "codigo": 195,
        "nome": "Poupanca",
        "unidade": "% no mes",
        "periodicidade": "mensal",
        "observacoes": 13,
    },
    "selic": {
        "codigo": 4390,
        "nome": "Juros Selic",
        "unidade": "% ao ano",
        "periodicidade": "mensal",
        "observacoes": 13,
    },
    "inflacao": {
        "codigo": 433,
        "nome": "Inflacao (IPCA)",
        "unidade": "% no mes",
        "periodicidade": "mensal",
        "observacoes": 13,
    },
    "desemprego": {
        "codigo": 24369,
        "nome": "Desemprego",
        "unidade": "%",
        "periodicidade": "mensal",
        "observacoes": 13,
    },
}
