def adjust_results4_isadog(results, dogfile):
    with open(dogfile, "r") as f:
        dog_names = set(f.read().strip().split("\n"))

    for filename, labels in results.items():
        is_pet_dog = labels[0] in dog_names
        is_classified_dog = labels[1] in dog_names
        labels.extend([1 if is_pet_dog else 0, 1 if is_classified_dog else 0])
