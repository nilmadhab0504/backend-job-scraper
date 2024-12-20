import json
from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from scraper import Scraper 
from resumeparser import ResumeParser
from jobsearchengine import JobSearchEngine
from llmservice import LLMService 
import io
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"
load_dotenv() 
app = Flask(__name__)
CORS(app)

LlmService = LLMService(api_key="api key")
        
@app.route('/api/parse-and-search', methods=['POST'], strict_slashes=False)
def parse_and_search():
    if 'file' not in request.files:
        print("No file found in request.") 
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        print("No file selected.")
        return jsonify({"error": "No selected file"}), 400

    file.seek(0) 
    file_stream = io.BytesIO(file.read())

    if file and (file.filename.endswith('.pdf') or file.filename.endswith('.docx')):
        try:
            print("Valid file type detected. Parsing the resume...")
            matcher = ResumeParser()
            resume_text = matcher.parse_resume(file_stream)
            prompt = (
    f"Based on the resume text provided: {resume_text}, extract  "
    f"a JSON array of job suggestions (Job_List) that align with the candidate's skills and "
    f"qualifications. Format the response as a JSON object 'Job_List'."
)

            response = LlmService.get_llm_result(prompt=prompt)
            print(response)
            if isinstance(response, str):
                try:
                    response = json.loads(response)
                except json.JSONDecodeError as e:
                    raise ValueError(f"Failed to parse LLM response as JSON: {str(e)}")
            keywords = response.get('Job_List')
            if not keywords:
               return jsonify({"error": "Invalid response from LLM. Missing 'yr_exp' or 'Job_List'."}), 500
           
            scraper_instance = Scraper()
            jobs = scraper_instance.scrape(keywords)
            job_search_engine = JobSearchEngine(jobs)
            results = job_search_engine.search(resume_text)

            if results:
                return jsonify({"results": results, "resume_text":resume_text}), 200
            else:
                print("No matching jobs found.") 
                return jsonify({"results": [], "message": "No matching jobs found."}), 200
        except Exception as e:
            print(f"Error parsing resume or searching jobs: {str(e)}") 
            return jsonify({"error": f"Failed to process resume or search jobs: {str(e)}"}), 500
    else:
        print("Unsupported file type. Only PDF and DOCX are allowed.") 
        return jsonify({"error": "Unsupported file type. Please provide a PDF or DOCX file."}), 400



@app.route('/api/generate-cover-letter', methods=['POST'], strict_slashes=False)
def generate_cover_letter():
    try:
        data = request.get_json()
        resume_text = data.get("resume_text")
        description = data.get("description")
        company = data.get("company")
        position =data.get("position")
        if not resume_text or not description:
            return jsonify({"error": "Both 'resume_text' and 'description' are required."}), 400

        prompt = (
            f"Using the provided company: {company}, position: {position}, job description: {description} and resume text: {resume_text}, "
            "craft a professional cover letter tailored to the role, ensuring it is within 200 words."
        )
        cover_letter = LlmService.get_llm_result(prompt=prompt)

        return jsonify({"cover_letter": cover_letter}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)