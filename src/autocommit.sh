#!/bin/bash

autocommit() {
    local script_dir="$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")"
    local repo_root="$(dirname "$script_dir")"
    local venv_python="$repo_root/venv/bin/python"

    if [ ! -x "$venv_python" ]; then
        echo "Error: Python executable not found at $venv_python"
        echo "Please ensure you have set up the virtual environment correctly"
        return 1
    fi

    "$venv_python" "$script_dir/main.py" "$@"
}

# Export the function so it's available in subshells
export -f autocommit
