import requests

API_KEY = 'f7706f1c14f2420e8ea3ea564149d330'
PROJECT_ID = 'your_project_id_here'

def extract_submission_texts(submission_links):
    submission_texts = []
    
    for idx, link in enumerate(submission_links, start=1):
        url = f'https://autoextract.scrapinghub.com/v1/extract?project={PROJECT_ID}&url={link}&pageFunction=() => {{"submissionText": document.querySelector(".source-copier").innerText}}'
        headers = {'Authorization': f'Bearer {API_KEY}'}
        
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            submission_text = data['submissionText'].strip() if 'submissionText' in data else 'Not found'
            submission_texts.append(submission_text)
            
            # Store the extracted text in a file
            with open(f"code_{idx}.txt", "w") as file:
                file.write(submission_text)
                file.write("\n---Separator---\n")
        else:
            print(f"Failed to extract data from {link}. Status code: {response.status_code}")

    return submission_texts

def read_submission_links(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]

submission_links = read_submission_links("submission_links.txt")
submission_texts = extract_submission_texts(submission_links)

for idx, text in enumerate(submission_texts, start=1):
    print(f"Submission {idx}:\n{text}\n")
