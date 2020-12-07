import PyPDF2

def remove_password_from_pdf(input_file_path: str, output_file_path: str, password: str) -> str:
    """
    Opens the PDF file, from the input_file_path, and decrypts (applies password) to the PDF. The contents are copied
     to the output_file_path.

    :param input_file_path: Absolute file path of PDF file with password.
    :param output_file_path: Absolute file path of file to save a copy of the PDF WITHOUT the password.
    :param password: The plain-text password to decrypt the PDF.
    :return: Returns the file path of the output_file_path param if successful.
    """
    # Create a PdfFileWriter object
    out = PyPDF2.PdfFileWriter()

    # Open encrypted PDF file with the PdfFileReader
    file = PyPDF2.PdfFileReader(input_file_path)

    # Check if the opened file is actually Encrypted
    if file.isEncrypted:

        # If encrypted, decrypt it with the password
        file.decrypt(password)

        # Now, the file has been unlocked.
        # Iterate through every page of the file
        # and add it to our new file.
        for idx in range(file.numPages):
            # Get the page at index idx
            page = file.getPage(idx)

            # Add it to the output file
            out.addPage(page)

        # Open a new file
        with open(output_file_path, "wb") as f:

            # Write our decrypted PDF to this file
            out.write(f)

            # Print success message when Done
            return output_file_path
