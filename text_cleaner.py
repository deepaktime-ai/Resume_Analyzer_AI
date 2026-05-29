import sys
import os

# Adds the project root (Resume_Analyzer_AI) to the search path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.parser import ResumeParser


import re

class TextCleaner:

    def __init__(self, text):
        self.text = text

    def clean_text(self):
        # Remove extra spaces, symbols
        text = re.sub(r'\s+', ' ', self.text)
        return text.strip()

    def extract_email(self):
        match = re.findall(r'[\w\.-]+@[\w\.-]+', self.text)
        return match[0] if match else None

    def extract_phone(self):
        match = re.findall(r'\+?\d[\d\s\-]{8,15}', self.text)
        return match[0] if match else None

    def extract_name(self):
        # Simple heuristic: first line
        lines = self.text.strip().split("\n")
        return lines[0] if lines else None

    def extract_skills(self):
        skills_keywords = [
            "python", "java", "c++", "machine learning",
            "data science", "sql", "deep learning",
            "nlp", "tensorflow", "pandas"
        ]

        found_skills = []
        text_lower = self.text.lower()

        for skill in skills_keywords:
            if skill in text_lower:
                found_skills.append(skill)

        return found_skills

    def extract_education(self):
        education_keywords = ["b.tech", "m.tech", "bachelor", "master", "phd"]

        found = []
        text_lower = self.text.lower()

        for edu in education_keywords:
            if edu in text_lower:
                found.append(edu)

        return found

    def extract_experience(self):
        exp_keywords = ["experience", "intern", "worked", "company"]

        found = []
        text_lower = self.text.lower()

        for exp in exp_keywords:
            if exp in text_lower:
                found.append(exp)

        return found

    def process(self):
        return {
            "name": self.extract_name(),
            "email": self.extract_email(),
            "phone": self.extract_phone(),
            "skills": self.extract_skills(),
            "education": self.extract_education(),
            "experience": self.extract_experience()
        }


# ✅ TEST BLOCK
if __name__ == "__main__":
    from tools.parser import ResumeParser

    file_path = r"C:\Users\Dell\Desktop\DeepakResume1.pdf"

    parser = ResumeParser(file_path)
    raw_text = parser.parse()

    cleaner = TextCleaner(raw_text)
    structured_data = cleaner.process()

    print("\n🧠 Structured Resume Data:\n")
    for key, value in structured_data.items():
        print(f"{key}: {value}")