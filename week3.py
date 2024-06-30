#hihi and crazy bits
l=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
for i in l:
    if i%2==0:
        print(i+1)
    else:
        print(i-1)


def toggle(n,l,r):
    # First, create a mask with all 1s from bit position 0 to r (inclusive)
    # Then, create another mask with all 1s from bit position 0 to (l-1) (inclusive)
    # Finally, XOR these two masks to get the desired 'num'
    num = ((1 << r) - 1) ^ ((1 << (l - 1)) - 1)
    # Toggle the bits in 'n' using 'num'
    return n^num


n,l,r=map(int,input().split(' '))
print("After toggling:",toggle(n,l,r))