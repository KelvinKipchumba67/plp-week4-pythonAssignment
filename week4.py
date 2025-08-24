with open("file.txt", "r", encoding="utf-8",  errors="ignore") as file:
    text=file.read()
    print(text)
upper=text.upper()
with open ("output.txt", "w", encoding="utf-8", errors="ignore" ) as new_file:
    new_file.write(upper)
   

while True:
    filename=input("\n Enter the file name: ")

    try: 
        with open (filename, "r", encoding="utf-8", errors="ignore") as recent_file:
            content=recent_file.read()
            print("\nFile opened successfully")
            print(content)
            break
    except FileNotFoundError:
        print("Sorry file cannot be found, Check the file name and try again !!")
