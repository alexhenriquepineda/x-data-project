import google.generativeai as genai


def generative_ai_text(GEMINI_API_KEY, model, pdf_text):
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel(model)
    chat = model.start_chat(history=[])

    response = chat.send_message("Considere que será um texto postado no Twitter, então resuma em 2 linhas o que está escrito no seguinte texto, mas como o texto será postado no Twitter, não crie dois paragráfos, escreva tudo em uma linha só:" + pdf_text)

    return response

