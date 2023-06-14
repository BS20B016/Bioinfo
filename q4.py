# Define the human and chicken hemoglobin sequences
human_hb = "MVHLTPEEKSAVTALWGKVNVDEVGGEALGRLLVVYPWTQRFFESFGDLSTPDAVMGNPKVKAHGKKVLGAFSDGLAHLDNLKGTFATLSELHCDKLHVDPENFRLLGNVLVCVLAHHFGKEFTPPVQAAYQKVVAGVANALAHKYH"
chicken_hb = "MVLSPADKTNVKAAWGKVGAHAGEYGAEALERMFLSFPTTKTYFPHFDLSHGSAQVKGHGKKVADALTNAVAHVDDMPNALSALSDLHAHKLRVDPVNFKLLSHCLLVTLAAHLPAEFTPAVHASLDKFLANVSTVLTSKYR"

# Define the length of the pentapeptides to match
k = 5

# Find all the matching pentapeptides and their frequency of occurrence
human_pentapeptides = set(human_hb[i:i+k] for i in range(len(human_hb) - k + 1))
chicken_pentapeptides = set(chicken_hb[i:i+k] for i in range(len(chicken_hb) - k + 1))
matching_pentapeptides = human_pentapeptides.intersection(chicken_pentapeptides)

matching_pentapeptides_counts = {}
for pentapeptide in matching_pentapeptides:
    human_count = human_hb.count(pentapeptide)
    chicken_count = chicken_hb.count(pentapeptide)
    matching_pentapeptides_counts[pentapeptide] = (human_count, chicken_count)

# Print the matching pentapeptides and their frequency of occurrence
for pentapeptide, (human_count, chicken_count) in matching_pentapeptides_counts.items():
    print(f"{pentapeptide}: {human_count} (human), {chicken_count} (chicken)")
