def clean_text(text):
    """Basic text cleaning for headings"""
    text = text.strip()
    # Remove excessive whitespace
    text = ' '.join(text.split())
    # Remove common trailing punctuation
    text = text.rstrip('.:,-')
    return text