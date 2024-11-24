# -*- coding: utf-8 -*-
from flask import Flask, render_template, request

app = Flask(__name__)

AREAS = [
    {
        "id": "comunhao_com_deus",
        "name": "Comunhão com Deus",
        "example": "Consistência na leitura bíblica, oração diária, momentos de adoração pessoal."
    },
    {
        "id": "amor_ao_proximo",
        "name": "Amor ao Próximo",
        "example": "Praticar o perdão, ajudar quem precisa, tratar as pessoas com gentileza."
    },
    {
        "id": "servico_na_igreja",
        "name": "Serviço na Igreja",
        "example": "Participar ativamente em ministérios, como louvor, ensino ou ações sociais."
    },
    {
        "id": "evangelismo",
        "name": "Evangelismo",
        "example": "Compartilhar sua fé, convidar pessoas para a igreja, viver como exemplo de Cristo."
    },
    {
        "id": "fe_e_confianca",
        "name": "Fé e Confiança",
        "example": "Permanecer firme em tempos difíceis, confiar nas promessas de Deus."
    },
    {
        "id": "conhecimento_biblico",
        "name": "Conhecimento Bíblico",
        "example": "Estudo regular das Escrituras, participação em estudos bíblicos ou cursos teológicos."
    },
    {
        "id": "vida_de_oracao",
        "name": "Vida de Oração",
        "example": "Frequência na oração, intercessão por outros, gratidão em oração."
    },
    {
        "id": "frutos_do_espirito",
        "name": "Frutos do Espírito",
        "example": "Demonstrar amor, alegria, paz, paciência, bondade, fidelidade, mansidão e domínio próprio."
    }
]

@app.route("/")
def index():
    return render_template("index.html", areas=AREAS)

@app.route("/result", methods=["POST"])
def result():
    print(request.form)
    scores = []
    for area in AREAS:
        value = request.form.get(area["id"], "0")
        print(f"{area['id']}: {value}")
        if not value:
            value = "0"
        try:
            scores.append(int(value))
        except (ValueError, TypeError):
            scores.append(0)
    
    total = sum(scores)
    avg = total / len(AREAS)
    return render_template("result.html", scores=scores, areas=AREAS, avg=avg)

if __name__ == "__main__":
    app.run(debug=True)
