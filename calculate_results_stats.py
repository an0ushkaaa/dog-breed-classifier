def calculate_results_stats(results):
    correct_classifications = sum(1 for labels in results.values() if labels[2] == labels[3])
    total_images = len(results)
    accuracy = (correct_classifications / total_images) * 100
    return {"accuracy": accuracy, "total_images": total_images}
