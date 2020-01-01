from collections import Counter


class MyNode:
    def __init__(self, value=None, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value

    def __str__(self):
        if self.left:
            s = '({})-'.format(self.left.value)
        else:
            s = '(None)-'
        if self.value:
            s = s + '({})'.format(self.value)
        else:
            s = s + '(None)'
        if self.right:
            s = s + '-({})'.format(self.right.value)
        else:
            s = s + '-(None)'
        return s
        

def print_counter(counter):
    s = "{"
    for k, v in counter.items():
        s = s + "{}: {}".format(k, v) + '  '
    s = s + '}'
    print(s)
    
    
def get_codes(node: MyNode, path=''):
    if node.value:
        print(node.value, path)
        return
    if node.left:
        get_codes(node.left, path=(path + '0'))
    if node.right:
        get_codes(node.right, path=(path + '1'))

string = 'beep boop beer!'
str_counter = Counter(string)
node_counter = Counter()
for k, v in str_counter.items():
    n = MyNode(value=k)
    node_counter += Counter({n: v})

while len(node_counter) > 1:
    weights = []
    nodes = []
    for i in range(2):
        element = node_counter.most_common()[:-2:-1]
        nodes.append(element[0][0])
        weights.append(element[0][1])
        node_counter.pop(nodes[i])
    root_node = MyNode(left=nodes[0], right=nodes[1])
    node_counter = node_counter + Counter({root_node: (weights[0] + weights[1])})
    # print_counter(node_counter)

root = list(node_counter)[0]
get_codes(root)