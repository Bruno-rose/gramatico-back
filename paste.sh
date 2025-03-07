#!/bin/bash

# Exit on any error
set -e

# Script configuration
readonly PROJECT_DIR="/Users/bruno/Developer/gramatico-be"
readonly VENV_DIR=".venv"
readonly PYTHON_CMD="python"
readonly UV_CMD="/opt/homebrew/bin/uv"

# Set secure PATH
export PATH="/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"

# Setup virtual environment
setup_venv() {
    "${UV_CMD}" venv
    source "${VENV_DIR}/bin/activate"
    "${UV_CMD}" pip install .
}

# Main execution
main() {
    # Change to project directory
    cd "${PROJECT_DIR}"

    # Setup or activate virtual environment
    if [ ! -d "${VENV_DIR}" ]; then
        setup_venv
    else
        source "${VENV_DIR}/bin/activate"
    fi

    # Run main application
    "${PYTHON_CMD}" main.py

    # Notify user
    osascript -e 'display notification "Corrected content copied to clipboard" with title "Gramatico"'
}

# Execute main function
main
