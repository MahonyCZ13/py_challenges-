##############################
# Challenge 1
##############################

from string import ascii_letters

original = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
url = "map"
c1 = ''

for c in url:
    if c in ascii_letters:
        c1 = c1 + ascii_letters[(ascii_letters.index(c)+2)%len(ascii_letters)]
    else:
        c1+=c

print (c1)