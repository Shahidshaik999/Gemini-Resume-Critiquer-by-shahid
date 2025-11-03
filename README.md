
# 📄 Gemini Resume Critiquer — Setup & Troubleshooting

> A complete step-by-step README to reproduce the Gemini + Streamlit Resume Analyzer app built by **Shaik Shahid**.  
> Includes every command, verified versions, and solutions to common setup errors — so future users won’t face the same issues.

---

## 🚀 Project Summary

This project is an **AI-powered Resume Analyzer** built using **Google Gemini API** and **Streamlit**.  
It extracts text from uploaded resumes (PDF/TXT) and provides smart, structured feedback on:

- Resume clarity and formatting  
- Skill visibility  
- Relevance for a specific job role  
- Areas of improvement  

---

## ✅ Prerequisites

- Windows OS (PowerShell recommended)  
- **Python 3.12+** installed  
- A valid **Google Generative AI API key** from [Google AI Studio](https://aistudio.google.com/app/apikey)  
- Internet connection for model access

---

## 🧾 Verified Versions

| Package | Version |
|----------|----------|
| Python | 3.12.x |
| streamlit | 1.51.0 |
| google-generativeai | 0.8.5 |
| PyPDF2 | 3.0.1 |
| python-dotenv | 1.2.1 |

---

## 🪜 Step 1: Create Project Environment

```bash
cd "C:\Users\<your-user>\OneDrive\Desktop"
mkdir Resume_SW
cd Resume_SW
py -3.12 -m venv .venv
.venv\Scripts\activate
```

After activation, your prompt should look like: `(.venv)`

---

## 🪜 Step 2: Install Dependencies

```bash
pip install --upgrade pip
pip install streamlit google-generativeai PyPDF2 python-dotenv
```

---

## 🪜 Step 3: Setup Google API Key

Create a `.env` file in your project folder and paste your Gemini API key:

```
GOOGLE_API_KEY=your_google_api_key_here
```

> ⚠️ **Note:** Never share or upload your `.env` file to GitHub.

---

## 🪜 Step 4: Create `app.py`

Here’s the working version of the main app:

```python
import streamlit as st
import PyPDF2, io, os, google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.title("📄 Gemini Resume Critiquer")
uploaded = st.file_uploader("Upload Resume (PDF/TXT)", type=["pdf", "txt"])
if uploaded:
    reader = PyPDF2.PdfReader(uploaded)
    resume_text = ''.join(page.extract_text() for page in reader.pages)
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    response = model.generate_content(f"Analyze this resume and provide structured feedback: {resume_text}")
    st.subheader("🧠 AI Analysis Results")
    st.write(response.text)
```

---

## 🪜 Step 5: Run the App

```bash
streamlit run app.py
```

If Streamlit is not recognized:

```bash
python -m streamlit run app.py
```

Then open the local app in your browser:  
👉 **http://localhost:8501**

---

## 🧩 Troubleshooting

| Error | Cause | Solution |
|-------|--------|-----------|
| `'streamlit' not recognized` | Virtual environment not active | Run `.venv\Scripts\activate` then reinstall: `pip install streamlit` |
| `Invalid API key` | Wrong or expired Gemini key | Regenerate key from [AI Studio](https://aistudio.google.com/app/apikey) |
| `Missing modules` | Packages not installed in active env | `pip install google-generativeai PyPDF2 python-dotenv` |

---

## 📂 Folder Structure

```
Resume_SW/
 ├── app.py
 ├── .env
 ├── .venv/
 ├── requirements.txt
 └── README.md
```

---

## 💡 Tips

- Use `models/gemini-2.5-flash` for fast and cost-efficient analysis  
- Keep `.env` file secret (never push it to GitHub)  
- Activate your venv every time you open the project  
- Add a simple `requirements.txt` for portability

---

## 🧾 Example `requirements.txt`

```
streamlit==1.51.0
google-generativeai==0.8.5
PyPDF2==3.0.1
python-dotenv==1.2.1
```

---

## 🧠 Lessons Learned

- Always check which Python version your `pip` is using (`py -3.12 -m pip`)  
- If Streamlit fails, reinstall it inside the active environment  
- Keep your Gemini API key in `.env`, not hardcoded  

---

## 🧑‍💻 Author

**Shaik Shahid**  
B.Tech CSE (AI & ML)  
📧 [shahidshaik9898p@gmail.com](mailto:shahidshaik9898p@gmail.com)  
🔗 [LinkedIn](https://linkedin.com/in/shaik-shahid-7a1897282) | [GitHub](https://github.com/Shahidshaik999)

---

### 📜 License

**MIT License** — free to use and modify with attribution.
