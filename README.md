"#  Rohit"
"# django-cicd-configuration-files" 
# CSV File Analysis Project

This project allows users to upload CSV files and process them for data analysis. The project is built using Django and includes features for user authentication, file upload, and data analysis.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Session Management](#session-management)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- User authentication (signup, login, logout)
- ![image](https://github.com/user-attachments/assets/6b8f59a8-bdf7-4005-9046-154a83f2f07b)

- File upload and validation
- ![image](https://github.com/user-attachments/assets/0d59d2d3-4f3b-4c6a-b4ff-71be42443365)

- Data analysis on uploaded CSV files

- ![image](https://github.com/user-attachments/assets/a490e946-32e1-472c-8772-095c1aafa577)

- 
- Display results of data analysis


![image](https://github.com/user-attachments/assets/8bd2627e-63b1-4631-a81c-a08284a2e818)


![image](https://github.com/user-attachments/assets/308a7970-c6b1-49ef-a44a-d76340d8e1cc)


![image](https://github.com/user-attachments/assets/c8f5f722-70ce-4647-8d76-f8e4ad306e55)



## Requirements

- Python 3.12.4
- Django 5.0.7

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/1Rohitmahajan/csv_file_analysis_project.git
cd csv-file-analysis-project

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate


python manage.py createsuperuser

python manage.py runserver
