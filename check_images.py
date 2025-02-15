import argparse
import time
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculate_results_stats import calculate_results_stats
from print_results import print_results

# Command-line arguments
def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', help='Path to images folder')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='File with dog names')
    return parser.parse_args()

if __name__ == "__main__":
    start_time = time.time()
    in_arg = get_input_args()

    pet_labels = get_pet_labels(in_arg.dir)
    results = classify_images(in_arg.dir, pet_labels, in_arg.arch)
    adjust_results4_isadog(results, in_arg.dogfile)
    results_stats = calculate_results_stats(results)
    print_results(results, results_stats, in_arg.arch)

    end_time = time.time()
    print(f"\n** Total Time Elapsed: {end_time - start_time:.2f} seconds **")
