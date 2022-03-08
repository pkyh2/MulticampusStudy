def makeTree(tree, node):
    if tree:
        if tree[0] == 'L':
            node[1] = sum(node)
        elif tree[0] == 'R':
            node[0] = sum(node)
        return makeTree(tree[1:], node)
    else:
        return node


T = int(input())

for t in range(T):
    tree = input()
    rootnode = [1, 1]
    result = makeTree(tree, rootnode)
    print('#{} {}'.format(t+1, ' '.join(map(str, result))))