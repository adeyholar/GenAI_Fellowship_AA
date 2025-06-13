def read_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            return [line.strip() for line in lines]
    except FileNotFoundError:
        return ["Error: Log file not found!"]
    except Exception as e:
        return [f"Error: {str(e)}"]

log_file = "network.log"
log_lines = read_log(log_file)
print("Log Contents:")
for line in log_lines:
    print(line)