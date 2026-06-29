#!/usr/bin/env python3

import argparse
import json

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            print(f"Searching for: {args.query}") 
            
            with open("/home/anpenlibe/workspace/projects/rag-search-engine/data/movies.json") as file:
                data = json.load(file)
            
            movies = data["movies"]
            results = []
            index = 1

            # search logic, results for only 5 indices
            for movie in movies:               
                if args.query.lower() in movie["title"].lower():
                    results.append(movie["title"])
                    print(f"{index}. {movie["title"]}")
                    index += 1
                if index > 5:
                    break

            

            
        case _:
            parser.print_help()

if __name__ == "__main__":
    main()
