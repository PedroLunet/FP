def count_parent_boxes(boxes, target):
    count = 1
    box, items = boxes
    
    if target in items:
        return 1
    #elif target not in items:
    #    return -1
    else:
        for i in items:
            if type(i) == tuple:
                


print(count_parent_boxes(("BOX A",[("BOX B", [("BOX C", ["water"])]), "orange", ("BOX D", ["apple", ("BOX E", [])])]), "none")) 
print(count_parent_boxes(("BOX A",[("BOX B", [("BOX C", ["water"])]), "orange", ("BOX D", ["apple", ("BOX E", [])])]), "apple"))
print(count_parent_boxes(("BOX A",[("BOX B", [("BOX C", ["water"])]), "orange", ("BOX D", ["apple", ("BOX E", [])])]), "orange"))
print(count_parent_boxes(("BOX A",[("BOX B", [("BOX C", ["water"])]), "orange", ("BOX D", ["apple", ("BOX E", [])])]), "water"))
print(count_parent_boxes(("BOX A",[("BOX B", [("BOX C", ["water"])]), "orange", ("BOX D", ["apple", ("BOX E", [])])]), "BOX A"))