#!/usr/bin/env python3
"""
Frontend setup script - Tries to build Tailwind CSS and copy Alpine.js.
This script is optional and will not fail if Node.js is not available.
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path


def check_node_available() -> bool:
    """Check if Node.js and npm are available."""
    try:
        subprocess.run(["node", "--version"], capture_output=True, check=True)
        subprocess.run(["npm", "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def setup_frontend(project_dir: Path) -> None:
    """Setup frontend assets (Tailwind CSS + Alpine.js)."""
    print("\n🎨 Setting up frontend assets (Tailwind CSS + Alpine.js)...")
    
    if not check_node_available():
        print("⚠️  Node.js/npm not found. Skipping frontend setup.")
        print("   To setup later, run:")
        print("   1. npm install")
        print("   2. npm run build")
        print("   See FRONTEND_SETUP.md for details.")
        return
    
    try:
        # Change to project directory
        os.chdir(project_dir)
        
        # Install npm dependencies
        print("📦 Installing npm dependencies...")
        subprocess.run(["npm", "install"], check=True, capture_output=True)
        
        # Build Tailwind CSS
        print("🎨 Building Tailwind CSS...")
        subprocess.run(["npm", "run", "build:css"], check=True, capture_output=True)
        
        # Copy Alpine.js
        alpine_source = project_dir / "node_modules" / "alpinejs" / "dist" / "alpine.min.js"
        alpine_dest = project_dir / "app" / "presentation" / "static" / "js" / "alpine.js"
        
        if alpine_source.exists():
            shutil.copy(alpine_source, alpine_dest)
            print("✅ Alpine.js copied successfully")
        else:
            print("⚠️  Alpine.js not found in node_modules")
        
        print("✅ Frontend setup completed!")
        
    except subprocess.CalledProcessError as e:
        print(f"⚠️  Frontend setup failed: {e}")
        print("   You can setup manually later. See FRONTEND_SETUP.md")
    except Exception as e:
        print(f"⚠️  Error during frontend setup: {e}")
        print("   You can setup manually later. See FRONTEND_SETUP.md")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        project_dir = Path(sys.argv[1])
        setup_frontend(project_dir)
    else:
        print("Usage: python setup_frontend.py <project_directory>")

