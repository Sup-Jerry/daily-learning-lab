from pathlib import Path

# 创建一个示例文件，确保脚本可以独立运行
sample_path = Path(__file__).with_name("sample_note.txt")
sample_path.write_text("Python\nGit\nFrontend\n", encoding="utf-8")

print("Reading file:", sample_path.name)
line_count = 0

with sample_path.open("r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        cleaned = line.strip()
        print(f"Line {line_number}: {cleaned}")
        line_count += 1

print("Total lines:", line_count)
