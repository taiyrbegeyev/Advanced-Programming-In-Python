#JTSK-350112
# mod_conversion.py
# Taiyr Begeyev
# t.begeyev@jacobs-university.de
def in2cm_table(start_length, end_length, step_size):
    print("{0:>8} {1:>8}".format("inch", "cm"))
    for i in range(start_length, end_length, step_size):
        print("{0:>8.1f} {1:>8.1f}".format(i, i * 2.54))