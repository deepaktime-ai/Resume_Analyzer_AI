from models.llama_client import LlamaClient


class ResumeScorer:

    def __init__(self):
        self.llm = LlamaClient()

    def score(self, structured_data):
        prompt = self._build_prompt(structured_data)
        response = self.llm.generate(prompt)
        return response

    def _build_prompt(self, data):
        return f"""
You are an ATS (Applicant Tracking System).

Evaluate the resume and provide:

1. Overall Score (0–100)
2. Score Breakdown:
   - Skills (out of 40)
   - Experience (out of 30)
   - Education (out of 20)
   - Formatting (out of 10)
3. Final Feedback

Resume Data:
Skills: {data.get("skills")}
Education: {data.get("education")}
Experience: {data.get("experience")}

Be strict and realistic like a real ATS system.
"""


# ✅ TEST BLOCK
if __name__ == "__main__":
    from utils.text_cleaner import TextCleaner
    from tools.parser import ResumeParser

    file_path = r"C:\Users\Dell\Desktop\DeepakResume1.pdf"

    # Step 1: Parse
    parser = ResumeParser(file_path)
    raw_text = parser.parse()

    # Step 2: Structure
    cleaner = TextCleaner(raw_text)
    structured_data = cleaner.process()

    # Step 3: Score
    scorer = ResumeScorer()
    result = scorer.score(structured_data)

    print("\n📈 Resume ATS Score:\n")
    print(result)