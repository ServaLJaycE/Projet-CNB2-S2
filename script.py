from openpyxl import load_workbook
 
#load excel file
workbook = load_workbook(filename="test.xlsx")
 
#open workbook
sheet = workbook.active
 
#modify the desired cell
sheet["A1"] = "Full Name"
 
#save the file
workbook.save(filename="test.xlsx")