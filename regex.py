import re

""""
str1 = "tataismyfavoritebrand" \
      "tatatomorrowismyendtatsemexam@123abcd"

str2 = "anirudha@gmail.com" \
       "aditi@gmail.com"

p = re.compile(r'@gmail.com')
c = p.finditer(str2)
for i in c:
    print(i.string)
    
"""

# pattern = re.compile(r'tata*')
#
# mat = pattern.finditer(str1)
# for m in mat:
#     # print(m)

# mystr = "abhdljskja"
# a = re.compile(r'\A')
# first = a.finditer(mystr)
# for f in first:
#     print(f)

'''
text_to_search = "
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

sentence = "Start a sentence and then bring it to an end"

pattern = re.compile(r'.')
matches = re.finditer(sentence)

for match in matches:
    print(match)