import os

for file_tex in os.listdir("latest_plot/"):

    if ".tex" not in file_tex:
        continue

    if "clean" in file_tex:
        continue

    file_open = open("latest_plot/" + file_tex, "r")
    lines_tex = file_open.readlines()
    file_open.close()

    clean_lines = ""
    for line_tex in lines_tex:
        if "&" in line_tex and "mathbf" not in line_tex and "Model" not in line_tex:
            continue
        clean_lines += line_tex
    
    file_open = open("latest_plot/" + file_tex.replace(".tex", "_clean.tex"), "w")
    file_open.write(clean_lines)
    file_open.close()