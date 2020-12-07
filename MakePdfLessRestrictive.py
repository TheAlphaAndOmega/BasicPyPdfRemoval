import argparse
import RemoveEncrypt

parser = argparse.ArgumentParser(description='Remove known password from PDF encrypted file and save a new file from' +
                                             ' decrypted PDF.')

parser.add_argument('-i', '--input_file_path', required=True, type=str,
                    help='The absolute file path of the existing PDF with a password')

parser.add_argument('-o', '--output_file_path', required=True, type=str,
                    help='The absolute file path to create a copy of the PDF to, which will not have a password')

parser.add_argument('-p', '--password', required=True, type=str,
                    help='The absolute file path for the PDF with a password')

args = parser.parse_args()

# print("Displaying input_file_path as: % s" % args.input_file_path)
# print("Displaying output_file_path as: % s" % args.output_file_path)
# print("Displaying password as: % s" % args.password)

print(RemoveEncrypt.remove_password_from_pdf(args.input_file_path, args.output_file_path, args.password))

