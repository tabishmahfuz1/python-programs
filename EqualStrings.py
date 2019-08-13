from sys import stdin, stdout
T = int(stdin.readline())
for i in range(T):
    strs = stdin.readline().strip('\n').split(' ')
    charsA = dict()
    charsB = dict()
    for c in strs[0]:
        charsA[c] = (charsA.get(c) or 0) + 1
    for c in strs[1]:
        charsB[c] = (charsB.get(c) or 0) + 1
	print('charsA', charsA)
	print('charsB', charsB)
    flag="YES\n"
    if (len(charsA) != len(charsB)):
        flag="NO\n"
    else:
        for c in charsA:
            if c not in charsB:
                flag="NO\n"
                break
            if (charsA[c] != charsB[c]):
                flag="NO\n"
                break
    stdout.write(flag)