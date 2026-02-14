import streamlit as st
import time
from agents import planner_agent, research_agent, critic_agent, writer_agent

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="AutoResearcher | Multi-Agent Research System",
    page_icon="🛰️",
    layout="wide"
)

# --------------------------------------------------
# Minimal Sony-Style CSS
# --------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #ffffff;
}
.main-title {
    font-size: 42px;
    font-weight: 600;
    letter-spacing: 1px;
}
.subtitle {
    font-size: 16px;
    color: #666;
}
.section-box {
    padding: 25px;
    border-radius: 10px;
    border: 1px solid #e6e6e6;
    margin-bottom: 25px;
}
.agent-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 10px;
}
.metric-box {
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #eee;
    text-align: center;
}
.footer {
    text-align: center;
    font-size: 12px;
    color: gray;
    margin-top: 50px;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Header
# --------------------------------------------------
st.markdown('<div class="main-title">AutoResearcher</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Multi-Agent Autonomous Research Pipeline | Planner → Research → Critic → Writer</div>', unsafe_allow_html=True)
st.divider()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("System Overview")
st.sidebar.markdown("Mode: Local Simulation")
st.sidebar.markdown("Architecture: Modular Multi-Agent")
st.sidebar.markdown("Memory: In-Memory Store")
st.sidebar.markdown("Design: Decoupled UI & Reasoning Layer")
st.sidebar.divider()
st.sidebar.markdown("Built for AI Research Evaluation")

# --------------------------------------------------
# Input
# --------------------------------------------------
query = st.text_input("Enter Research Question")

run_button = st.button("Run Research Pipeline")

if run_button and query:

    progress = st.progress(0)
    status = st.empty()

    # ---------------- Planner ----------------
    status.info("Planner Agent structuring research plan...")
    time.sleep(1)
    plan = planner_agent(query)
    progress.progress(25)

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="agent-title">Planner Agent</div>', unsafe_allow_html=True)
    st.write(plan)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- Research ----------------
    status.info("Research Agent retrieving academic sources...")
    time.sleep(2)
    research = research_agent(query)
    progress.progress(50)

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="agent-title">Research Agent</div>', unsafe_allow_html=True)
    with st.expander("View Retrieved Papers"):
        st.write(research)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- Critic ----------------
    status.info("Critic Agent evaluating findings...")
    time.sleep(1)
    critique = critic_agent(research)
    progress.progress(75)

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="agent-title">Critic Agent</div>', unsafe_allow_html=True)
    st.write(critique)
    st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- Writer ----------------
    status.info("Writer Agent generating final structured report...")
    time.sleep(2)
    report = writer_agent(query, research, critique)
    progress.progress(100)

    st.markdown('<div class="section-box">', unsafe_allow_html=True)
    st.markdown('<div class="agent-title">Final Research Report</div>', unsafe_allow_html=True)
    st.write(report)
    st.markdown('</div>', unsafe_allow_html=True)

    status.success("Multi-Agent Execution Completed")

    # --------------------------------------------------
    # Evaluation Metrics (Professional Touch)
    # --------------------------------------------------
    st.divider()
    st.subheader("Research Evaluation Metrics")

    col1, col2, col3 = st.columns(3)

    col1.metric("Agents Executed", "4")
    col2.metric("Sources Retrieved", "3")
    col3.metric("Pipeline Status", "Stable")

    # --------------------------------------------------
    # Download Button
    # --------------------------------------------------
    st.download_button(
        label="Download Research Report",
        data=report,
        file_name="AutoResearch_Report.txt"
    )

# --------------------------------------------------
# Architecture Section
# --------------------------------------------------
st.divider()
st.subheader("System Architecture")

st.markdown("""
This system follows a modular multi-agent orchestration pattern.

• Planner Agent – Task decomposition  
• Research Agent – Academic source retrieval  
• Critic Agent – Analytical validation  
• Writer Agent – Structured synthesis  

Each agent operates independently and passes structured output 
through a sequential pipeline, enabling backend LLM swapping 
without affecting UI or orchestration logic.
""")

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown('<div class="footer">AutoResearcher v2.0 | AI Research Evaluation System</div>', unsafe_allow_html=True)
