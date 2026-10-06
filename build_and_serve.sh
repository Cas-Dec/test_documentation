#!/bin/bash
# Quick script to build and serve the documentation site

set -e

cd "$(dirname "$0")/docs-site"

echo "========================================="
echo "HPC Data Documentation Site Builder"
echo "========================================="
echo ""

# Check if mkdocs is installed
if ! command -v mkdocs &> /dev/null; then
    echo "ERROR: mkdocs not found!"
    echo ""
    echo "Install with:"
    echo "  pip install mkdocs mkdocs-material"
    echo ""
    exit 1
fi

# Check if material theme is available
if ! python -c "import material" 2>/dev/null; then
    echo "WARNING: mkdocs-material theme not found"
    echo "Install with: pip install mkdocs-material"
    echo ""
fi

echo "What would you like to do?"
echo ""
echo "  1) Serve locally (recommended for demo)"
echo "  2) Build static HTML"
echo "  3) Validate only (check for errors)"
echo ""
read -p "Enter choice [1-3]: " choice

case $choice in
    1)
        echo ""
        echo "Starting local server..."
        echo "Open http://localhost:8000 in your browser"
        echo "Press Ctrl+C to stop"
        echo ""
        mkdocs serve
        ;;
    2)
        echo ""
        echo "Building static HTML..."
        mkdocs build
        echo ""
        echo "✅ Build complete!"
        echo "Output in: docs-site/site/"
        echo ""
        echo "To view:"
        echo "  cd site && python -m http.server 8000"
        ;;
    3)
        echo ""
        echo "Validating configuration..."
        mkdocs build --strict
        echo ""
        echo "✅ Validation passed!"
        ;;
    *)
        echo "Invalid choice"
        exit 1
        ;;
esac
