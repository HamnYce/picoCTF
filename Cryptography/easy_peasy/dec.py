# for o in range(ord('0'), ord('9') + 1):
#     print('\x00' * 49_968)
#     print(f'{chr(o)}' * 32)
# print('\n')
with open('finalres') as f:
    s = list(map(lambda x: x.strip(), f.readlines()))
CAPS = [chr(o) for o in range(65, 65+26)]
LOWER = [chr(o) for o in range(97, 97+26)]
NUMS = [chr(o) for o in range(ord('0'), ord('9') + 1)]

flag = open('flag').read().strip()
blag = bytes.fromhex(flag)
# print(blag)
a = [None] * 32

for i in range(len(s)):
    line = s[i]
    bine = bytes.fromhex(line)
    # print(bine)
    if 0 <= i < 26:
        current_char = chr(65 + i)
    elif 26 <= i < 26+26:
        current_char = chr(97 + i - 26)
    else:
        current_char = chr(i + ord('0') - 52)
    for j in range(len(bine)):
        if (bine[j] == blag[j]):
            print(f'pos:{j},char:{current_char}')
            a[j] = current_char
print(''.join(a))
# print(current_char)
