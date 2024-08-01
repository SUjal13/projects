import json
import re

def parse_resume(file_path):
    with open(file_path, 'r') as file:
        resume_text = file.read()

    # Example parsing logic
    resume_data = {
        "name": re.search(r"Name:\s*(.*)", resume_text).group(1).strip(),
        "email": re.search(r"Email:\s*(.*)", resume_text).group(1).strip(),
        "phone": re.search(r"Phone:\s*(.*)", resume_text).group(1).strip(),
        "education": re.search(r"Education:\s*(.*)", resume_text).group(1).strip(),
        "experience": re.search(r"Experience:\s*(.*)", resume_text).group(1).strip()
    }

    return resume_data

def main():
    # Use raw string for Windows path
    file_path = r'D:\Sem 6\Artificial Intelligence\Assignment\resume.txt'
    resume_data = parse_resume(file_path)
    
    with open(r'D:\Sem 6\Artificial Intelligence\Assignment\resume.json', 'w') as json_file:
        json.dump(resume_data, json_file, indent=4)

if __name__ == "__main__":
    main()
