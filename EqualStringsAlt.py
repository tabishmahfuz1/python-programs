from sys import stdin, stdout
T = int(stdin.readline())
for i in range(T):
    strs = stdin.readline().strip().split(' ')
    if(sorted(strs[0]) == sorted(strs[1])):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")