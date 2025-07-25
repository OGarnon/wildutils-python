# main.py
"""
WildUtils CLI - A toolkit of useful Python utilities.
This file handles the command-line interface (CLI) and routes to utility modules.
"""

import argparse  # Used to create the CLI structure
import logging  # Basic logging for user-friendly output

# Importing utility functions from utils folder
from utils import tracker, csvgen, weather, password, renamer

# Configure logging output
logging.basicConfig(level=logging.INFO, format="%(message)s")

def main():
    # Create the main argument parser
    parser = argparse.ArgumentParser(description="WildUtils - A CLI toolset")
    sub = parser.add_subparsers(dest="command", required=True)  # Enable subcommands

    # Subcommand: track
    t = sub.add_parser("track", help="Track days left until a deadline.")
    t.add_argument("date", help="Target date in YYYY-MM-DD format")

    # Subcommand: csvgen
    c = sub.add_parser("csvgen", help="Generate a mock CSV report")
    c.add_argument("output", help="Output filename")

    # Subcommand: weather
    w = sub.add_parser("weather", help="Show fake weather for a city")
    w.add_argument("city", help="City name")

    # Subcommand: pwcheck
    p = sub.add_parser("pwcheck", help="Check password strength")
    p.add_argument("password", help="Password to check")

    # Subcommand: rename
    r = sub.add_parser("rename", help="Batch rename files with a prefix")
    r.add_argument("dir", help="Directory path")
    r.add_argument("prefix", help="Prefix for renamed files")

    # Parse command-line arguments
    args = parser.parse_args()

    # Route to appropriate utility function
    if args.command == "track":
        tracker.days_until(args.date)
    elif args.command == "csvgen":
        csvgen.generate_report(args.output)
    elif args.command == "weather":
        weather.show_weather(args.city)
    elif args.command == "pwcheck":
        password.check_strength(args.password)
    elif args.command == "rename":
        renamer.rename_files(args.dir, args.prefix)

if __name__ == "__main__":
    main()
