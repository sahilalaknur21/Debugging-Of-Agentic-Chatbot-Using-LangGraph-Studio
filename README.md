<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=10,20,50&height=240&section=header&text=Debugging%20CHATBOT%20WITH%20LangGraph%20Studio(3.O)&fontSize=30&fontColor=fff&animation=fadeIn&fontAlignY=38" width="100%">
</picture>
<br/>

<div align="center">

<a href="https://github.com/sahilalaknur21/Debugging-Agentic-Chatbot">
  <img src="https://socialify.git.ci/sahilalaknur21/Debugging-Agentic-Chatbot/image?description=Advanced%20Agent%20Observability%20%26%20Reliability%20Engineering&font=JetBrains%20Mono&name=Agentic%20Debugger%20Pro&owner=1&pattern=Circuit%20Board&theme=Dark" width="100%">
</a>

<br/>

<p>
  <img src="https://img.shields.io/badge/Focus-Observability-FF6B6B?style=for-the-badge&logo=target&logoColor=white" alt="Focus"/>
  <img src="https://img.shields.io/badge/Tool-LangGraph_Studio-4285F4?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Studio"/>
  <img src="https://img.shields.io/badge/Stack-Groq_LPU-F55036?style=for-the-badge&logo=lightning&logoColor=white" alt="Groq"/>
  <img src="https://img.shields.io/badge/Environment-Local_Dev-34A853?style=for-the-badge&logo=windows-terminal&logoColor=white" alt="Local"/>
</p>

</div>

<br/>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br/>

## 🧐 The "Black Box" Problem

Building agents is easy. **Fixing them is hard.**

Most AI development stops at `print(response)`. But when an agent enters an infinite loop, hallucinates a math result, or calls the wrong tool, standard logging isn't enough. You need **X-Ray Vision** into the agent's brain.

This repository is a **Reliability Engineering** sandbox. It moves the **Agentic Chatbot (ReAct Architecture)** into **LangGraph Studio** to demonstrate advanced debugging, state rewinding, and human-in-the-loop (HITL) workflows.

<br/>

## 🔬 Debugging Capabilities

<div align="center">

| Feature | Description | Why it matters |
| :--- | :--- | :--- |
| **🔍 Visual Inspection** | See the exact path the agent takes (LLM → Tool → LLM). | Instantly spot cyclic loops or logic errors. |
| **⏮️ Time Travel** | Rewind the agent to a previous state and "fork" the conversation. | Test fixes without restarting the entire chat. |
| **🛑 HITL Interrupts** | Pause execution before specific tool calls (e.g., `write_to_db`). | Prevent dangerous actions before they happen. |
| **🧪 Node Isolation** | Test the `math_tool` or `search_tool` independently. | Verify tools work before the LLM tries to use them. |

</div>

<br/>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br/>

## 🏗 System Architecture (The "Glass Box")

By running this project in **LangGraph Studio**, the architecture becomes fully transparent.

<div align="center">

<table>
  <tr>
    <td align="center" width="33%">
      <img src="https://img.icons8.com/color/96/monitor.png" width="80" alt="Studio"/>
      <br/><br/>
      <h3>🖥️ The Studio</h3>
      <sub><b>Localhost:2024</b><br/>The UI frontend that connects to the underlying LangGraph API.</sub>
    </td>
    <td align="center" width="33%">
      <img src="https://img.icons8.com/color/96/server.png" width="80" alt="Server"/>
      <br/><br/>
      <h3>⚙️ The API Server</h3>
      <sub><b>LangGraph CLI</b><br/>Runs the `agent.py` graph in an in-memory FastAPI server.</sub>
    </td>
    <td align="center" width="33%">
      <img src="https://img.icons8.com/color/96/database.png" width="80" alt="State"/>
      <br/><br/>
      <h3>💾 The State</h3>
      <sub><b>In-Memory Store</b><br/>Persists the conversation thread allowing for state rewinding.</sub>
    </td>
  </tr>
</table>

</div>

<br/>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

<br/>

## ⚡ Quick Start (Debugging Mode)

### 1. Install the Debugger

pip install -U "langgraph-cli[inmem]"

### 2. Configure Environment
Create a .env file with your API keys:

Code snippet

GROQ_API_KEY="your_key"
TAVILY_API_KEY="your_key"
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY="your_key"
3. Launch the Studio
Run this command in your project root:



langgraph dev
Success: The terminal will show 🚀 API: http://127.0.0.1:2024. Open your browser to the Studio UI link provided.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif">

## 🧪 How to Debug (Walkthrough)
Once the Studio is running, try these "Stress Tests" to see the debugging in action:

The "Math Hallucination" Test:

Prompt: "Calculate 50 + 20 then divide by 0."

Observation: Watch the divide tool throw an error.

Action: Edit the state to change "0" to "2" and resume execution.

The "Loop" Test:

Prompt: "Keep searching for the weather until you find it."

Observation: Watch the graph cycle between llm and search.

Action: Use the "Interrupt" button to manually stop the agent.

<div align="center">

## 💡 Engineered by Sahil Alaknur
<p> <sub>Mastering AI Reliability & Observability. ⭐ Star this repo if you find it useful!</sub> </p>

<img src="https://www.google.com/url?sa=E&source=gmail&q=https://capsule-render.vercel.app/api?type=waving%26color=gradient%26customColorList=10,20,50%26height=120%26section=footer" width="100%">

</div>

