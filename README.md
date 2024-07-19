# Comstomized resume generator

## Overview
The Resume Updater is designed to assist job seekers by automating the customization of resumes for specific job descriptions using OpenAI's GPT-4. This tool aims to save time and reduce the emotional energy often expended in the overwhelming task of tailoring resumes manually. By providing an AI-driven, precise update to resumes based on a list of job descriptions, it allows job seekers to present themselves optimally for various roles efficiently.

## Objective
The primary objective of this project is to enhance the job application process by:
- **Automating Resume Customization**: Automatically updating resumes to highlight the skills and experiences that are most relevant to each job description.
- **Saving Time and Effort**: Reducing the time and effort job seekers spend on customizing their resumes for different applications.
- **Reducing Emotional Stress**: Helping job seekers manage the often overwhelming task of job application preparation, thereby conserving their emotional energy.

## Features
- **DOCX File Reading**: Extracts content from DOCX formatted resumes.
- **AI-Powered Updates**: Utilizes OpenAI's GPT-4 to tailor resumes according to the provided job descriptions.
- **Text File Output**: Outputs the updated resumes into text files.
- **MongoDB Integration**: Stores job descriptions and updated resumes in a MongoDB database.

## Prerequisites
Before you can run this project, you'll need to install the following:
- Python 3.8 or higher
- `openai` Python package
- `python-dotenv` package for environment variable management
- `pymongo` package for interacting with MongoDB
- `python-docx` package for reading DOCX files

## Setup
1. **Clone the repository**:
