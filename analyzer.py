import sys
import os

# Adds the main 'Resume_Analyzer_AI' folder to Python's search list
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.llama_client import LlamaClient

from models.llama_client import LlamaClient


class ResumeAnalyzer:

    def __init__(self):
        self.llm = LlamaClient()

    def analyze(self, structured_data):
        prompt = self._build_prompt(structured_data)
        response = self.llm.generate(prompt)
        return response

    def _build_prompt(self, data):
        return f"""
You are an expert HR and career coach.

Analyze the following resume data and provide:

1. Strengths
2. Weaknesses
3. Missing Skills
4. Suggestions for improvement

Resume Data:
Name: {data.get("name")}
Skills: {data.get("skills")}
Education: {data.get("education")}
Experience: {data.get("experience")}

Give clear and professional output.
"""


# ✅ TEST BLOCK
if __name__ == "__main__":
    from utils.text_cleaner import TextCleaner
    from tools.parser import ResumeParser

    file_path = r"C:\Users\Dell\Desktop\DeepakResume1.pdf"

    # Step 1: Parse
    parser = ResumeParser(file_path)
    raw_text = parser.parse()

    # Step 2: Clean + Structure
    cleaner = TextCleaner(raw_text)
    structured_data = cleaner.process()

    # Step 3: Analyze
    analyzer = ResumeAnalyzer()
    result = analyzer.analyze(structured_data)

    print("\n🤖 AI Resume Analysis:\n")
    print(result)