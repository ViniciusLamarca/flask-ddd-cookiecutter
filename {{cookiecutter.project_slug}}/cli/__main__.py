"""CLI main entry point."""
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from app import create_app

if __name__ == "__main__":
    app = create_app()
    # Flask CLI will automatically discover commands registered via app.cli
    app.cli()

