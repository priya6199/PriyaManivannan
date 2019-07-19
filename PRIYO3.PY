M=str(input())
if (M=='a' or M=='A' or M=='e' or M=='E' or M=='i' or M=='I' or M=='o' or M=='O' or M=='u' or M=='U'):
    print('Vowel')
elif (M>='a' and M<='z') or (M>='A' and M<='Z'):
    print('Consonant')
else:
    print('invalid')
