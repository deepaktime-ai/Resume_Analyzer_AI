import sys
import os

# Get the absolute path of the parent directory (Resume_Analyzer_AI)
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

# Now your import will work
from models.llama_client import LlamaClient

from models.llama_client import LlamaClient


class JobMatcher:

    def __init__(self):
        self.llm = LlamaClient()

    def match(self, structured_data, job_description):
        prompt = self._build_prompt(structured_data, job_description)
        response = self.llm.generate(prompt)
        return response

    def _build_prompt(self, data, job_desc):
        return f"""
You are an AI hiring assistant.

Compare the candidate resume with the job description.

Provide:
1. Match Percentage (0-100%)
2. Matching Skills
3. Missing Skills
4. Final Recommendation (Selected / Not Selected with reason)

Resume:
Skills: {data.get("skills")}
Education: {data.get("education")}
Experience: {data.get("experience")}

Job Description:
{job_desc}

Give output in a clear structured format.
"""


# ✅ TEST BLOCK
if __name__ == "__main__":
    from utils.text_cleaner import TextCleaner
    from tools.parser import ResumeParser

    file_path = r"C:\Users\Dell\Desktop\DeepakResume1.pdf"

    # Step 1: Parse Resume
    parser = ResumeParser(file_path)
    raw_text = parser.parse()

    # Step 2: Structure Data
    cleaner = TextCleaner(raw_text)
    structured_data = cleaner.process()

    # Step 3: Sample Job Description
    job_description = """
    We are hiring a Machine Learning Engineer.

    Requirements:
    - Strong Python skills
    - Experience in Machine Learning
    - Knowledge of Deep Learning
    - Familiarity with SQL
    - Experience with cloud platforms
    """

    # Step 4: Match
    matcher = JobMatcher()
    result = matcher.match(structured_data, job_description)

    print("\n📊 Job Match Analysis:\n")
    print(result)