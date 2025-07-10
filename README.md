
# 🤖 agentic-linkedin-post-generator

An agentic AI assistant that transforms your achievements, projects, and competitions into professional, personalized, and high-quality LinkedIn posts — using a multi-agent reasoning loop inspired by ReAct.

Built with **Streamlit**, **Ollama**, and custom AI agents for:
- 🧠 Post generation
- 🧐 Critique & iteration
- 🎨 Styling (tone adjustment)
- 📊 Optimization (hashtags, emojis, CTA)

---

## 🛠 Features

- ✅ Upload your achievements/projects as a CSV
- 🤖 Multi-agent collaboration to write, critique, and polish each post
- 🎭 Choose tone: inspirational, funny, professional, etc.
- 🔁 Run multiple refinement iterations

---

## 📁 File Structure

```bash

agentic-linkedin-post-generator/
│
├── app.py                 # Streamlit app UI
├── multi\_agent.py         # Multi-agent reasoning & refinement
├── prompts.py             # Prompt engineering for each agent
├── achievements.csv       # Your input data (e.g., projects, awards)
├── requirements.txt       # Python dependencies
└── README.md              # This file

```

---

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/agentic-linkedin-post-generator.git
cd agentic-linkedin-post-generator
```

### 2. Create Conda Environment

```bash
conda create -n agentic-posts python=3.10 -y
conda activate agentic-posts
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

Make sure you have Ollama running and models pulled:

```bash
ollama run llama3.2
streamlit run app.py
```

---

## 📄 CSV Format (Input File)

Name your file `achievements.csv` with at least these columns:

| Title                         | Description                                                  | Tags                              |
| ----------------------------- | ------------------------------------------------------------ | --------------------------------- |
| UNAS FEST 2022 – Debate Champ | National 1st place, discussed food security & sustainability | debate, leadership, communication |

---

## 📜 License

License — Free to use, build, and remix.
Credit appreciated if you use this for something cool. 🧠✨

---

## 🙋‍♂️ Author

**Hansen Dafa Pramudya Kusuma**
🎓 Information Systems @ Airlangga University
🔬 Focus: AI, ML, NLP, and intelligent automation
🌐 [linkedin.com/in/hansendafa](https://linkedin.com/in/hansendafa)

---