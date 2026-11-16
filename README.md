# 🦜️🔗 LangChain Modern — Practical Guide & Integration Starter

A comprehensive, modular tutorial series and production starter kit for modern **LangChain (v0.2+)**, **Ollama**, and **Hugging Face Inference**.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-v0.2+-1C3C3C?style=flat&logo=langchain&logoColor=white)](https://python.langchain.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-black?style=flat&logo=ollama&logoColor=white)](https://ollama.com/)
[![HuggingFace](https://img.shields.io/badge/Hugging_Face-Serverless-FFD21E?style=flat&logo=huggingface&logoColor=black)](https://huggingface.co/)

---

## 📚 Notebook Curriculum (`updated/`)

| # | Notebook | Focus Areas | Key Concepts |
|---|---|---|---|
| 01 | [`1-langchain_intro.ipynb`](updated/1-langchain_intro.ipynb) | LangChain Fundamentals | LCEL, PromptTemplates, StrOutputParser |
| 02 | [`2-model_integration.ipynb`](updated/2-model_integration.ipynb) | Multi-Provider Models | ChatOllama, HuggingFaceEndpoint, Groq |
| 03 | [`3-tools.ipynb`](updated/3-tools.ipynb) | Tool Calling & Function Execution | `@tool` decorator, StructuredTool, args schema |
| 04 | [`4-messages.ipynb`](updated/4-messages.ipynb) | Message State Management | `HumanMessage`, `SystemMessage`, `AIMessage` |
| 05 | [`5-structured_outputs.ipynb`](updated/5-structured_outputs.ipynb) | Type-Safe Extraction | Pydantic v2 schemas, `.with_structured_output()` |
| 06 | [`6-middleware.ipynb`](updated/6-middleware.ipynb) | Middleware & Callbacks | Logging, tracing, custom runnable wrappers |

---

## 🚀 Quick Start (`main.py`)

Run the unified test runner to verify local and serverless LLM connectivity:

```bash
# 1. Install dependencies with uv or pip
pip install -r requirements.txt

# 2. Configure .env
cp .env.example .env
# Add HUGGINGFACEHUB_API_TOKEN

# 3. Run interactive runner
python main.py
```

### Options:
1. **Local Ollama Model**: Connects to `http://localhost:11434` with `ChatOllama` (default: `qwen` / `llama3`).
2. **Hugging Face Serverless**: Queries `Qwen/Qwen2.5-72B-Instruct` via free serverless API endpoint.
3. **Dual Pipeline**: Runs both in sequence to benchmark latency.

---

## 🛠️ Tech Stack & Requirements

- Python 3.11+
- `langchain-core`, `langchain-community`
- `langchain-ollama`, `langchain-huggingface`
- Managed via `uv` or `pip`

---

<sub>Maintained by [Kaushal Sharma](https://github.com/Kaushal-1925)</sub>
