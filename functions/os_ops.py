import os 
import subprocess as sp

"""This file contains functions to interact with the OS on the users system"""

paths = {
    'notepad' : "C:\\WINDOWS\\system32\\notepad.exe",
    'discord' : "C:\\Users\\user\\AppData\\Local\\Discord\\Update.exe",
    'slack' : "C:\\Users\\user\\AppData\\Local\\slack\\slack.exe",
    'microsoft_word' : "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    'excel' : "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    'calculator' : "C:\\Windows\\System32\\calc.exe",
    'code' : "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
}

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])

def  open_discord():
    os.startfile(paths['discord'])

def open_microsoft_word():
    os.startfile(paths['microsoft_word'])

def open_excel():
    os.startfile(paths['excel'])

def open_slack():
    os.startfile(paths['slack'])

def open_calculator():
    sp.Popen(paths['calculator'])

def open_cmd():
    os.system('start cmd')




