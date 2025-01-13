"""
Git utility functions for interacting with repositories.

This module provides a collection of helper functions for common Git operations
like getting repository information, staging files, creating commits, and pushing changes.
"""

from git import Repo
from typing import List, Tuple


def get_repo() -> Repo:
    """Get git repository object for current directory"""
    return Repo(".")


def get_staged_files() -> List[str]:
    """Get list of files staged for commit"""
    repo = get_repo()
    return [item.a_path for item in repo.index.diff("HEAD")]


def get_diff() -> str:
    """Get git diff output for staged changes"""
    repo = get_repo()
    return repo.git.diff("--cached")


def stage_files(files: List[str]) -> None:
    """Stage specified files for commit"""
    repo = get_repo()
    repo.index.add(files)


def create_commit(message: str) -> None:
    """Create a commit with the given message"""
    repo = get_repo()
    repo.index.commit(message)


def get_current_branch() -> str:
    """Get name of current branch"""
    repo = get_repo()
    return repo.active_branch.name


def push_changes() -> None:
    """Push commits to remote repository"""
    repo = get_repo()
    origin = repo.remote()
    current_branch = get_current_branch()
    print(f"Pushing changes to {origin.url} on branch {current_branch}")
    origin.push(
        refspec=f'refs/heads/{current_branch}:refs/heads/{current_branch}')
