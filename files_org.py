import os
from pathlib import Path

# create dictionary with folder names and respective file extensions
subdir = {
        "Docs":[".pdf",".docx",".txt"],
        "Audio":[".m4a",".m4b",".mp3"],
        "Images":[".jpg",".jpeg",".png",".jfif",".avif"],
        "Apps":[".exe",".msi"],
        "Compressed":[".zip",".rar"]
        }

# function to pick folder given file extension
def pickDir(ext):
    for folder, extension in subdir.items():
        for suffix in extension:
            if suffix == ext:
                return folder


# function that scans all files, check extension and move it to respective folder
def organizeDir(file_path):
    for item in os.scandir(file_path):
                
        # skip if it's directory
        if item.is_dir():
                continue
        
        # save file path
        filePath = Path(item)
        print(filePath)
        # save file extension
        fileType = filePath.suffix.lower()
        print(fileType)
        directory = pickDir(fileType)
        print(directory)
        
        # skip if file doesn't have extension
        if directory == None:
            continue
        
        directoryPath = Path(file_path)/directory
        print(directoryPath)
        # make new directory if not found
        if directoryPath.is_dir() != True:
                directoryPath.mkdir()
                print(directoryPath)
        # move file 
        newFilePath = directoryPath / filePath.name
        filePath.rename(newFilePath)

def start_organizing():
    file_path = input("Enter the path of the folder you want to organize: ")
    #file_path = "C:/Users/manuel/Downloads"
    print(file_path)
    organizeDir(file_path)

if __name__ == "__main__":
    start_organizing()