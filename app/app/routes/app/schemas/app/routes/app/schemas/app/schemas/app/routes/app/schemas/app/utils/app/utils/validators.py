def validate_text(text: str) -> bool:
    return isinstance(text, str) and len(text) > 0
