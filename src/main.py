#!/usr/bin/env python3
import sys
from commit_agent import analyze_changes
from git_utils import stage_files, create_commit

def main():
    """Main entry point for the commit assistant"""
    try:
        # Get suggestions from the agent
        files, message = analyze_changes()
        
        if not files:
            print("No files to commit")
            return 1
            
        # Show suggestions to user
        print("\nSuggested files to commit:")
        for file in files:
            print(f"- {file}")
            
        print(f"\nSuggested commit message:\n{message}")
        
        # Ask for confirmation
        response = input("\nProceed with commit? [y/N] ").lower()
        if response != 'y':
            print("Commit cancelled")
            return 0
            
        # Stage files and create commit
        stage_files(files)
        create_commit(message)
        print("Commit created successfully!")
        return 0
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
