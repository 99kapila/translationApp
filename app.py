from flask import Flask, render_template, request, jsonify

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

        try:
            response = requests.get(API_URL, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
            translation = response.json().get('responseData', {}).get('translatedText', '')
        except requests.RequestException as e:
            # Log the exception for debugging
            app.logger.exception("Error in MyMemory Translation API request:")
            # Return a JSON response with an error message
            return jsonify(error=f"An error occurred in translation: {str(e)}"), 500

    return render_template('index.html', translation=translation, input_language=input_language,
                           input_text=input_text, output_language=output_language)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
