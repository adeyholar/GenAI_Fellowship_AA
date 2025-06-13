def read_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return ["Error: Log file not found!"]
    except Exception as e:
        return [f"Error: {str(e)}"]

def write_summary(file_path, lines):
    try:
        with open(file_path, 'w') as file:
            file.write("Network Log Summary\n")
            issues = [line for line in lines if any(kw in line.upper() for kw in ["ERROR", "WARNING", "CRITICAL"])]
            file.write(f"Total Issues: {len(issues)}\n")
            for issue in issues:
                file.write(f"- {issue}\n")
        return "Summary written successfully"
    except Exception as e:
        return f"Error writing summary: {str(e)}"

def append_log(file_path, new_entry):
    try:
        with open(file_path, 'a') as file:
            file.write(f"{new_entry}\n")
        return "Log appended successfully"
    except Exception as e:
        return f"Error appending log: {str(e)}"