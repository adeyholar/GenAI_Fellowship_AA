import requests


def parse_network_log(log_line):
    """Parse a log line and return status if it contains a keyword."""
    keywords = ["ERROR", "WARNING", "CRITICAL"]
    for keyword in keywords:
        if keyword in log_line.upper():
            return f"Found {keyword}: {log_line.strip()}"
    return "No issues detected"

def check_device_status(url="https://api.ipify.org?format=json"):
    """Check device status via a sample API."""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f"Device active: {response.json()['ip']}"
        return "Device offline"
    except requests.RequestException as e:
        return f"Network error: {e}"
    
def count_log_issues(log_lines):
    """Count log lines with issues."""
    keywords = ["ERROR", "WARNING", "CRITICAL"]
    return sum(1 for line in log_lines if any(keyword in line.upper() for keyword in keywords))