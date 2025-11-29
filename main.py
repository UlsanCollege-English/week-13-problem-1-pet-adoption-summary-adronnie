def summarize_adoptions(adoptions):
    counts = {}
    for animal in adoptions:
        counts[animal] = counts.get(animal, 0) + 1
    return counts
