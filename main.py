import PyPDF2

from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def set_need_appearances_writer(writer: PdfFileWriter):
    # See 12.7.2 and 7.7.2 for more information: http://www.adobe.com/content/dam/acom/en/devnet/acrobat/pdfs/PDF32000_2008.pdf
    try:
        catalog = writer._root_object
        # get the AcroForm tree
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)
            })

        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        # del writer._root_object["/AcroForm"]['NeedAppearances']
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green buttopdfOutput)n in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    #
    # pdfObj = open("F:\\NameGender.pdf", 'rb')
    #
    # reader = PyPDF2.PdfFileReader(
    #     pdfObj,
    #     strict=True,
    #     warndest=None,
    #     overwriteWarnings=True
    #     )
    #
    # print(reader.getFormTextFields())
    #
    # # Print values from PDF file
    # print("Textbox value = {0}".format(reader.getFields()['txtName']['/V']))
    #
    # if reader.getFields()['Option Button 1']['/V'] == '/1':
    #     print("Gender = Male")
    # else:
    #     print("Gender = Female")
    #
    # print("Checkbox 1 value = {0}".format(reader.getFields()['chk1']['/V']))
    # print("Checkbox 2 value = {0}".format(reader.getFields()['chk2']['/V']))
    #
    # print("Gender = ")
    #
    # print(reader.getFields())





#
# Attempt write to PDF file
#

myfile = PdfFileReader("C:\\TEMP\\Biology Lab Form 01.pdf")
first_page = myfile.getPage(0)

writer = PdfFileWriter()
set_need_appearances_writer(writer)

data_dict = {
            'txtPIName': 'Annalisa Scimemi',
            'txtPIOffice': 'BIO 329'
            }

writer.updatePageFormFieldValues(first_page, fields=data_dict)
writer.addPage(first_page)

with open("c:\\temp\\newfile.pdf","wb") as new:
    writer.write(new)

#
# Attempt write to PDF file
#


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
