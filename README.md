# 🎤 AI Speaking Examiner (B2)

An AI-powered English Speaking Examiner built with **Streamlit** and **Google Gemini API**.  
This app simulates a real speaking test examiner and provides structured, detailed feedback on English speaking performance.

---

## 🚀 Live Demo
https://raymentor-ituresrurvixjl9rwmovzt.streamlit.app/

---

## 📌 Features

- 🧠 AI-powered speaking evaluation using Google Gemini
- 🎯 Structured feedback:
  - Grammar
  - Vocabulary
  - Fluency
  - Coherence & Cohesion
- 📝 IELTS / B2-style speaking tasks (Part 1, 2, 3 simulation)
- 💬 Chat-like interactive UI
- 🎨 Custom UI styling for a clean exam interface
- ⚡ Fast response generation via Gemini API

---

## 🛠 Tech Stack

- Python 3.10+
- Streamlit
- Google Generative AI (`google-genai`)
- python-dotenv

---

## 📁 Project Structure
|- app.py                # Main Streamlit application
|- system_prompt.txt     # AI examiner prompt template
|- requirements.txt      # Python dependencies
|- assets/
    |- Ray_Mentor.png    # UI assets/logo
|- .gitignore
|- README.md

---

## ⚙️ Setup Instructions (Local)

### 1. Clone repository
git clone https://github.com/KhangNguyen08/RayMentor.git
cd RayMentor

## 2. Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

## 3. Install dependencies
pip install -r requirements.txt

## 4. Configure environment variables
Create a .env file in the root directory:

GEMINI_API_KEY=your_api_key_here

## ▶️ Run application locally
streamlit run app.py

## 🌐 Deployment (Streamlit Cloud)
- Push code to GitHub  
- Go to https://share.streamlit.io  
- Select repository: RayMentor  
- Set Main file: app.py  
- Add Secret in Streamlit:

GEMINI_API_KEY = "your api here"

- Click Deploy 🚀

## 🔐 Security Notes
- Never commit .env to GitHub
- Always use Streamlit Secrets for production deployment
- API keys must be kept private

## 📈 Future Improvements
- User authentication system
- Save speaking history (database integration)
- Real-time streaming feedback
- Band score prediction model
- Analytics dashboard for progress tracking

## 👨‍💻 Author
Built by Khang Nguyen

## 📄 License
MIT License
