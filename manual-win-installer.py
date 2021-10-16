import zipfile
from tkinter import filedialog
import os
file_path = filedialog.askopenfilename()
program_path = os.path.basename(file_path).rsplit(".", 1 )[0]
path_for_program = r"C:\\ProgramFiles\\" + program_path
with zipfile.ZipFile(file_path, 'r') as zip_ref:
    zip_ref.extractall(path_for_program)
