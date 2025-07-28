# Adobe Hackathon Round 1A - PDF Outline Extractor

## 📌 Overview
A robust solution for extracting structured outlines from PDF documents, specifically developed for Adobe Hackathon Round 1A. Handles English and Hindi text with precise heading detection.

## 🚀 Features
- 🗂 **Multilingual Support**: Accurately handles Hindi and English content
- 🔍 **Smart Heading Detection**: Identifies H1, H2, H3, H4 headings with high precision
- 📄 **Page-Aware**: Includes correct 1-based page numbers for each heading
- 🧠 **Font-Based Analysis**: Font size and style analysis to infer heading levels
- 📦 **Docker-Ready**: Compatible with `linux/amd64` and runs fully offline

## 🛠 Installation

### Prerequisites
- Python 3.9+
- Docker (for container deployment)

### Clone the Repository
```bash
git clone https://github.com/Roushani06/Adobe_hack.git
cd Adobe_hack
```

### Install Dependencies (for local run)
```bash
pip install -r requirements.txt
```

> ✅ Make sure you have `PyMuPDF==1.23.7` or compatible for PDF processing

## 📄 Requirements

### requirements.txt
```
PyMuPDF==1.23.7
```

## 🏃‍♂ Usage

### Local Execution

1. Place PDF files in the input/ folder  
2. Run the extractor:

bash
python main.py


3. Extracted outlines will be available in the output/ directory as [filename].json

### 🐳 Docker Execution

#### Build the Docker image:

bash
docker build --platform linux/amd64 -t pdf-outliner .


#### Process documents:

bash
docker run --rm \
  -v "$(pwd)/input:/app/input" \
  -v "$(pwd)/output:/app/output" \
  --network none \
  pdf-outliner


## 📂 Project Structure


project/
├── input/               # Input PDFs (auto-created if missing)
├── output/              # Output JSONs (auto-created)
├── src/
│   ├── __init__.py
│   ├── pdf_processor.py # Font and span analysis logic
│   └── utils.py         # Utility functions (e.g., text cleaning)
├── Dockerfile           # Docker setup
├── main.py              # Entry point
├── README.md
└── requirements.txt     # pdfminer.six, unidecode

---

## 📸 Screenshots

### Processing Flow
![Processing Flow](screenshots/processing_flow.png)
PDF processing workflow showing input → processing → output

### Sample Output
![JSON Output](screenshots/json_output.png)
Example of extracted outline in JSON format

### Docker Execution
![Docker Execution](screenshots/docker_run.png)
Running the processor in Docker container

---

## 👨‍💻 Team - ZenCode

Roushani Kumari – [GitHub](https://github.com/Roushani06)
Snigdha Kumar – [GitHub](https://github.com/snigdhaydv27)
