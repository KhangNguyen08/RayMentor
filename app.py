import os
import base64
import streamlit as st
from streamlit.components.v1 import html as components_html
from dotenv import load_dotenv
from google import genai

def get_base64_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = get_base64_image("assets/Ray_Mentor.png")

st.set_page_config(page_title="B2 Speaking Examiner", page_icon="assets/Ray_Mentor.png", layout="wide")

st.markdown("""
<style>
:root {
    --ink: #2b2f38;
    --royal: #2952a3;
    --royal-dark: #1e3d80;
    --bg-soft: #f4f6f9;
    --cream: #f7f1e3;
    --border-soft: #e2e5ea;
}

section[data-testid="stSidebar"] {
    background-color: var(--bg-soft);
    border-right: 1px solid var(--border-soft);
}

h1, h2, h3, .stMarkdown h1 {
    color: var(--ink) !important;
}

.eyebrow {
    color: var(--royal);
    font-size: 0.8rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 0.1rem;
}

textarea {
    border-radius: 8px !important;
}
textarea:focus {
    border-color: var(--royal) !important;
    box-shadow: 0 0 0 1px var(--royal) !important;
}

button[kind="primary"] {
    background-color: var(--royal) !important;
    border-color: var(--royal) !important;
}
button[kind="primary"]:hover {
    background-color: var(--royal-dark) !important;
    border-color: var(--royal-dark) !important;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: var(--royal) !important;
}

.full-bleed {
    width: 100vw;
    position: relative;
    left: 50%;
    right: 50%;
    margin-left: -50vw;
    margin-right: -50vw;
    margin-top: -1rem;
}

.block-container {
    max-width: 1500px;
    padding-top: 0rem;
    margin: 0 auto;
}

header[data-testid="stHeader"] {
    display: none;
}

div[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stWidgetLabel"] p {
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    color: var(--ink) !important;
}
</style>
""", unsafe_allow_html=True)

# Load environment variables
load_dotenv()

# Initialize Gemini client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Load system prompt
with open("system_prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

MODEL_ROUTER = {
    "Part 1": "gemini-2.5-flash",
    "Part 2": "gemini-2.5-flash",
    "Part 3": "gemini-2.5-pro",
    "Part 4": "gemini-2.5-flash",
}   

# ----------------------------
# Streamlit UI
# ----------------------------

st.markdown(f"""
<div class="full-bleed" style="
    background-color: var(--royal);
    padding: 1.1rem 2.5rem;
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
">
    <img src="data:image/png;base64,{logo_base64}" style="height: 100px;">
    <span style="color: #ffffff; font-size: 1.6rem; font-weight: 700;">
        Ray Studio | AI Speaking Examiner
    </span>
</div>
<div style="
    color: var(--royal);
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1.4rem;
">
    Cambridge B2 First for Schools
</div>
""", unsafe_allow_html=True)

st.divider()

st.markdown("""
<p style="text-align: center; color: var(--ink); font-size: 1.15rem; margin-bottom: 0.6rem;">
    Please select the speaking part you want to assess
</p>
""", unsafe_allow_html=True)

col_l, col_c, col_r = st.columns([1, 2, 1])
with col_c:
    part = st.selectbox(
        "Speaking Part",
        ["Part 1", "Part 2", "Part 3", "Part 4"],
        label_visibility="collapsed"
    )
    show_debug = st.checkbox("Show prompt (debug)")

st.divider()

if part in ["Part 1", "Part 4"]:
    col1, col2 = st.columns(2)
    with col1:
        question = st.text_area("Question", height=200)
    with col2:
        answer = st.text_area("Student's Answer", height=200)

elif part == "Part 2":
    col1, col2 = st.columns(2)
    with col1:
        question = st.text_area("Task / Instructions", height=200)
        image = st.file_uploader("Upload image (Part 2)")
        if image is not None:
            st.image(image, use_container_width=True)
    with col2:
        answer = st.text_area("Student monologue", height=200)

elif part == "Part 3":
    col1, col2 = st.columns(2)
    with col1:
        question = st.text_area("Discussion Question", height=100)
        ideas = st.text_area("5 suggested ideas", height=200)
    with col2:
        dialogue = st.text_area("Candidate A/B discussion", height=200)

components_html("""
<script>
const doc = window.parent.document;

function autoResize(area) {
    area.style.height = "auto";
    area.style.height = (area.scrollHeight + 4) + "px";
}

function attach() {
    doc.querySelectorAll("textarea").forEach(area => {
        if (!area.dataset.autoResizeAttached) {
            area.dataset.autoResizeAttached = "true";
            area.style.overflowY = "hidden";
            area.addEventListener("input", () => autoResize(area));
            autoResize(area);
        }
    });
}

attach();
new MutationObserver(attach).observe(doc.body, {
    childList: true,
    subtree: true
});
</script>
""", height=0)

st.divider()

# ----------------------------
# Evaluate
# ----------------------------

if st.button("Evaluate", type="primary", use_container_width=True):

    model_name = MODEL_ROUTER.get(part, "gemini-2.5-flash")

    st.caption(f"Using model: {model_name}")

    if part == "Part 1":
        prompt = f"""
{SYSTEM_PROMPT}

PART 1 (INTERVIEW)

Question:
{question}

Student's Answer:
{answer}
"""

    elif part == "Part 2":
        prompt = f"""
{SYSTEM_PROMPT}

PART 2 (LONG TURN - IMAGE DESCRIPTION)

Task:
{question}

Student monologue:
{answer}
"""

    elif part == "Part 3":
        prompt = f"""
{SYSTEM_PROMPT}

PART 3 (DISCUSSION)

Question:
{question}

Suggested ideas:
{ideas}

Dialogue:
{dialogue}
"""

    elif part == "Part 4":
        prompt = f"""
{SYSTEM_PROMPT}

PART 4 (OPINION)

Question:
{question}

Student's Answer:
{answer}
"""

    if show_debug:
        with st.expander("Prompt sent to model"):
            st.code(prompt, language="markdown")

    with st.spinner(f"Evaluating with {model_name}..."):

        response = client.models.generate_content(
            model=model_name,
            contents=prompt
        )

    st.divider()
    st.subheader("Feedback")
    with st.container(border=True):
        st.markdown(response.text)
