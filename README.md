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

<<<<<<< HEAD
### 📍 Local Execution
1. Place PDF files inside the `input/` directory
2. Run the extractor
```bash
py main.py
```
3. Output JSON files will be created in the `output/` folder
=======
### Local Execution

1. Place PDF files in the input/ folder  
2. Run the extractor:

```bash
python main.py
```


3. Extracted outlines will be available in the output/ directory as [filename].json
>>>>>>> 79bc0104fb2145c36fe7becc2b59cf27597f4ec3

### 🐳 Docker Execution

#### Step 1: Build the Docker Image
```bash
docker build -t pdf-outliner .
```

<<<<<<< HEAD
#### Step 2: Run the Container 
=======
```bash
docker build --platform linux/amd64 -t pdf-outliner .
```
>>>>>>> 79bc0104fb2145c36fe7becc2b59cf27597f4ec3

For Linux/macOS:  

<<<<<<< HEAD
=======
#### Process documents:

>>>>>>> 79bc0104fb2145c36fe7becc2b59cf27597f4ec3
```bash
docker run --rm \
  -v "$(pwd)/input:/app/input" \
  -v "$(pwd)/output:/app/output" \
  --network none \
  pdf-outliner
```

For Windows PowerShell:
```bash
docker run --rm `
  -v "${PWD}/input:/app/input" `
  -v "${PWD}/output:/app/output" `
  --network none `
  pdf-outliner
```

For Windows CMD:
```bash
docker run --rm ^
  -v "%CD%/input:/app/input" ^
  -v "%CD%/output:/app/output" ^
  --network none ^
  pdf-outliner
```

## 📂 Project Structure
<<<<<<< HEAD
```
=======

```bash
>>>>>>> 79bc0104fb2145c36fe7becc2b59cf27597f4ec3
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
└── requirements.txt     # Python dependencies

```

```

## 📸 Screenshots

### ✅ Sample Output
![JSON Output](screenshots/json_output.png)

### ⚙ Docker Execution
![Docker Run](screenshots/docker_run.png)

---

## 👨‍💻 Team - ZenCode

- **Roushani Kumari** – [GitHub](https://github.com/Roushani06)
- **Snigdha Kumar** – [GitHub](https://github.com/snigdhaydv27)

> ✨ Built with passion for Adobe Hackathon
