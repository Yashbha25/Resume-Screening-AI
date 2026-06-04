import spacy
import pdfplumber
import docx
from cryptography.fernet import Fernet

nlp = spacy.load("en_core_web_sm")


def extract_text_from_pdf(pdf_file):
    """Extract text from a PDF file using pdfplumber."""
    with pdfplumber.open(pdf_file) as pdf:
        return "".join(
            [page.extract_text() for page in pdf.pages if page.extract_text()]
        )


def extract_text_from_docx(docx_file):
    """Extract text from a DOCX file."""
    doc = docx.Document(docx_file)
    return " ".join([para.text for para in doc.paragraphs])


def preprocess_text(text):
    """Lemmatize and clean text using spaCy."""
    doc = nlp(text)
    tokens = [
        token.lemma_.lower()
        for token in doc
        if not token.is_stop and token.is_alpha
    ]
    return " ".join(tokens)


def extract_candidate_details(text):
    """Extract named entities from resume text."""
    doc = nlp(text)
    entities = {"Name": [], "Education": [], "Skills": [], "Experience": []}
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["Name"].append(ent.text)
        elif ent.label_ in ["ORG", "EDUCATION"]:
            entities["Education"].append(ent.text)
        elif ent.label_ in ["SKILL", "ABILITY"]:
            entities["Skills"].append(ent.text)
        elif ent.label_ in ["DATE", "TIME"]:
            entities["Experience"].append(ent.text)
    return entities


def generate_encryption_key():
    """Generate a Fernet encryption key."""
    return Fernet.generate_key()


def encrypt_text(text, key):
    """Encrypt text using Fernet symmetric encryption."""
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())


def decrypt_text(token, key):
    """Decrypt a Fernet-encrypted token."""
    cipher = Fernet(key)
    return cipher.decrypt(token).decode()
