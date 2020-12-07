# Basic PyPdf2 Removal Example

## Make a new project/folder with venv
I recommend using PyCharm but you could use the command line if you have no GUI programs...

Here are the sequences of commands from the terminal:

    C:
    
    python -m pip install virtualenv
    
    cd "C:\Users\123\Desktop"
    
    virtualenv MyNewFolderNameToBeCreated
    
    cd MyNewFolderNameToBeCreated
    
    Scripts\activate.bat

Now you should see a change in the folder name. It should look like this:
    
    (MyNewFolderNameToBeCreated) C:\Users\123\Desktop\MyNewFolderNameToBeCreated>

Now you need to copy 3 files to your folder. You can do this using folder explorer.

##Copy the python project files to your folder.

1) Copy file "requirements.txt" to new folder/project
2) Copy file "MakePdfLessRestrictive.py" to new folder/project
3) Copy file "RemoveEncrypt.py" to new folder/project


## Install python packages
Now go back to your venv terminal and execute the command:

    python -m pip install -r requirements.txt

... Then wait for completion of pip for PyPDF2 & pyinstaller...

## Give it a test
Execute this from the venv terminal: 

    python MakePdfLessRestrictive.py -i "C:\Users\123\Desktop\PdfWithPass.pdf" -o "C:\Users\123\Desktop\File_With_No_Pass.pdf" -p "password123"

## Make exe file
Execute this from the venv terminal: 

    pyinstaller MakePdfLessRestrictive.py --onefile

There should now be 2 new folders created under `MyNewFolderNameToBeCreated`, one called `build` and the other called `dist`. The folder `dist` contains the resulting .exe file (you can ignore other folders/files) which should be named `MakePdfLessRestrictive.exe`. The full file path would be `C:\Users\123\Desktop\MyNewFolderNameToBeCreated\dist\MakePdfLessRestrictive.exe`


## Run from command line to test the exe made by pyinstaller
    "C:\Users\123\Desktop\MakePdfLessRestrictive.exe" -i "C:\Users\123\Desktop\File_With_Pass.pdf" -o "C:\Users\123\Desktop\File_With_No_Pass.pdf" -p "file_password_plain_text"

## VBA Code
    Private Sub testShellExe()
        Call VBA.Shell("""C:\Users\123\Desktop\MakePdfLessRestrictive.exe"" -i ""C:\Users\123\Desktop\File_With_Pass.pdf"" -o ""C:\Users\123\Desktop\File_With_No_Pass.pdf"" -p ""password""")
    End Sub
