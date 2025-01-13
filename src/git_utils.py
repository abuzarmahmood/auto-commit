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

def push_changes() -> None:
    """Push commits to remote repository"""
    repo = get_repo()
    origin = repo.remote()
    origin.push()
