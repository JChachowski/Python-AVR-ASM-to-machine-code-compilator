import sys
from antlr4 import *
from AVRLexer import AVRLexer
from AVRParser import AVRParser
from MyAVRVisitor import MyAVRVisitor
from intelhex import IntelHex
from label_collector import LabelCollector
from code_generator import CodeGenerator
from antlr4.error.ErrorListener import ErrorListener
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox, ttk
import sys

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax error at line {line}, column {column}: {msg}")
        raise Exception(f"Syntax error at line {line}, column {column}: {msg}")

#Intel HEX file generator
def write_hex_file(filename: str, machine_code: list[int]):
    ih = IntelHex()
    addr = 0
    for word in machine_code:
        try:
            ih.puts(addr, word.to_bytes(2, byteorder="little"))
            addr += 2
        except:
            # ih.puts(addr, word.to_bytes(4, byteorder="little"))
            # addr += 4
            word1 = int((word & 0b11111111111111110000000000000000) >> 16)
            word2 = int((word & 0b00000000000000001111111111111111))
            ih.puts(addr, word1.to_bytes(4, byteorder="little"))
            addr += 2
            ih.puts(addr, word2.to_bytes(4, byteorder="little"))
            addr += 2
    ih.write_hex_file(filename)

#raw binary file generator
def write_bin_file(filename: str, machine_code: list[int]):
    with open(filename, 'wb') as f:
        for word in machine_code:
            try:
                f.write(word.to_bytes(2, byteorder='little'))
            except:
                word1 = int((word & 0b11111111111111110000000000000000) >> 16)
                word2 = int((word & 0b00000000000000001111111111111111))
                f.write(word1.to_bytes(2, byteorder='little'))
                f.write(word2.to_bytes(2, byteorder='little'))
#type "hex" | "bin"
def assemble(input_code: str, filename: str, type: str):
    input_stream = InputStream(input_code.upper())

    lexer = AVRLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = AVRParser(stream)
    #error_parser = AVRParser(stream)
    #error_parser.removeErrorListeners()
    #error_parser.addErrorListener(MyErrorListener)
    #error_tree = error_parser.program()
    tree = parser.program()

    #collect labels 
    collector = LabelCollector()
    collector.visit(tree)

    #generate code
    generator = CodeGenerator(collector.labels)
    generator.visit(tree)
    machine_code = generator.get_flat_code()

    if(type == "hex"):
        filename = filename
        write_hex_file(filename, machine_code)
    elif(type == "bin"): 
        filename = filename
        write_bin_file(filename, machine_code)
    else: print("ERROR: file not saved, wrong type")
    return machine_code

#TODO input handling: add propper file input, sanitize it and add .upper()

# GUI definition
def run_gui():
    def select_input_file():
        file_path = filedialog.askopenfilename(filetypes=[("ASM files", "*.asm"), ("All files", "*.*")])
        if file_path:
            input_file_var.set(file_path)

    def select_output_dir():
        dir_path = filedialog.askdirectory()
        if dir_path:
            output_dir_var.set(dir_path)

    def run_assembler():
        input_path = input_file_var.get()
        output_dir = output_dir_var.get()
        filetype = file_type_var.get()

        if not os.path.isfile(input_path) or not os.path.isdir(output_dir):
            messagebox.showerror("Error", "Invalid input file or output directory.")
            return

        with open(input_path, "r", encoding="utf-8") as f:
            input_code = f.read()

        base_filename = os.path.splitext(os.path.basename(input_path))[0]
        out_filename = os.path.join(output_dir, base_filename + (".hex" if filetype == "hex" else ".bin"))

        try:
            assemble(input_code, out_filename, filetype)
        except Exception as e:
            messagebox.showerror("Assembling Error", str(e))
            return

        output_text.delete(1.0, tk.END)
        with open(out_filename, "rb" if filetype == "bin" else "r") as f:
            content = f.read()
            if isinstance(content, bytes):
                content = ' '.join(f'{b:02X}' for b in content)
            output_text.insert(tk.END, content)

    root = tk.Tk()
    root.title("AVR Assembler GUI")

    input_file_var = tk.StringVar()
    output_dir_var = tk.StringVar()
    file_type_var = tk.StringVar(value="hex")

    tk.Label(root, text="Input File:").grid(row=0, column=0, sticky="w")
    tk.Entry(root, textvariable=input_file_var, width=50).grid(row=0, column=1)
    tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2)

    tk.Label(root, text="Output Directory:").grid(row=1, column=0, sticky="w")
    tk.Entry(root, textvariable=output_dir_var, width=50).grid(row=1, column=1)
    tk.Button(root, text="Browse", command=select_output_dir).grid(row=1, column=2)

    tk.Label(root, text="Output Format:").grid(row=2, column=0, sticky="w")
    ttk.Combobox(root, textvariable=file_type_var, values=["hex", "bin"], width=10).grid(row=2, column=1, sticky="w")

    tk.Button(root, text="Assemble", command=run_assembler).grid(row=3, column=0, columnspan=3, pady=10)

    tk.Label(root, text="Output File Content:").grid(row=4, column=0, columnspan=3, sticky="w")
    output_text = scrolledtext.ScrolledText(root, width=80, height=20)
    output_text.grid(row=5, column=0, columnspan=3)

    root.mainloop()



if( len(sys.argv)>2):
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    print(input_filename[-4:])
    print(output_filename[-4:] == ".hex")
    if(input_filename[-4:] != ".asm"): 
        print("ERROR: input filename extension incorrect")
        exit()
    if(output_filename[-4:] not in [".hex", ".bin"]): 
        print("ERROR: output filename extension incorrect")
        exit()
    output_type = output_filename[-3:]

    with open(input_filename, "r", encoding="utf-8") as file:
        input_code = file.read()

    assembled_code = assemble(input_code, "out.hex",output_type)
else:
    run_gui()