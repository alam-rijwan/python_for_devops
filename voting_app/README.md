# 🗳️ Voting App (Flask Web Application)

A simple web-based Voting Application built using **Python Flask**.  
This project demonstrates basic backend development, template rendering, and static file handling using Flask.

---

## 📌 Project Overview

The Voting App allows users to vote through a web interface.  
It is built to understand:

- Flask application structure
- Template rendering using Jinja2
- Static file management (CSS)
- Virtual environment usage
- Basic DevOps project structure

---

## 🏗️ Project Structure

VOTING_APP/
│
├── app.py # Main Flask application
├── requirements.txt # Project dependencies (optional but recommended)
├── README.md # Project documentation
│
├── templates/ # HTML templates
│ └── index.html
│
├── static/ # Static files 
│ └── style.css
│
└── venv/ # Virtual environment (not pushed to GitHub)


---

## ⚙️ Technologies Used

- Python 3.x
- Flask
- HTML5
- CSS3

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd VOTING_APP

 python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

App will run on:

http://127.0.0.1:5000/

