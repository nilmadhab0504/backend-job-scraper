### **README for Flask Backend Application**

---

#### **Overview**
This Flask-based backend application powers a semantic search engine to match resumes with job descriptions and generate customized cover letters. The backend performs the following functions:

1. Parses uploaded resumes.
2. Integrates with OpenAI to generate job role suggestions.
3. Scrapes job data from Apna.co for the suggested roles.
4. Utilizes `sentence_transformers` and `FAISS` for efficient job recommendation.

---

### **Getting Started**

#### **Prerequisites**
- Python 3.10 installed on your system.
- `pip` (Python package manager).
- A working internet connection to download dependencies and models.

---

### **Installation Instructions**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nilmadhab0504/backend-job-scraper
   cd backend-job-scraper
   ```

2. **Set Up a Virtual Environment**
   Create a virtual environment using Python 3.10:
   ```bash
   python3.10 -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```cmd
     venv\Scripts\activate
     ```

4. **Install Required Dependencies**
   Install all the dependencies listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

5. **Install Additional Libraries**
   Since `sentence_transformers` and `faiss` are not always included in `requirements.txt`, install them separately:
   ```bash
   pip install sentence_transformers faiss-cpu
   ```

   > *If you have a GPU-enabled system and want to leverage it, install `faiss-gpu` instead:*
   ```bash
   pip install faiss-gpu
   ```

6. **Run the Application**
   Start the Flask application by running:
   ```bash
   python app.py
   ```

   The application will run on port **4000**. Open your web browser and navigate to:
   ```
   http://127.0.0.1:4000
   ```

---

### **Usage**
- Open your web browser and navigate to `http://127.0.0.1:4000`.
- Use the provided endpoints for uploading resumes, generating job matches, and creating cover letters.

---
