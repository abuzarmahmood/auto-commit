#!/bin/bash

autocommit() {
    local script_dir="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"
    /media/bigdata/projects/auto-commit/venv/bin/python "$script_dir/main.py" "$@"
}

# Export the function so it's available in subshells
export -f autocommit
