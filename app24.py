from openai import OpenAI
from dotenv import load_dotenv
import os
import docx
from pymongo import MongoClient

# Load environment variables
load_dotenv()

# Get API Key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize the OpenAI client with your API key
client = OpenAI(api_key=OPENAI_API_KEY)

# MongoDB connection setup
mongo_client = MongoClient(os.getenv("mongodb://localhost:27017/"))
db = mongo_client['resume_database']
collection = db['updated_resumes']

# Function to read a DOCX file and return its content
def read_docx(filepath):
    doc = docx.Document(filepath)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

resume_text = read_docx("./SM_DataScientist.docx")

# Define a job description
job_descriptions = ["""""",]


# Function to update resume based on job description
def update_resume(resume_text, job_description_text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Update the following resume to better match the job description provided."},
            {"role": "user", "content": resume_text},
            {"role": "system", "content": "Job description:"},
            {"role": "user", "content": job_description_text},
            {"role": "system", "content": "Please rewrite the resume emphasizing the skills and experiences that are most relevant to the job description, and quantize the achievements."}
        ]
    )
    if response.choices:
        return response.choices[0].message.content
    return "No response generated."


for idx, job_description in enumerate(job_descriptions):
    updated_resume = update_resume(resume_text, job_description)
    #collection.insert_one({"job_description": job_description, "updated_resume": updated_resume})

    # Write to a text file
    with open(f"updated_resume_{idx+1}.txt", "w") as file:
        file.write(f"Job Description: {idx+1}\n\nUpdated Resume:\n{updated_resume}")

print("All updated resumes have been stored in MongoDB and written to text files.")



