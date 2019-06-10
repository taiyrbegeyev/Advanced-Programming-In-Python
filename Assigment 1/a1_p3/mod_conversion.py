#JTSK-350112
# mod_conversion.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de

"""
        Mod Conversion module
        The module prints the conversion table
"""

def in2cm_table(start_length, end_length, step_size):
    print("{0:>8} {1:>8}".format("inch", "cm"))
    for i in range(start_length, end_length, step_size):
        print("{0:>8.1f} {1:>8.1f}".format(i, i * 2.54))

def in2cm_table_html(start_length, end_length, step_size):
    #generate HTML code
    strTable = '<html>\n<head>\n<title>Conversion Table</title>\n\
    <style type="text/css">\n\
    #center{ display: flex; justify-content: center; align-items: center; }\n\
    .myTable{text-align:center;background-color:#eee;border-collapse:collapse;}\n\
    .myTable th { background-color:#000;color:white;width:50%; }\n\
    .myTable td, .myTable th { padding:20px;border:1px solid #000; }\n\
    </style></head>\n\
    <body>\n<div id = "center">\n<table class = "myTable">\n\
    <tr>\n<th>inch</th><th>cm</th>\n</tr>\n'

    for i in range(start_length, end_length, step_size):
        strTable += '<tr><td>' + str(i) + '</td>\n' + \
                '<td>' + str(i * 2.54) + '</td></tr>\n'

    strTable += '</table>\n</div></body>\n</html>'

    # open the file
    file = open("in2cmtable.html", "w")
    # write into the file
    file.write(strTable)
    #close the file
    file.close()