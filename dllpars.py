import pefile

dll = input("filename: ")

pe = pefile.PE(dll)

print("\n\n")
print(hex(pe.OPTIONAL_HEADER.ImageBase))
print("\n\n")
for i in pe.DIRECTORY_ENTRY_EXPORT.symbols:
    print (hex(i.address), " ", i.name,)

input()