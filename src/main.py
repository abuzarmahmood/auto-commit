#!/usr/bin/env python3
"""
Smart Git commit assistant CLI tool.

This script provides a command-line interface for automatically analyzing Git changes,
generating commit messages, and managing the commit process. It supports automatic
confirmation and push operations through command line flags.
"""
import warnings  # noqa
# Suppress warnings # noqa
warnings.filterwarnings("ignore")  # noqa

import sys
import os
import argparse
from commit_agent import analyze_changes
from git_utils import stage_files, create_commit, push_changes, get_staged_files, get_diff


def main():
    """Main entry point for the commit assistant"""
    parser = argparse.ArgumentParser(description='Smart Git commit assistant')
    parser.add_argument('-d', '--directory',
                        help='Path to git repository (defaults to current directory)',
                        default='.')
    parser.add_argument('-y', '--yes', action='store_true',
                        help='Automatically confirm commit without prompting')
    parser.add_argument('-p', '--push', action='store_true',
                        help='Automatically push changes after commit')
    parser.add_argument('-m', '--message', type=str,
                        help='Seed text to guide commit message generation')
    args = parser.parse_args()

    try:
        # Change to specified directory
        original_dir = os.getcwd()
        os.chdir(args.directory)

        diff_output = get_diff()
        if not diff_output:
            print("No staged changes to commit (use 'git add' first)")
            return 1

        # Check for staged changes
        staged_files = get_staged_files()
        if not staged_files:
            print("No changes staged for commit (use 'git add' first)")
            return 1

        # Get suggestions from the agent
        files, message, cost = analyze_changes(seed_text=args.message)

        if not files:
            print("No files to commit")
            return 1

        # Show suggestions to user
        print("\nSuggested files to commit:")
        for file in files:
            print(f"- {file}")

        print(f"\nSuggested commit message:\n{message}")

        # Handle commit confirmation
        if not args.yes:
            response = input("\nProceed with commit? [y/N] ").lower()
            if response != 'y':
                print("Commit cancelled")
                return 0

        # Stage files and create commit
        stage_files(files)
        create_commit(message)
        print("Commit created successfully!")

        # Handle pushing changes
        if args.push:
            push_changes()
            print("Changes pushed successfully!")
        elif not args.yes:  # Only ask if not in automatic mode
            push_response = input("\nPush changes to remote? [y/N] ").lower()
            if push_response == 'y':
                push_changes()
                print("Changes pushed successfully!")

        # Print operation cost
        print(f"\nOperation cost: ${cost:.4f}")
        return 0

    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1
    finally:
        # Always return to original directory
        if 'original_dir' in locals():
            os.chdir(original_dir)


if __name__ == "__main__":
    sys.exit(main())
