```python
from flask import Flask, request, jsonify
from openai_api import OpenAI_API

app = Flask(__name__)
openai_api = OpenAI_API()

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data.get('text')
    source_lang = data.get('source_lang')
    target_lang = data.get('target_lang')

    if not text or not source_lang or not target_lang:
        return jsonify({'error': 'Missing required parameter'}), 400

    try:
        translated_text = openai_api.translate_text(text, source_lang, target_lang)
        return jsonify({'translated_text': translated_text}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
