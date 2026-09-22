# Seu Dinheiro Hoje

Um painel simples que mostra, de um jeito facil de entender, como esta o
dolar, o euro, a poupanca, os juros, os precos e o desemprego no Brasil.
Nada de grafico complicado ou termo tecnico: e so abrir e olhar.

## Como usar

Precisa so do Python instalado e de uma biblioteca chamada `requests`.

```
pip install requests
python main.py
```

Isso cria o arquivo `seu_dinheiro_hoje.html`. Abra ele com dois cliques
e pronto, o painel aparece no navegador.

Pode rodar de novo quando quiser (amanha, semana que vem, todo dia) que
ele sempre busca os numeros mais atuais.

## O que tem dentro

Uma capa com seis botoes. Cada um abre uma tela sobre um assunto:

- **Dolar** - quanto vale hoje, se subiu ou caiu, e quanto voce compra
  de dolar com R$ 100.
- **Euro** - a mesma ideia, mas com o euro.
- **Poupanca** - quanto rendeu no mes e quanto viraria um dinheiro
  guardado ha 12 meses.
- **Juros (Selic)** - a taxa que o Banco Central define, explicada em
  poucas palavras.
- **Precos subindo (inflacao)** - quanto as coisas ficaram mais caras,
  com um exemplo pratico de preco.
- **Desemprego** - quantas pessoas em cada 100 estao sem trabalho.

## De onde vem a informacao

Tudo vem direto do Banco Central do Brasil, que disponibiliza esses
numeros de graca para qualquer pessoa consultar. Nao precisa de senha
nem cadastro.

## Arquivos do projeto

- `config.py` - lista o que o painel busca.
- `dados.py` - busca os numeros no Banco Central.
- `analise.py` - transforma os numeros em frases simples.
- `css_template.py` - cuida da aparencia.
- `html_builder.py` - monta a pagina final.
- `main.py` - arquivo que voce roda para gerar tudo.

## Deixando isso sempre atualizado sozinho

Se quiser publicar isso na internet e deixar atualizando sozinho todo
dia, da para usar o GitHub Pages junto com o GitHub Actions: um robo
roda o `python main.py` no horario que voce escolher e publica o
resultado automaticamente, sem voce precisar fazer nada.
