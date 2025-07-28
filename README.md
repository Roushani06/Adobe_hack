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

## 🏃‍♂ Usage

### 📍 Local Execution
1. Place PDF files inside the `input/` directory
2. Run the extractor
```bash
py main.py 
```
or  
```bash
python main.py 
```

3. Output JSON files will be created in the `output/` folder

### 🐳 Docker Execution

#### Step 1: Build the Docker Image
```bash
docker build -t pdf-outliner .
```

#### Step 2: Run the Container 

For Linux/macOS:  

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
```
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

## 👨‍💻 Team - ZenCode

- **Roushani Kumari** – [GitHub](https://github.com/Roushani06)
- **Snigdha Kumar** – [GitHub](https://github.com/snigdhaydv27)

> ✨ Built with passion for Adobe Hackathon
