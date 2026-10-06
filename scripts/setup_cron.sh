#!/bin/bash
# Setup cron job for automated documentation updates
# Usage: bash scripts/setup_cron.sh [--install|--uninstall|--check]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
CRON_SCRIPT="$REPO_ROOT/scripts/update_site.py"
LOG_DIR="$REPO_ROOT/logs"

# Default: run every 6 hours
CRON_SCHEDULE="0 */6 * * *"

# Create log directory
mkdir -p "$LOG_DIR"

show_usage() {
    cat <<EOF
Setup automated documentation updates via cron

Usage: $0 [OPTIONS]

Options:
    --install       Install the cron job
    --uninstall     Remove the cron job
    --check         Check current cron configuration
    --test          Run the update script once (dry-run)
    --help          Show this help message

Environment:
    CRON_SCHEDULE   Override default schedule (default: "0 */6 * * *")
                    Examples:
                      "0 */6 * * *"    - Every 6 hours
                      "0 0 * * *"      - Daily at midnight
                      "*/30 * * * *"   - Every 30 minutes

Examples:
    # Install with default schedule (every 6 hours)
    $0 --install

    # Install with custom schedule (daily at 2 AM)
    CRON_SCHEDULE="0 2 * * *" $0 --install

    # Test the update script
    $0 --test
EOF
}

check_dependencies() {
    echo "Checking dependencies..."

    # Check Python
    if ! command -v python3 &> /dev/null; then
        echo "ERROR: python3 not found"
        exit 1
    fi

    # Check required Python packages
    python3 -c "import yaml, jsonschema" 2>/dev/null || {
        echo "ERROR: Required Python packages not found"
        echo "Install with: pip install pyyaml jsonschema"
        exit 1
    }

    # Check mkdocs
    if ! command -v mkdocs &> /dev/null; then
        echo "ERROR: mkdocs not found"
        echo "Install with: pip install mkdocs mkdocs-material"
        exit 1
    fi

    echo "✓ All dependencies found"
}

get_cron_entry() {
    # Generate the cron entry
    cat <<EOF
# HPC Documentation Auto-Update (managed by setup_cron.sh)
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
$CRON_SCHEDULE cd "$REPO_ROOT" && python3 "$CRON_SCRIPT" --commit --notify-on-error >> "$LOG_DIR/cron-update.log" 2>&1
EOF
}

install_cron() {
    echo "Installing cron job..."
    check_dependencies

    # Check if cron job already exists
    if crontab -l 2>/dev/null | grep -q "update_site.py"; then
        echo "WARNING: Cron job already exists. Remove it first with --uninstall"
        exit 1
    fi

    # Add cron job
    (crontab -l 2>/dev/null || true; get_cron_entry) | crontab -

    echo "✓ Cron job installed successfully"
    echo ""
    echo "Schedule: $CRON_SCHEDULE"
    echo "Logs: $LOG_DIR/cron-update.log"
    echo ""
    echo "To check logs: tail -f $LOG_DIR/cron-update.log"
}

uninstall_cron() {
    echo "Removing cron job..."

    # Remove lines related to update_site.py
    crontab -l 2>/dev/null | grep -v "update_site.py" | grep -v "HPC Documentation Auto-Update" | crontab - || true

    echo "✓ Cron job removed"
}

check_cron() {
    echo "Current cron configuration:"
    echo ""

    if crontab -l 2>/dev/null | grep -q "update_site.py"; then
        crontab -l 2>/dev/null | grep -A2 "HPC Documentation Auto-Update"
        echo ""
        echo "✓ Cron job is installed"

        if [ -f "$LOG_DIR/cron-update.log" ]; then
            echo ""
            echo "Last 10 log entries:"
            tail -n 10 "$LOG_DIR/cron-update.log"
        fi
    else
        echo "No cron job installed"
        echo "Run '$0 --install' to set it up"
    fi
}

test_run() {
    echo "Running update script (dry-run)..."
    check_dependencies

    cd "$REPO_ROOT"
    python3 "$CRON_SCRIPT" --dry-run

    echo ""
    echo "✓ Test completed successfully"
    echo "Run '$0 --install' to enable automatic updates"
}

# Main script
case "${1:-}" in
    --install)
        install_cron
        ;;
    --uninstall)
        uninstall_cron
        ;;
    --check)
        check_cron
        ;;
    --test)
        test_run
        ;;
    --help|-h)
        show_usage
        ;;
    *)
        show_usage
        exit 1
        ;;
esac
