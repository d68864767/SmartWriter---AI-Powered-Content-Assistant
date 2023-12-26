```python
import openai
import os

# Load your OpenAI API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

class OpenAI_API:
    def __init__(self):
        self.engine = "text-davinci-002"  # You can use other engines like "text-davinci-002", "text-curie-002"

    def generate_text(self, prompt, max_tokens=100):
        """
        Function to generate text using OpenAI GPT-3 or GPT-4 model.
        """
        response = openai.Completion.create(
            engine=self.engine,
            prompt=prompt,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()

    def translate_text(self, text, source_lang, target_lang):
        """
        Function to translate text from one language to another.
        """
        # Construct the prompt
        prompt = f"{text}\n{source_lang}:{target_lang} translation:"
        
        # Generate the translated text
        translated_text = self.generate_text(prompt)
        
        return translated_text

    def generate_code_comments(self, code):
        """
        Function to generate comments for a given code snippet.
        """
        # Construct the prompt
        prompt = f"{code}\n# Comment:"
        
        # Generate the comment
        comment = self.generate_text(prompt)
        
        return comment
```
