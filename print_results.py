def print_results(results, results_stats, model):
    print(f"\nModel: {model}")
    print(f"Total Images: {results_stats['total_images']}")
    print(f"Accuracy: {results_stats['accuracy']:.2f}%\n")
