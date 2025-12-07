import asyncio
from agent.agent import ResearchAssistantAgent
from rag.index_documents import index_documents

async def main():
    # Indexar documentos automáticamente
    print("📂 Indexing documents in 'docs/'...")
    index_documents(doc_folder="rag/docs", store_path="rag/store")
    
    # Crear agente
    agent = ResearchAssistantAgent()
    
    # Solicitar query al usuario
    query = input("🔎 Research question: ")
    
    # Ejecutar agente
    report = await agent.run(query)
    
    # Mostrar resultados de forma clara
    print("\n📝 Research Plan:\n")
    print(report.get("plan", "No plan generated."))
    
    print("\n📘 Summary:\n")
    print(report.get("summary", "No summary generated."))

if __name__ == '__main__':
    asyncio.run(main())
