#  Read a text file line by line and print only lines that contain the word “Python”

with open("day_15_reading_txt_files\Main.txt", "r") as file:
    for line in file:
        # Converts the line to lowercase to catch "python", "Python", or "PYTHON"
        if "python" in line.lower():
            print(line.strip())
