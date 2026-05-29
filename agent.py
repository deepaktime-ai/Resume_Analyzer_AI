from tools.parser import ResumeParser
from utils.text_cleaner import TextCleaner
from tools.analyzer import ResumeAnalyzer
from tools.matcher import JobMatcher
from tools.scorer import ResumeScorer
from rag.retriever import Retriever


class ResumeAgent:

    def __init__(self):
        self.analyzer = ResumeAnalyzer()
        self.matcher = JobMatcher()
        self.scorer = ResumeScorer()
        self.retriever = Retriever()
        self.retriever.load_data()

    def run(self, resume_path, job_description):
        print("\n🚀 Agent Started...\n")

        # Step 1: Parse
        parser = ResumeParser(resume_path)
        raw_text = parser.parse()

        # Step 2: Clean & Structure
        cleaner = TextCleaner(raw_text)
        structured_data = cleaner.process()

        # Step 3: Retrieve context (RAG)
        context = self.retriever.get_context("resume improvement tips")

        # Step 4: Analyze
        analysis = self.analyzer.analyze(structured_data)

        # Step 5: Match
        match_result = self.matcher.match(structured_data, job_description)

        # Step 6: Score
        score = self.scorer.score(structured_data)

        return {
            "structured_data": structured_data,
            "analysis": analysis,
            "job_match": match_result,
            "score": score,
            "rag_context": context
        }


# ✅ TEST BLOCK
if __name__ == "__main__":
    agent = ResumeAgent()

    resume_path = r"C:\Users\Dell\Desktop\DeepakResume1.pdf"

    job_description = """
    Looking for a Software Engineer with:
    - Python
    - Data Structures
    - Cloud knowledge
    """

    result = agent.run(resume_path, job_description)

    print("\n📊 FINAL OUTPUT:\n")

    for key, value in result.items():
        print(f"\n=== {key.upper()} ===\n")
        print(value)