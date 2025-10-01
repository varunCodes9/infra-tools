def parse_logs(file_path):
    error_count = 0
    warning_count = 0
    info_count = 0
    try:
        with open(file_path, "r") as f:
            for lines in f:
                if "ERROR" in lines:
                    error_count += 1
                elif "WARNING" in lines:  # Aligned with 'if'
                    warning_count += 1
                if "INFO" in lines:
                    info_count += 1
        print(f"[LOG PARSER] ERROR count = {error_count}")
        print(f"Total WARNING lines: {warning_count}")
        print(f"Total INFO lines: {info_count}")

    except FileNotFoundError:
        print(f"File {file_path} not found!")


if __name__ == "__main__":
    parse_logs("error.log")
