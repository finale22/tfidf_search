import argparse
from results_printer import print_results

def main():
    parser = argparse.ArgumentParser(description="TF-IDF search")
    parser.add_argument("--mode", 
                        type=str, required=True, 
                        choices=["search"], 
                        help="Please type \"search\"")
    
    args = parser.parse_args()
    if args.mode == "search":
        print_results()

if __name__ == "__main__":
    main()