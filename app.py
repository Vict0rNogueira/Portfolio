"""
Portfólio Pessoal - Aplicação Flask
Desenvolvedor em busca de oportunidades na área de tecnologia
"""

from flask import Flask, render_template

# Inicialização da aplicação
app = Flask(__name__)


@app.route("/")
def home():
    """Página inicial - Hero e apresentação"""
    return render_template("index.html")


@app.route("/projetos")
def projetos():
    """Página de projetos - Cards com trabalhos realizados"""
    return render_template("projetos.html")


@app.route("/contato")
def contato():
    """Página de contato - Links para redes e WhatsApp"""
    return render_template("contato.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
