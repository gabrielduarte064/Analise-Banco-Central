
from datetime import date, timedelta

import requests

from config import BASE_URL, SERIES


def _converter_valor(valor_bruto):
    if valor_bruto is None:
        return None
    texto = str(valor_bruto).strip().replace(",", ".")
    try:
        return float(texto)
    except ValueError:
        return None


def _formatar_data(data_python):
    return data_python.strftime("%d/%m/%Y")


def _janela_de_datas(periodicidade, observacoes):
    hoje = date.today()
    if periodicidade == "diaria":
        dias = int(observacoes * 1.6) + 30
    else:
        dias = int(observacoes * 31) + 45
    dias = min(dias, 365 * 10 - 30)
    return hoje - timedelta(days=dias), hoje


def buscar_serie(chave):
    info = SERIES[chave]
    data_inicial, data_final = _janela_de_datas(info["periodicidade"], info["observacoes"])

    url = BASE_URL.format(
        codigo=info["codigo"],
        data_inicial=_formatar_data(data_inicial),
        data_final=_formatar_data(data_final),
    )

    resposta = requests.get(url, timeout=25, headers={"User-Agent": "painel-bolso/1.0"})
    resposta.raise_for_status()
    bruto = resposta.json()

    serie = []
    for item in bruto:
        valor = _converter_valor(item.get("valor"))
        if valor is not None:
            serie.append({"data": item.get("data"), "valor": valor})

    limite = info["observacoes"]
    if len(serie) > limite:
        serie = serie[-limite:]

    return serie


def buscar_tudo():
    resultado = {}
    for chave in SERIES:
        try:
            resultado[chave] = buscar_serie(chave)
        except Exception as erro:
            print(f"Nao consegui buscar '{SERIES[chave]['nome']}': {erro}")
            resultado[chave] = []
    return resultado
