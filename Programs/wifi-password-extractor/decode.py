utf = "b'\xff\xfeE\x00n\x00c\x00o\x00d\x00i\x00n\x00g\x00'"
decode = utf.encode("utf-16").decode("utf-16")
print(decode)

'''f = open('Prajol.txt',"r")
decode = f.decode(encoding = 'utf-16')
#encode = text.encode(encoding = 'utf-16')
f.write(str(decode))
#f.encode(encoding = 'utf-16')
f.close()'''