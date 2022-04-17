N = int(input())
tree = {}
for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left,right]

def order1(root):
    if root != '.':
        print(root,end='')
        order1(tree[root][0])
        order1(tree[root][1])
def order2(root):
    if root != '.':
        order2(tree[root][0])
        print(root,end='')
        order2(tree[root][1])
def order3(root):
    if root != '.':
        order3(tree[root][0])
        order3(tree[root][1])
        print(root,end='')

order1('A')
print()
order2('A')
print()
order3('A')
