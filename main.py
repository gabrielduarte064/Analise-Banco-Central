from dados import buscar_tudo
from analise import gerar_insights
from html_builder import montar_html

SAIDA = "seu_dinheiro_hoje.html"


def main():
    print("Buscando os numeros mais recentes no Banco Central...")
    series = buscar_tudo()

    print("Transformando os numeros em frases simples...")
    insights = gerar_insights(series)

    print("Montando a pagina...")
    html = montar_html(insights)

    with open(SAIDA, "w", encoding="utf-8") as arquivo:
        arquivo.write(html)

    print(f"Pronto. Abra o arquivo: {SAIDA}")


if __name__ == "__main__":
    main()
