from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# MyMemory Translation API endpoint
API_URL = "https://api.mymemory.translated.net/get"

@app.route('/', methods=['GET', 'POST'])
def index():
    input_language = ""
    input_text = ""
    output_language = ""
    translation = ""

    if request.method == 'POST':
        input_language = request.form['input_language']
        input_text = request.form['input_text']
        output_language = request.form['output_language']

        # Make a request to the MyMemory Translation API
        params = {
            'q': input_text,
            'langpair': f'{input_language}|{output_language}'
        }
        response = requests.get(API_URL, params=params)
        translation = response.json().get('responseData', {}).get('translatedText', '')

    return render_template('index.html', translation=translation, input_language=input_language,
                           input_text=input_text, output_language=output_language)

if __name__ == '__main__':
    app.run(debug=True)
