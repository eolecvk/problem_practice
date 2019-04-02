

# Find all duplicates in list using set (one-liner)
items = [1, 1, 1, 2, 3, 4, 4, 5]
dupes = set([it for it in items if items.count(it) > 1])


# Find intersection of 2 sets..
valid_items = ["rouge", "bleu"]
my_items = ["vert", "rouge"]
my_valid_items = my_items.intersection(valid_items)

# Difference
invalid_items = ["vert", "jaune"]
my_not_invalid_items = my_items.difference(invalid_items)