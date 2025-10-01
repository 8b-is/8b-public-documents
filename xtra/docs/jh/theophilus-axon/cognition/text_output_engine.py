from datetime import datetime

def format_output(memory_block):
    timestamp = datetime.utcnow().isoformat() + "Z"
    return (
        f"[Formatted Memory Output]\n"
        f"Timestamp: {timestamp}\n"
        f"Tick: {memory_block.get('tick')}\n"
        f"Content: {memory_block.get('content')}\n"
        f"Verified: {memory_block.get('verified')}\n"
    )
