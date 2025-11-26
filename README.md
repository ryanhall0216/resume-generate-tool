# 📄 Resume Tailor Tool

A Streamlit app that tailors your resume to a given job description using OpenAI.  
It generates a polished **DOCX** or **PDF** file with customizable styles and correct formatting.

---

## 🚀 Features
- Tailor your resume to any job description using OpenAI.
- Outputs **DOCX** or **PDF** resumes.
- Dynamic filename based on your name from the template file.
- Customizable font size, font color, and layout via sidebar.
- Auto-removes duplicate bullets and formats justified text.
- Always includes **Dates, Degree, Institution, GPA** in education.

---

## 📂 Project Structure
```

.
├── assets/
│   └── resume\_template.txt     # Your base resume text (first line = Name)
├── outputs/                    # Generated resumes will be saved here
├── .env                        # Stores your API key
├── 1.py                        # Main Streamlit app
├── requirements.txt            # Python dependencies
├── start.bat                   # (Optional) Windows batch file to launch app
└── README.md                   # This guide

````

---

## ⚙️ Setup

1. **Clone repo or copy files** into a project folder.  

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
````

3. **Set your OpenAI API key** in `.env`:

   ```
   OPENAI_API_KEY=your_api_key_here
   ```

4. **Edit your base resume** in:

   ```
   assets/resume_template.txt
   ```

   * First line → Your name (used for output file name).
   * Next lines → Contact info (e.g., email, phone).
   * Then add your resume content.

---

## ▶️ Run the App

```bash
streamlit run 1.py
```

or on Windows, you can double-click:

```
start.bat
```

---

## 🖊️ Usage

1. Paste a **job description** into the text box.
2. (Optional) Add a **custom prompt**.
3. Choose whether to include **technologies per position**.
4. Select output format: **DOCX** or **PDF**.
5. Adjust style settings (font, size, colors) from the sidebar.
6. Click **Generate Tailored Resume**.

Your tailored resume will be available for **download** and also saved in:

```
outputs/<Your_Name>.docx
outputs/<Your_Name>.pdf
```

---

## ✅ Example

**Input:**

* Resume: `assets/resume_template.txt`
* Job Description: Full-stack developer with Java + React

**Output:**

* `outputs/Javier_Bogran.docx`
* `outputs/Javier_Bogran.pdf`

---

## 💡 Notes

* Education block always includes: `Dates`, `Degree`, `Institution (school + location)`, `GPA`.
* All paragraphs are **justified** for professional look.
* Styles reset when app restarts, but you can extend to save `styles_config.json`.

---

## 🛠️ Tech Stack

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [python-docx](https://python-docx.readthedocs.io/)
* [ReportLab](https://www.reportlab.com/)
* [OpenAI API](https://platform.openai.com/)

---

## 📜 License

MIT License – free to use and modify.

```