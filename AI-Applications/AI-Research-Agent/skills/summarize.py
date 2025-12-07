async def summarize_text(kernel, query: str, docs: list) -> str:
    if not docs:
        return f"No relevant documents found for '{query}'."
    
    prompt = f"""
    You are an expert research assistant.
    Summarize the information for the query: "{query}".
    Use ONLY the following documents: {docs}.
    Return the summary in 150 words max.
    Use bullet points or numbered list.
    Do not add information not present in the documents.
    """
    
    if kernel:
        summary = await kernel.chat("openai").complete_async(prompt)
    else:
        # Fallback simple summary: top 3 paragraphs
        summary = "\n- " + "\n- ".join(docs[:3])
    
    return summary
