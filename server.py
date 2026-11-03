from mcp.server.fastmcp import FastMCP
import json
from datetime import datetime
import re

# Initialize MCP server
mcp = FastMCP("SecurityGatewayTestServer")

def write_audit_log(tool_name: str, arguments: dict, status: str):
    """Appends security inspection results to the audit log."""
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "tool_name": tool_name,
        "arguments": arguments,
        "status": status
    }
    with open("audit_log.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")

@mcp.tool()
def calculate_sum(a: int, b: int) -> int:
    """Adds two numbers together."""
    res = a + b
    write_audit_log("calculate_sum", {"a": a, "b": b}, "ALLOWED")
    return res

@mcp.tool()
def read_secret_file(file_path: str) -> str:
    """Attempts to read a sensitive file (For attack simulation)."""
    
    # --- REGEX SECURITY CHECK ---
    # If the requested file path contains 'password' or 'secret', block it immediately!
    if re.search(r"password|secret", file_path, re.IGNORECASE):
        print(f"[SECURITY ALERT] Blocked malicious attempt for file: {file_path}")
        write_audit_log("read_secret_file", {"file_path": file_path}, "BLOCKED")
        return "Access Denied: Security Policy Violation Detected by Gateway."

    res = f"Simulated secret content: {file_path} file read successfully."
    write_audit_log("read_secret_file", {"file_path": file_path}, "ALLOWED")
    return res

if __name__ == "__main__":
    mcp.run()