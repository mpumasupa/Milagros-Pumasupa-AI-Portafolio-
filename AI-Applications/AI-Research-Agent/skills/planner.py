async def plan_section(kernel, query: str, docs: list) -> str:
    if not docs:
        return f"No documents available for '{query}'."
    
    prompt = f"""
    You are a research assistant.
    Create a concise research plan for the query: "{query}".
    Use ONLY the following documents: {docs}.
    Return the plan as 3-5 bullet points.
    """
    
    if kernel:
        plan = await kernel.chat("openai").complete_async(prompt)
    else:
        # Fallback simple plan
        plan = f"Research plan for '{query}' using {len(docs)} documents."
    
    return plan
