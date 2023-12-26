```python
import unittest
from unittest.mock import patch, MagicMock
from openai_api import OpenAI_API

class TestOpenAI_API(unittest.TestCase):
    def setUp(self):
        self.api = OpenAI_API()
        self.mock_response = MagicMock()
        self.mock_response.choices = [MagicMock()]
        self.mock_response.choices[0].text.strip.return_value = "Test text"

    @patch('openai.Completion.create')
    def test_generate_text(self, mock_create):
        mock_create.return_value = self.mock_response
        result = self.api.generate_text("Test prompt")
        self.assertEqual(result, "Test text")
        mock_create.assert_called_once_with(engine=self.api.engine, prompt="Test prompt", max_tokens=100)

    @patch('openai.Completion.create')
    def test_translate_text(self, mock_create):
        mock_create.return_value = self.mock_response
        result = self.api.translate_text("Hello", "English", "Spanish")
        self.assertEqual(result, "Test text")
        mock_create.assert_called_once_with(engine=self.api.engine, prompt="Hello\nEnglish:Spanish translation:", max_tokens=100)

    @patch('openai.Completion.create')
    def test_generate_code_comments(self, mock_create):
        mock_create.return_value = self.mock_response
        result = self.api.generate_code_comments("print('Hello, World!')")
        self.assertEqual(result, "Test text")
        mock_create.assert_called_once_with(engine=self.api.engine, prompt="print('Hello, World!')\n# Comment:", max_tokens=100)

if __name__ == '__main__':
    unittest.main()
```
