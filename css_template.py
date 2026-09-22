
CSS = """
* { box-sizing: border-box; }

body {
  margin: 0;
  font-family: 'Segoe UI', Arial, Helvetica, sans-serif;
  background: #f4f1ea;
  color: #2b2b2b;
}

.topo {
  background: #1b1f3b;
  color: white;
  padding: 26px 24px;
  text-align: center;
}

.topo h1 {
  margin: 0;
  font-size: 26px;
}

.topo p {
  margin: 6px 0 0 0;
  color: #c8cce0;
  font-size: 13px;
}

.container {
  max-width: 1000px;
  margin: 0 auto;
  padding: 24px 20px 60px 20px;
}

.tab { display: none; }
.tab.active { display: block; }

.grade-capa {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
  margin-top: 20px;
}

.botao-capa {
  display: block;
  text-align: left;
  border: none;
  cursor: pointer;
  border-radius: 18px;
  padding: 24px;
  color: white;
  font-family: inherit;
  transition: transform 0.15s ease;
}

.botao-capa:hover { transform: translateY(-4px); }

.botao-capa .icone {
  font-size: 34px;
  font-weight: 800;
  margin-bottom: 10px;
}

.botao-capa .titulo {
  font-size: 19px;
  font-weight: 700;
}

.botao-capa .subtitulo {
  font-size: 13px;
  margin-top: 6px;
  opacity: 0.9;
}

.cor-dolar { background: #1f8a4c; }
.cor-euro { background: #2453a6; }
.cor-poupanca { background: #b8860b; }
.cor-selic { background: #8e2c48; }
.cor-inflacao { background: #a8471f; }
.cor-desemprego { background: #4a4a68; }

.voltar {
  display: inline-block;
  margin-bottom: 18px;
  background: #1b1f3b;
  color: white;
  border: none;
  padding: 10px 18px;
  border-radius: 20px;
  cursor: pointer;
  font-size: 13px;
}

.titulo-secao {
  font-size: 24px;
  font-weight: 800;
  margin-bottom: 4px;
}

.subtitulo-secao {
  color: #6b6b6b;
  font-size: 14px;
  margin-bottom: 20px;
}

.cartao {
  background: white;
  border-radius: 16px;
  padding: 22px;
  margin-bottom: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
}

.valor-grande {
  font-size: 40px;
  font-weight: 800;
}

.legenda-valor {
  color: #6b6b6b;
  font-size: 13px;
  margin-top: 2px;
}

.linha-fatos {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
  margin-top: 16px;
}

.fato {
  background: #f4f1ea;
  border-radius: 12px;
  padding: 14px 16px;
}

.fato .rotulo {
  font-size: 12px;
  color: #6b6b6b;
  text-transform: uppercase;
}

.fato .numero {
  font-size: 20px;
  font-weight: 800;
  margin-top: 4px;
}

.numero.sobe { color: #1f8a4c; }
.numero.desce { color: #b23a3a; }

.frase-simples {
  font-size: 15px;
  line-height: 1.5;
  margin: 10px 0;
}

.destaque {
  font-weight: 800;
}

.curiosidade {
  background: #fff8e6;
  border-left: 5px solid #b8860b;
  border-radius: 8px;
  padding: 16px 18px;
  margin-top: 18px;
}

.curiosidade .rotulo-curiosidade {
  font-size: 12px;
  text-transform: uppercase;
  color: #8a6d00;
  font-weight: 700;
  margin-bottom: 6px;
}

.rodape {
  text-align: center;
  color: #999;
  font-size: 12px;
  margin-top: 40px;
}

@media (max-width: 600px) {
  .valor-grande { font-size: 32px; }
  .topo h1 { font-size: 21px; }
}
"""
