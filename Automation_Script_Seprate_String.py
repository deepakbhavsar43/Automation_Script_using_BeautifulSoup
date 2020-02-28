in_tag = ['XYZ', 'CREF', 'BREF', 'RREF', 'REF']

in_string = 'XYZ:MUMBAI UNIVERSITYCREF:PUNE UNIVERSITYBREF:DADAR UNIVERSITYRREF:KOLHAPUR UNIVERCITY LLCREF:SOLAPUR UNIVERSITY'
result = "|"
for i in in_tag:
    print(i)
    temp = in_string.replace(i, "|" + i)
    print("temp",temp)
    temp = None
result += temp
print(result)