from pathlib import Path
from pypdf import PdfReader

def read_pdf_text(pdf_path: Path) -> str:
    text = []
    reader = PdfReader(str(pdf_path))
    for p in reader.pages:
        t = p.extract_text() or ""
        if t: text.append(t)
    return "\n".join(text)

def read_text_file(path: Path, encoding="utf-8") -> str:
    return path.read_text(encoding=encoding)

def build_system_prompt(name: str, summary: str, cv: str) -> str:
    base = (
        f"You are acting as {name}. You are answering questions on {name}'s website, "
        f"particularly questions related to {name}'s career, background, skills and experience. "
        f"Be professional and engaging; if you don't know the answer, say you will follow up via email "
        f"and ask for contact details (email) to continue the conversation.\n\n"
        f"## Summary:\n{summary}\n\n## CV Profile:\n{cv}\n\n"
        f"Always stay in character as {name}."
    )
    return base
