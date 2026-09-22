def ultimo(serie):
    if not serie:
        return None
    return serie[-1]


def variacao_desde(serie, posicoes_atras):
    if not serie or len(serie) <= posicoes_atras:
        return None
    atual = serie[-1]["valor"]
    antigo = serie[-1 - posicoes_atras]["valor"]
    if antigo == 0:
        return None
    return round(((atual - antigo) / antigo) * 100, 2)


def maior_e_menor(serie):
    if not serie:
        return None
    maior = max(serie, key=lambda item: item["valor"])
    menor = min(serie, key=lambda item: item["valor"])
    return {"maior": maior, "menor": menor}


def quanto_compra_com_100_reais(valor_moeda):
    if not valor_moeda:
        return None
    return round(100 / valor_moeda, 2)


def render_poupanca(serie_poupanca, valor_guardado=1000):
    if not serie_poupanca:
        return None
    total = valor_guardado
    for item in serie_poupanca:
        total = total * (1 + item["valor"] / 100)
    return round(total, 2)


def preco_no_ano_passado(preco_atual, inflacao_12_meses_pct):
    if inflacao_12_meses_pct is None:
        return None
    return round(preco_atual / (1 + inflacao_12_meses_pct / 100), 2)


def montar_bloco_moeda(nome, serie):
    if not serie:
        return {"nome": nome, "disponivel": False}

    atual = ultimo(serie)
    var_dia = variacao_desde(serie, 1)
    var_mes = variacao_desde(serie, min(21, len(serie) - 1)) if len(serie) > 1 else None
    var_ano = variacao_desde(serie, len(serie) - 1) if len(serie) > 1 else None
    extremos = maior_e_menor(serie)
    compra_100 = quanto_compra_com_100_reais(atual["valor"])

    return {
        "nome": nome,
        "disponivel": True,
        "valor_atual": atual["valor"],
        "data_atual": atual["data"],
        "variacao_dia": var_dia,
        "variacao_mes": var_mes,
        "variacao_ano": var_ano,
        "maior": extremos["maior"] if extremos else None,
        "menor": extremos["menor"] if extremos else None,
        "compra_com_100_reais": compra_100,
    }


def montar_bloco_poupanca(serie):
    if not serie:
        return {"disponivel": False}

    atual = ultimo(serie)
    doze_meses = serie[-12:] if len(serie) >= 12 else serie
    total_apos_12_meses = render_poupanca(doze_meses, 1000)
    rendimento_12_meses_pct = round((total_apos_12_meses / 1000 - 1) * 100, 2) if total_apos_12_meses else None

    return {
        "disponivel": True,
        "valor_atual": atual["valor"],
        "data_atual": atual["data"],
        "mil_reais_vira": total_apos_12_meses,
        "rendimento_12_meses_pct": rendimento_12_meses_pct,
    }


def montar_bloco_selic(serie):
    if not serie:
        return {"disponivel": False}

    atual = ultimo(serie)
    extremos = maior_e_menor(serie)

    return {
        "disponivel": True,
        "valor_atual": atual["valor"],
        "data_atual": atual["data"],
        "maior": extremos["maior"] if extremos else None,
        "menor": extremos["menor"] if extremos else None,
    }


def montar_bloco_inflacao(serie):
    if not serie:
        return {"disponivel": False}

    atual = ultimo(serie)
    acumulado_12_meses = None
    if len(serie) >= 12:
        fator = 1.0
        for item in serie[-12:]:
            fator *= (1 + item["valor"] / 100)
        acumulado_12_meses = round((fator - 1) * 100, 2)

    preco_exemplo_hoje = 100
    preco_exemplo_ano_passado = preco_no_ano_passado(preco_exemplo_hoje, acumulado_12_meses)

    return {
        "disponivel": True,
        "valor_mes_atual": atual["valor"],
        "data_atual": atual["data"],
        "acumulado_12_meses": acumulado_12_meses,
        "exemplo_preco_hoje": preco_exemplo_hoje,
        "exemplo_preco_ano_passado": preco_exemplo_ano_passado,
    }


def montar_bloco_desemprego(serie):
    if not serie:
        return {"disponivel": False}

    atual = ultimo(serie)
    var_mes = variacao_desde(serie, 1)

    return {
        "disponivel": True,
        "valor_atual": atual["valor"],
        "data_atual": atual["data"],
        "variacao_mes": var_mes,
    }


def gerar_insights(series):
    dolar = montar_bloco_moeda("Dolar", series.get("dolar", []))
    euro = montar_bloco_moeda("Euro", series.get("euro", []))
    poupanca = montar_bloco_poupanca(series.get("poupanca", []))
    selic = montar_bloco_selic(series.get("selic", []))
    inflacao = montar_bloco_inflacao(series.get("inflacao", []))
    desemprego = montar_bloco_desemprego(series.get("desemprego", []))

    euro_mais_caro_que_dolar = None
    if dolar.get("disponivel") and euro.get("disponivel"):
        euro_mais_caro_que_dolar = euro["valor_atual"] > dolar["valor_atual"]

    return {
        "dolar": dolar,
        "euro": euro,
        "poupanca": poupanca,
        "selic": selic,
        "inflacao": inflacao,
        "desemprego": desemprego,
        "euro_mais_caro_que_dolar": euro_mais_caro_que_dolar,
    }
