def canUnlockAll(boxes):
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True

    for box_index in range(num_boxes):
        if unlocked_boxes[box_index]:
            keys = boxes[box_index]
            for key in keys:
                if key < num_boxes and not unlocked_boxes[key]:
                    unlocked_boxes[key] = True

    return all(unlocked_boxes)
