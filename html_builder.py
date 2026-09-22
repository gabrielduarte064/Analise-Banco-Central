from datetime import datetime

from css_template import CSS


def _seta(valor):
    if valor is None:
        return ""
    return "subiu" if valor >= 0 else "caiu"


def _classe_numero(valor):
    if valor is None:
        return ""
    return "sobe" if valor >= 0 else "desce"


def _fmt_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def _fmt_pct(valor):
    if valor is None:
        return "sem dado"
    sinal = "+" if valor >= 0 else ""
    return f"{sinal}{valor}%"


def _capa():
    return """
    <div id="capa" class="tab active">
      <p style="color:#6b6b6b; font-size:15px; margin-top:0;">
        Escolha o que voce quer entender agora.
      </p>
      <div class="grade-capa">
        <button class="botao-capa cor-dolar" onclick="mostrar('dolar', this)">
          <div class="icone">US$</div>
          <div class="titulo">Dolar</div>
          <div class="subtitulo">quanto esta valendo hoje</div>
        </button>
        <button class="botao-capa cor-euro" onclick="mostrar('euro', this)">
          <div class="icone">EUR</div>
          <div class="titulo">Euro</div>
          <div class="subtitulo">quanto esta valendo hoje</div>
        </button>
        <button class="botao-capa cor-poupanca" onclick="mostrar('poupanca', this)">
          <div class="icone">%</div>
          <div class="titulo">Poupanca</div>
          <div class="subtitulo">quanto seu dinheiro rende</div>
        </button>
        <button class="botao-capa cor-selic" onclick="mostrar('selic', this)">
          <div class="icone">$</div>
          <div class="titulo">Juros (Selic)</div>
          <div class="subtitulo">a taxa que mexe com tudo</div>
        </button>
        <button class="botao-capa cor-inflacao" onclick="mostrar('inflacao', this)">
          <div class="icone">^</div>
          <div class="titulo">Precos subindo</div>
          <div class="subtitulo">inflacao do mes</div>
        </button>
        <button class="botao-capa cor-desemprego" onclick="mostrar('desemprego', this)">
          <div class="icone">#</div>
          <div class="titulo">Desemprego</div>
          <div class="subtitulo">quem esta sem trabalho</div>
        </button>
      </div>
    </div>"""


def _botao_voltar():
    return '<button class="voltar" onclick="mostrar(\'capa\', null)">voltar</button>'


def _secao_dolar(d):
    if not d.get("disponivel"):
        return f'<div id="dolar" class="tab">{_botao_voltar()}<p>Sem dados do dolar agora.</p></div>'

    return f"""
    <div id="dolar" class="tab">
      {_botao_voltar()}
      <div class="titulo-secao">Dolar</div>
      <div class="subtitulo-secao">atualizado em {d['data_atual']}</div>

      <div class="cartao">
        <div class="valor-grande">{_fmt_moeda(d['valor_atual'])}</div>
        <div class="legenda-valor">1 dolar em reais</div>

        <div class="linha-fatos">
          <div class="fato">
            <div class="rotulo">desde ontem</div>
            <div class="numero {_classe_numero(d['variacao_dia'])}">{_fmt_pct(d['variacao_dia'])}</div>
          </div>
          <div class="fato">
            <div class="rotulo">no ultimo mes</div>
            <div class="numero {_classe_numero(d['variacao_mes'])}">{_fmt_pct(d['variacao_mes'])}</div>
          </div>
          <div class="fato">
            <div class="rotulo">no ultimo ano</div>
            <div class="numero {_classe_numero(d['variacao_ano'])}">{_fmt_pct(d['variacao_ano'])}</div>
          </div>
        </div>
      </div>

      <div class="curiosidade">
        <div class="rotulo-curiosidade">Na pratica</div>
        <p class="frase-simples">Com <span class="destaque">R$ 100</span>, hoje voce compra
        <span class="destaque">{d['compra_com_100_reais']} dolares</span>.</p>
        <p class="frase-simples">Nos ultimos meses, o dolar mais caro foi
        <span class="destaque">{_fmt_moeda(d['maior']['valor'])}</span> (em {d['maior']['data']}),
        e o mais barato foi <span class="destaque">{_fmt_moeda(d['menor']['valor'])}</span>
        (em {d['menor']['data']}).</p>
      </div>
    </div>"""


def _secao_euro(e, euro_mais_caro):
    if not e.get("disponivel"):
        return f'<div id="euro" class="tab">{_botao_voltar()}<p>Sem dados do euro agora.</p></div>'

    frase_comparacao = ""
    if euro_mais_caro is True:
        frase_comparacao = "O euro esta mais caro que o dolar, como quase sempre acontece."
    elif euro_mais_caro is False:
        frase_comparacao = "Neste momento, o euro esta mais barato que o dolar, o que e raro."

    return f"""
    <div id="euro" class="tab">
      {_botao_voltar()}
      <div class="titulo-secao">Euro</div>
      <div class="subtitulo-secao">atualizado em {e['data_atual']}</div>

      <div class="cartao">
        <div class="valor-grande">{_fmt_moeda(e['valor_atual'])}</div>
        <div class="legenda-valor">1 euro em reais</div>

        <div class="linha-fatos">
          <div class="fato">
            <div class="rotulo">desde ontem</div>
            <div class="numero {_classe_numero(e['variacao_dia'])}">{_fmt_pct(e['variacao_dia'])}</div>
          </div>
          <div class="fato">
            <div class="rotulo">no ultimo mes</div>
            <div class="numero {_classe_numero(e['variacao_mes'])}">{_fmt_pct(e['variacao_mes'])}</div>
          </div>
          <div class="fato">
            <div class="rotulo">no ultimo ano</div>
            <div class="numero {_classe_numero(e['variacao_ano'])}">{_fmt_pct(e['variacao_ano'])}</div>
          </div>
        </div>
      </div>

      <div class="curiosidade">
        <div class="rotulo-curiosidade">Na pratica</div>
        <p class="frase-simples">Com <span class="destaque">R$ 100</span>, hoje voce compra
        <span class="destaque">{e['compra_com_100_reais']} euros</span>.</p>
        <p class="frase-simples">{frase_comparacao}</p>
      </div>
    </div>"""


def _secao_poupanca(p):
    if not p.get("disponivel"):
        return f'<div id="poupanca" class="tab">{_botao_voltar()}<p>Sem dados da poupanca agora.</p></div>'

    return f"""
    <div id="poupanca" class="tab">
      {_botao_voltar()}
      <div class="titulo-secao">Poupanca</div>
      <div class="subtitulo-secao">referente a {p['data_atual']}</div>

      <div class="cartao">
        <div class="valor-grande">{_fmt_pct(p['valor_atual'])}</div>
        <div class="legenda-valor">foi o quanto a poupanca rendeu neste mes</div>
      </div>

      <div class="curiosidade">
        <div class="rotulo-curiosidade">Na pratica</div>
        <p class="frase-simples">Quem guardou <span class="destaque">R$ 1.000</span> na poupanca
        ha 12 meses, hoje teria <span class="destaque">R$ {p['mil_reais_vira']:.2f}</span>.</p>
        <p class="frase-simples">Isso e um rendimento de
        <span class="destaque">{_fmt_pct(p['rendimento_12_meses_pct'])}</span> no ano.</p>
      </div>
    </div>"""


def _secao_selic(s, poupanca):
    if not s.get("disponivel"):
        return f'<div id="selic" class="tab">{_botao_voltar()}<p>Sem dados da Selic agora.</p></div>'

    return f"""
    <div id="selic" class="tab">
      {_botao_voltar()}
      <div class="titulo-secao">Juros (Selic)</div>
      <div class="subtitulo-secao">referente a {s['data_atual']}</div>

      <div class="cartao">
        <div class="valor-grande">{_fmt_pct(s['valor_atual'])}</div>
        <div class="legenda-valor">taxa basica de juros do Brasil, ao ano</div>
      </div>

      <div class="curiosidade">
        <div class="rotulo-curiosidade">O que isso significa</div>
        <p class="frase-simples">A Selic e a taxa que o Banco Central define para controlar a economia.
        Quando ela sobe, os emprestimos ficam mais caros e a poupanca rende mais.
        Quando ela cai, o contrario acontece.</p>
        <p class="frase-simples">Nos ultimos meses, a Selic mais alta foi
        <span class="destaque">{_fmt_pct(s['maior']['valor'])}</span> (em {s['maior']['data']}),
        e a mais baixa foi <span class="destaque">{_fmt_pct(s['menor']['valor'])}</span>
        (em {s['menor']['data']}).</p>
      </div>
    </div>"""


def _secao_inflacao(i):
    if not i.get("disponivel"):
        return f'<div id="inflacao" class="tab">{_botao_voltar()}<p>Sem dados de inflacao agora.</p></div>'

    return f"""
    <div id="inflacao" class="tab">
      {_botao_voltar()}
      <div class="titulo-secao">Precos subindo (inflacao)</div>
      <div class="subtitulo-secao">referente a {i['data_atual']}</div>

      <div class="cartao">
        <div class="valor-grande">{_fmt_pct(i['valor_mes_atual'])}</div>
        <div class="legenda-valor">quanto os precos subiram neste mes (IPCA)</div>
      </div>

      <div class="curiosidade">
        <div class="rotulo-curiosidade">Na pratica</div>
        <p class="frase-simples">Nos ultimos 12 meses, os precos acumularam alta de
        <span class="destaque">{_fmt_pct(i['acumulado_12_meses'])}</span>.</p>
        <p class="frase-simples">Ou seja: um produto que custa
        <span class="destaque">R$ {i['exemplo_preco_hoje']:.2f}</span> hoje,
        custava por volta de <span class="destaque">R$ {i['exemplo_preco_ano_passado']:.2f}</span>
        ha um ano.</p>
      </div>
    </div>"""


def _secao_desemprego(dz):
    if not dz.get("disponivel"):
        return f'<div id="desemprego" class="tab">{_botao_voltar()}<p>Sem dados de desemprego agora.</p></div>'

    return f"""
    <div id="desemprego" class="tab">
      {_botao_voltar()}
      <div class="titulo-secao">Desemprego</div>
      <div class="subtitulo-secao">referente a {dz['data_atual']}</div>

      <div class="cartao">
        <div class="valor-grande">{_fmt_pct(dz['valor_atual'])}</div>
        <div class="legenda-valor">a cada 100 pessoas que procuram trabalho, essa e a parte sem emprego</div>
      </div>

      <div class="curiosidade">
        <div class="rotulo-curiosidade">Na pratica</div>
        <p class="frase-simples">Na comparacao com o mes anterior, o desemprego
        <span class="destaque">{_seta(dz['variacao_mes'])}</span>
        ({_fmt_pct(dz['variacao_mes'])}).</p>
      </div>
    </div>"""


def montar_html(insights):
    agora = datetime.now().strftime("%d/%m/%Y as %H:%M")

    corpo = _capa()
    corpo += _secao_dolar(insights["dolar"])
    corpo += _secao_euro(insights["euro"], insights["euro_mais_caro_que_dolar"])
    corpo += _secao_poupanca(insights["poupanca"])
    corpo += _secao_selic(insights["selic"], insights["poupanca"])
    corpo += _secao_inflacao(insights["inflacao"])
    corpo += _secao_desemprego(insights["desemprego"])

    html = f"""<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Seu Dinheiro Hoje</title>
<style>{CSS}</style>
</head>
<body>

<div class="topo">
  <h1>Seu Dinheiro Hoje</h1>
  <p>Atualizado em {agora}</p>
</div>

<div class="container">
  {corpo}
  <div class="rodape">Dados publicos do Banco Central do Brasil.</div>
</div>

<script>
function mostrar(id, botao) {{
  document.querySelectorAll('.tab').forEach(function(t) {{ t.classList.remove('active'); }});
  document.getElementById(id).classList.add('active');
  window.scrollTo(0, 0);
}}
</script>

</body>
</html>"""
    return html
