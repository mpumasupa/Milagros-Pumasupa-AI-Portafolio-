import os
from dotenv import load_dotenv
from semantic_kernel import Kernel
from rag.retriever import Retriever
from skills.summarize import summarize_text
from skills.planner import plan_section
from agent._config import MODEL

class ResearchAssistantAgent:

    def __init__(self):
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")

        if api_key:
            self.kernel = Kernel()
            from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
            self.kernel.add_service(
                OpenAIChatCompletion(
                    service_id="openai",
                    api_key=api_key
                )
            )
        else:
            self.kernel = None
            print("⚠️ OPENAI_API_KEY not found. Using local fallback.")

        self.retriever = Retriever()

    async def run(self, query: str):
        print("\n🔍 Searching for relevant information...\n")
        docs = self.retriever.search(query, k=5)
        print(f"Retrieved {len(docs)} relevant documents.\n")

        print("🧠 Generating research plan...\n")
        plan = await plan_section(self.kernel, query, docs)
        print("📑 Plan summary:\n", plan)

        print("\n✍️ Producing final report...\n")
        final_report = await summarize_text(self.kernel, query, docs)
        print("📝 Summary:\n", final_report)

        return {"plan": plan, "summary": final_report}
