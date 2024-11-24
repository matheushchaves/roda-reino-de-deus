from flask import Flask, render_template, request
import markdown
import os
from dotenv import load_dotenv
import openai
import requests

# Carregar variáveis do arquivo .env
load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
FROM_EMAIL_SENDGRID = os.getenv('FROM_EMAIL_SENDGRID')


# Configurar chave de API para OpenAI
openai.api_key = OPENAI_API_KEY

app = Flask(__name__)

AREAS = [
    {"id": "comunhao_com_deus", "name": "Comunhão com Deus", "example": "Consistência na leitura bíblica, oração diária, momentos de adoração pessoal."},
    {"id": "amor_ao_proximo", "name": "Amor ao Próximo", "example": "Praticar o perdão, ajudar quem precisa, tratar as pessoas com gentileza e compaixão."},
    {"id": "servico_cristao", "name": "Serviço Cristão", "example": "Participar ativamente em ministérios ou projetos sociais na igreja e na comunidade."},
    {"id": "evangelismo", "name": "Evangelismo", "example": "Compartilhar sua fé, convidar pessoas para a igreja e ser exemplo de Cristo no dia a dia."},
    {"id": "discipulado", "name": "Discipulado", "example": "Acompanhar e ser acompanhado por outros na caminhada cristã, promovendo crescimento mútuo."},
    {"id": "fe_e_confianca", "name": "Fé e Confiança", "example": "Permanecer firme em tempos difíceis, confiar nas promessas de Deus e rejeitar dúvidas."},
    {"id": "conhecimento_biblico", "name": "Conhecimento Bíblico", "example": "Estudo regular das Escrituras, participação em cursos teológicos e memorização de versículos."},
    {"id": "vida_de_oracao", "name": "Vida de Oração", "example": "Frequência na oração, intercessão por outros e prática de gratidão constante em oração."},
    {"id": "frutos_do_espirito", "name": "Frutos do Espírito", "example": "Demonstrar amor, alegria, paz, paciência, bondade, fidelidade, mansidão e domínio próprio."},
    {"id": "mordomia_crista", "name": "Mordomia Cristã", "example": "Gerenciar tempo, talentos e recursos financeiros de forma responsável para a glória de Deus."}
]


@app.route("/")
def index():
    return render_template("index.html", areas=AREAS)

def generate_assessment(name, scores):
    """
    Gera uma avaliação personalizada baseada nas notas usando a API do ChatGPT via REST.
    """
    import requests

    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    ENDPOINT = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}"
    }

    prompt = f"""
O usuário {name} forneceu as seguintes notas para áreas relacionadas à vida cristã:

{', '.join([f"{area['name']}: {score}" for area, score in zip(AREAS, scores)])}

Baseado nessas notas, escreva uma avaliação personalizada com direcionamentos práticos, utilizando versículos bíblicos relevantes. Para cada área, inclua:
- Uma reflexão baseada na nota.
- Um direcionamento prático.
- Um versículo bíblico aplicável.

Conclua a mensagem com uma palavra de encorajamento geral. (formato: markdown)
"""
    messages = [
        {"role": "system", "content": "Você é um conselheiro cristão reformado batista que usa a Bíblia como base para avaliações e direcionamentos."},
        {"role": "user", "content": prompt}
    ]
    data = {
        "model": "gpt-3.5-turbo",  # ou "gpt-4" se você tiver acesso
        "messages": messages,
        "temperature": 0.5,
        "max_tokens": 1000
    }
    try:
        response = requests.post(ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if 'choices' in response_json and response_json['choices']:
            assessment_markdown = response_json['choices'][0]['message']['content'].strip()
            # Converte Markdown para HTML
            assessment_html = markdown.markdown(assessment_markdown)
            return assessment_html
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API do ChatGPT: {e}")
    return "Desculpe, não foi possível gerar uma avaliação no momento."


@app.route("/result", methods=["POST"])
def result():
    name = request.form.get("name")

    scores = []
    for area in AREAS:
        value = request.form.get(area["id"], "0")
        try:
            scores.append(int(value))
        except (ValueError, TypeError):
            scores.append(0)

    avg = sum(scores) / len(AREAS)
    assessment = generate_assessment(name, scores)

    return render_template("result.html", scores=scores, areas=AREAS, avg=avg, assessment=assessment)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80,debug=True)
