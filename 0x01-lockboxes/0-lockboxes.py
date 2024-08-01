#!/usr/bin/python3
""" module for canUnlockAll function """


def canUnlockAll(boxes):
    """ a function that solves the puzzle """
    n = len(boxes)
    seen_box = set([0])
    unseen_box = set(boxes[0]) - (set([0]))
    while len(unseen_box) > 0:
        box_index = unseen_box.pop()
        if not box_index or box_index >= n or box_index < 0:
            continue
        if box_index not in seen_box:
            unseen_box = unseen_box.union(boxes[box_index])
            seen_box.add(box_index)
    return n == len(seen_box)
