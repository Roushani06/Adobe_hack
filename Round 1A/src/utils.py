import re

def clean_text(text):
    """Enhanced text cleaning for document processing"""
    text = text.strip()
    # Remove excessive whitespace
    text = ' '.join(text.split())
    # Remove common trailing punctuation
    text = text.rstrip('.:,-')
    return text

def extract_keywords(text):
    """Extract important keywords from text"""
    # Remove common stop words and punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    words = text.split()
    # Filter out common words and short terms
    return [w for w in words if len(w) > 2]