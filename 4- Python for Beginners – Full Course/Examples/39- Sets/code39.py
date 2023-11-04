# Sets are like python dictionaries, but doesn't have keys, are unordered and immutable
# Useful when you think of them as mathematical sets
# A set cannot have two of the same item, it erases repeated items

set1 = {"Roger", "Syd"}
set2 = {"Roger", "Luna"}
set3 = {"Roger", "Roger"}

intersect = set1 & set2
print(intersect)

union = set1 | set2
print(union)

difference = set1 - set2
print(difference)

contained = set1 > set3  # is set3 contained in set1?
print(contained)

contained = set1 < set3  # is set1 contained in set3?
print(contained)

print(len(set1))
print(list(set1))


