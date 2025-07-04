import sys

def preorder(node, tree):
    if node == '.':
        return
    print(node, end='')
    preorder(tree[node][0], tree)
    preorder(tree[node][1], tree)

def inorder(node, tree):
    if node == '.':
        return
    inorder(tree[node][0], tree)
    print(node, end='')
    inorder(tree[node][1], tree)

def postorder(node, tree):
    if node == '.':
        return
    postorder(tree[node][0], tree)
    postorder(tree[node][1], tree)
    print(node, end='')

def main():
    input = sys.stdin.readline
    n = int(input())

    tree = {}

    for _ in range(n):
        root, left, right = input().split()
        tree[root] = (left, right)

    preorder('A', tree)
    print()
    inorder('A', tree)
    print()
    postorder('A', tree)
    print()

if __name__ == "__main__":
    main()
