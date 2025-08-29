
file_path = "wifi_paragraph.txt"

try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if "Wi-Fi" in line:
                print(line.strip())
except FileNotFoundError:
    print(f"Error: The file '{file_path}' does not exist.")
