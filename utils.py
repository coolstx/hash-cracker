import hashlib

def hash_text(text, algo):
    """Hashes the given text using the specified algorithm."""
    text_bytes = text.encode('utf-8')
    
    try:
        if algo == "md5":
            return hashlib.md5(text_bytes).hexdigest()
        elif algo == "sha1":
            return hashlib.sha1(text_bytes).hexdigest()
        elif algo == "sha256":
            return hashlib.sha256(text_bytes).hexdigest()
        elif algo == "sha512":
            return hashlib.sha512(text_bytes).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {algo}")
    except Exception as e:
        return None
