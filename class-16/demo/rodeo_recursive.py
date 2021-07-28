"""
given a binary tree, where the value of each node is a linked_list, where the value of each linked_list is a value of a list, write a function that will return the following in a tuple.  Sum of all list values, the largest value, the smallest value, and the value furthest removed from 0
"""

def do_obstacle_course(tree):
    report = [0, None, None, None]

    def walk(node):
        if not node:
            return

        current = node.value.head

        while current:

            for num in current.value:
                report[0] += num
                if report[1] is None:
                    report[1] = num
                elif report[1] < num:
                    report[1] = num

                if report[2] is None:
                    report[2] = num
                elif report[2] > num:
                    report[2] = num

            current = current.next

        walk(node.left)
        walk(node.right)

    walk(tree.root)

    if abs(report[1]) > abs(report[2]):
        report[3] = report[1]
    else:
        report[3] = report[2]

    return report