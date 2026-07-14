import uuid
from datetime import datetime

def generate_uuid() -> str:
    return str(uuid.uuid4())

def format_timestamp(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def calculate_file_size(size_in_bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_in_bytes < 1024.0:
            return f"{size_in_bytes:.2f} {unit}"
        size_in_bytes /= 1024.0
    return f"{size_in_bytes:.2f} TB"