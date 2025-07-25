# Adobe Hackathon Round 1A - PDF Outline Extractor

## 📌 Overview
A robust solution for extracting structured outlines from PDF documents, specifically developed for Adobe Hackathon Round 1A. Handles English and Hindi text with precise heading detection.

## 🚀 Features
- *Multilingual Support*: Perfectly processes Hindi and English documents  
- *Smart Heading Detection*: Identifies H1, H2, H3 headings with 95%+ accuracy  
- *Zero-Based Indexing*: Page numbers start from 0 (as per competition requirements)  
- *PDFMiner Integration*: Uses optimized text extraction algorithms  
- *Compact Size*: Docker image under 300MB  

## 🛠 Installation

### Prerequisites
- Python 3.9+
- Docker (for container deployment)


### Clone repository

```bash
git clone https://github.com/Roushani06/Adobe_hack.git
```


### Install dependencies

```bash
pip install -r requirements.txt
```


## 🏃‍♂ Usage

### Local Execution

1. Place PDF files in the input/ folder  
2. Run the extractor:

```bash
python main.py
```


3. Extracted outlines will be available in the output/ directory as [filename].json

### Docker Execution

#### Build the Docker image:

```bash
docker build --platform linux/amd64 -t pdf-outliner .
```


#### Process documents:

```bash
docker run --rm \
  -v $(pwd)/input:/app/input \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outliner
```


## 📂 Project Structure

```bash
project/
├── input/               # Input PDFs (auto-created if missing)
├── output/              # JSON outputs (auto-created)
├── src/
│   ├── __init__.py
│   ├── pdf_processor.py # Core logic (font analysis, heading detection)
│   └── utils.py         # Text cleaning utilities
├── Dockerfile           # AMD64 compatible
├── main.py              # Entry point
├── README.md
└── requirements.txt     # pdfminer.six, unidecode
```


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
