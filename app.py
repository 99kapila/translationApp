from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    input_language = request.form.get('input_language')
    input_text = request.form.get('input_text')
    output_language = request.form.get('output_language')

    # Add your translation logic here

    # For now, let's just echo the input text
    output_text = input_text

    return render_template('index.html', input_language=input_language, input_text=input_text,
                           output_language=output_language, output_text=output_text)

if __name__ == '__main__':
    app.run(debug=True)
