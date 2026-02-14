# Multi-Agent Research Orchestrator

A modular multi-agent system designed to simulate autonomous academic research generation using a structured orchestration pipeline.

---

## Overview

Multi-Agent Research Orchestrator demonstrates how complex research workflows can be decomposed into specialized reasoning agents.

The system separates responsibilities into independent components to improve clarity, maintainability, and extensibility.

---

## Architecture

The system follows a sequential multi-agent pipeline:

User Query  
→ Planner Agent  
→ Research Agent (arXiv retrieval)  
→ Critic Agent  
→ Writer Agent  
→ Structured Research Report  

Each agent performs a specific role and passes structured output to the next stage.

The architecture is backend-agnostic and can support different language models without modifying the UI layer.

---

## Agents

### Planner Agent
Breaks down the research question into structured sub-tasks.

### Research Agent
Retrieves relevant academic papers using the arXiv API.

### Critic Agent
Analyzes findings and identifies limitations or gaps.

### Writer Agent
Generates a structured research-style report.

---

## Features

- Modular multi-agent design
- Clear separation of concerns
- Research-oriented user interface (Streamlit)
- Academic source retrieval
- Evaluation metrics display
- Downloadable research report
- Extensible backend architecture

---


---

## Design Principles

- Modularity
- Scalability
- Clear orchestration logic
- Decoupled UI and reasoning components
- Extensibility for future LLM integration

---

## Future Enhancements

- Hallucination risk scoring
- Single-agent vs multi-agent benchmarking
- Backend model integration
- Dynamic evaluation metrics
- Research confidence scoring

---

## Author

Yash Jagtap  
Computer Science Engineer  
AI Systems & Cybersecurity

---

## License

MIT License

<img width="1919" height="1022" alt="image" src="https://github.com/user-attachments/assets/388122c7-47d5-406e-9aa1-6906001c7995" />
<img width="1919" height="1033" alt="image" src="https://github.com/user-attachments/assets/13d4aa85-6c70-4425-9aac-8bb12a6716cc" />
<img width="1901" height="1031" alt="image" src="https://github.com/user-attachments/assets/e3a6050d-cc1f-4822-9e28-7d32bcff77ed" />
