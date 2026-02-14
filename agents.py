import arxiv
from memory import Memory

memory = Memory()

# 1️⃣ Planner Agent
def planner_agent(query):
    return f"""
Research Plan for: {query}

1. Identify core concepts
2. Search relevant academic papers
3. Analyze methodologies
4. Compare findings
5. Identify research gaps
6. Generate structured report
"""

# 2️⃣ Research Agent
def research_agent(query):
    search = arxiv.Search(query=query, max_results=3)
    results = []

    for paper in search.results():
        summary = f"Title: {paper.title}\nSummary: {paper.summary}\n"
        results.append(summary)
        memory.add(summary)

    return "\n\n".join(results)

# 3️⃣ Critic Agent
def critic_agent(content):
    return """
Critical Analysis:

• Potential bias in dataset
• Limited real-world evaluation
• Risk of hallucinated interpretations
• Need benchmarking against baseline models
"""

# 4️⃣ Writer Agent
def writer_agent(query, research_data, critique):
    return f"""
RESEARCH REPORT

Title: {query}

Abstract:
This report analyzes current literature and evaluates multi-agent approaches.

Key Findings:
{research_data}

Limitations:
{critique}

Future Work:
• Improve evaluation benchmarks
• Add reflection mechanisms
• Implement memory-augmented reasoning
"""
