def detect_hash(h):
    """
    Attempts to detect the hashing algorithm based on the hash length.
    Returns the algorithm name or None if unknown.
    """
    h = h.strip()
    length = len(h)
    
    if length == 32:
        return "md5"
    elif length == 40:
        return "sha1"
    elif length == 64:
        return "sha256"
    elif length == 128:
        return "sha512"
    return None
