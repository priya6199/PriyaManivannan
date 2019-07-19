R=str(input())
if (R=='a' or R=='A' or R=='e' or R=='E' or R=='i' or R=='I' or R=='o' or R=='O' or R=='u' or R=='U'):
    print('Vowel')
elif (R>='a' and R<='z') or (R>='A' and R<='Z'):
    print('Consonant')
else:
    print('invalid')
