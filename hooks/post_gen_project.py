#!/usr/bin/env python3
"""
Post-generation hook for Cookiecutter Flask template.
Handles conditional file removal and configuration adjustments.
"""
import os
import shutil
import sys
from pathlib import Path
from typing import Any

# Try to import TOML parser - use tomlkit if available, fallback to tomllib/tomli
try:
    import tomlkit  # type: ignore[import-untyped]
    HAS_TOMLKIT = True
except ImportError:
    HAS_TOMLKIT = False
    try:
        import tomllib  # Python 3.11+ - type: ignore[import-untyped]
        HAS_TOMLLIB = True
    except ImportError:
        try:
            import tomli  # type: ignore[import-untyped]
            HAS_TOMLLIB = True
        except ImportError:
            HAS_TOMLLIB = False


def remove_redis_files(context: dict[str, str]) -> None:
    """Remove Redis-related files if Redis is not being used."""
    project_dir = Path("{{ cookiecutter.project_slug }}")
    
    if not project_dir.exists():
        print(f"⚠️  Warning: Project directory {project_dir} does not exist")
        return
    
    redis_files = [
        project_dir / "app" / "infrastructure" / "redis",
        project_dir / "app" / "infrastructure" / "cache",
    ]
    
    for file_path in redis_files:
        try:
            if file_path.exists():
                if file_path.is_dir():
                    shutil.rmtree(file_path)
                else:
                    file_path.unlink()
                print(f"Removed: {file_path}")
        except (OSError, PermissionError) as e:
            print(f"⚠️  Warning: Could not remove {file_path}: {e}")
        except Exception as e:
            print(f"❌ Error removing {file_path}: {e}")
            raise


def remove_websocket_files(context: dict[str, str]) -> None:
    """Remove WebSocket-related files if WebSocket is not being used."""
    project_dir = Path("{{ cookiecutter.project_slug }}")
    
    if not project_dir.exists():
        print(f"⚠️  Warning: Project directory {project_dir} does not exist")
        return
    
    websocket_files = [
        project_dir / "app" / "infrastructure" / "websocket",
        project_dir / "app" / "presentation" / "websocket",
        project_dir / "run_websocket.py",
    ]
    
    for file_path in websocket_files:
        try:
            if file_path.exists():
                if file_path.is_dir():
                    shutil.rmtree(file_path)
                else:
                    file_path.unlink()
                print(f"Removed: {file_path}")
        except (OSError, PermissionError) as e:
            print(f"⚠️  Warning: Could not remove {file_path}: {e}")
        except Exception as e:
            print(f"❌ Error removing {file_path}: {e}")
            raise


def validate_toml_file(file_path: Path) -> bool:
    """Validate that a TOML file exists and is readable."""
    if not file_path.exists():
        return False
    if not file_path.is_file():
        return False
    try:
        content = file_path.read_text(encoding="utf-8")
        if not content.strip():
            return False
        # Try to parse to validate TOML structure
        if HAS_TOMLKIT:
            tomlkit.parse(content)
        elif HAS_TOMLLIB:
            if "tomllib" in sys.modules:
                import tomllib  # type: ignore[import-untyped]
                tomllib.loads(content.encode("utf-8"))
            else:
                import tomli  # type: ignore[import-untyped]
                tomli.loads(content)
        return True
    except (SyntaxError, ValueError, UnicodeDecodeError):
        # Invalid TOML or encoding issue
        return False
    except Exception:
        # Other errors - assume file is valid but parser issue
        return True  # Allow processing to continue


def update_pyproject_toml(context: dict[str, str]) -> None:
    """Update pyproject.toml to remove Redis and WebSocket dependencies if not used."""
    project_dir = Path("{{ cookiecutter.project_slug }}")
    pyproject_path = project_dir / "pyproject.toml"
    
    # Validate file before processing
    if not validate_toml_file(pyproject_path):
        print(f"⚠️  Warning: {pyproject_path} not found or invalid, skipping update")
        return
    
    use_redis = context.get("use_redis", "y").lower() == "y"
    use_websocket = context.get("use_websocket", "y").lower() == "y"
    
    try:
        content = pyproject_path.read_text(encoding="utf-8")
        
        if HAS_TOMLKIT:
            # Use tomlkit to preserve formatting
            doc = tomlkit.parse(content)
            
            # Get dependencies section
            if "tool" in doc and "poetry" in doc["tool"]:
                poetry = doc["tool"]["poetry"]
                if "dependencies" in poetry:
                    deps = poetry["dependencies"]
                    
                    if not use_redis and "redis" in deps:
                        del deps["redis"]
                        print("Updated pyproject.toml: removed Redis dependency")
                    
                    if not use_websocket:
                        removed_any = False
                        for dep in ["flask-socketio", "python-socketio", "eventlet"]:
                            if dep in deps:
                                del deps[dep]
                                removed_any = True
                        if removed_any:
                            print("Updated pyproject.toml: removed WebSocket dependencies")
            
            # Write back with preserved formatting
            pyproject_path.write_text(tomlkit.dumps(doc), encoding="utf-8")
            
        elif HAS_TOMLLIB:
            # Fallback: read with parser, write manually (less ideal but safer than regex)
            if "tomllib" in sys.modules:
                import tomllib  # type: ignore[import-untyped]
                data = tomllib.loads(content.encode("utf-8"))
            else:
                import tomli  # type: ignore[import-untyped]
                data = tomli.loads(content)
            
            # Remove dependencies
            if "tool" in data and "poetry" in data["tool"]:
                poetry = data["tool"]["poetry"]
                if "dependencies" in poetry:
                    deps = poetry["dependencies"]
                    
                    if not use_redis and "redis" in deps:
                        del deps["redis"]
                        print("Updated pyproject.toml: removed Redis dependency")
                    
                    if not use_websocket:
                        removed_any = False
                        for dep in ["flask-socketio", "python-socketio", "eventlet"]:
                            if dep in deps:
                                del deps[dep]
                                removed_any = True
                        if removed_any:
                            print("Updated pyproject.toml: removed WebSocket dependencies")
            
            # Write back using toml (if available) or manual formatting
            try:
                import toml  # type: ignore[import-untyped]
                pyproject_path.write_text(toml.dumps(data), encoding="utf-8")
            except ImportError:
                # Last resort: manual write (preserve structure as much as possible)
                print("⚠️  Warning: Could not write TOML properly, manual edit may be needed")
                print("   Install tomlkit for best results: pip install tomlkit")
                return
        else:
            print("⚠️  Warning: No TOML parser available, skipping pyproject.toml update")
            print("   Install tomlkit: pip install tomlkit")
            return
            
    except Exception as e:
        print(f"❌ Error updating pyproject.toml: {e}")
        print("   File will be left unchanged")
        raise


def update_env_example(context: dict[str, str]) -> None:
    """Update env.example to remove Redis variables if not used."""
    project_dir = Path("{{ cookiecutter.project_slug }}")
    env_example_path = project_dir / "env.example"
    
    if not env_example_path.exists():
        print(f"⚠️  Warning: {env_example_path} not found, skipping update")
        return
    
    if not env_example_path.is_file():
        print(f"⚠️  Warning: {env_example_path} is not a file, skipping update")
        return
    
    use_redis = context.get("use_redis", "y").lower() == "y"
    
    if not use_redis:
        try:
            content = env_example_path.read_text(encoding="utf-8")
            # Remove Redis-related variables
            lines = content.split("\n")
            filtered_lines = []
            skip_next = False
            
            for line in lines:
                if line.strip().startswith("# Redis"):
                    skip_next = True
                    continue
                if skip_next and (line.strip() == "" or line.strip().startswith("#")):
                    skip_next = False
                    if line.strip() != "":
                        filtered_lines.append(line)
                    continue
                if skip_next:
                    continue
                if any(var in line for var in ["REDIS_HOST", "REDIS_PORT", "REDIS_PASSWORD", "REDIS_DB"]):
                    continue
                filtered_lines.append(line)
            
            env_example_path.write_text("\n".join(filtered_lines), encoding="utf-8")
            print("Updated env.example: removed Redis variables")
        except (OSError, UnicodeDecodeError) as e:
            print(f"❌ Error updating env.example: {e}")
            print("   File will be left unchanged")
            raise
        except Exception as e:
            print(f"❌ Unexpected error updating env.example: {e}")
            raise


def update_dynaconf_settings(context: dict[str, str]) -> None:
    """Update Dynaconf settings to remove Redis and WebSocket config if not used."""
    project_dir = Path("{{ cookiecutter.project_slug }}")
    settings_path = project_dir / "app" / "infrastructure" / "config" / "settings.toml"
    
    # Validate file before processing
    if not validate_toml_file(settings_path):
        print(f"⚠️  Warning: {settings_path} not found or invalid, skipping update")
        return
    
    use_redis = context.get("use_redis", "y").lower() == "y"
    use_websocket = context.get("use_websocket", "y").lower() == "y"
    
    try:
        content = settings_path.read_text(encoding="utf-8")
        
        if HAS_TOMLKIT:
            # Use tomlkit to preserve formatting
            doc = tomlkit.parse(content)
            
            # Remove Redis section
            if not use_redis and "redis" in doc:
                del doc["redis"]
                print("Updated settings.toml: removed Redis configuration")
            
            # Remove WebSocket section
            if not use_websocket and "socketio" in doc:
                del doc["socketio"]
                print("Updated settings.toml: removed WebSocket configuration")
            
            # Write back with preserved formatting
            settings_path.write_text(tomlkit.dumps(doc), encoding="utf-8")
            
        elif HAS_TOMLLIB:
            # Fallback: read with parser, write manually
            if "tomllib" in sys.modules:
                import tomllib  # type: ignore[import-untyped]
                data = tomllib.loads(content.encode("utf-8"))
            else:
                import tomli  # type: ignore[import-untyped]
                data = tomli.loads(content)
            
            # Remove sections
            if not use_redis and "redis" in data:
                del data["redis"]
                print("Updated settings.toml: removed Redis configuration")
            
            if not use_websocket and "socketio" in data:
                del data["socketio"]
                print("Updated settings.toml: removed WebSocket configuration")
            
            # Write back
            try:
                import toml  # type: ignore[import-untyped]
                settings_path.write_text(toml.dumps(data), encoding="utf-8")
            except ImportError:
                print("⚠️  Warning: Could not write TOML properly, manual edit may be needed")
                print("   Install tomlkit for best results: pip install tomlkit")
                return
        else:
            print("⚠️  Warning: No TOML parser available, skipping settings.toml update")
            print("   Install tomlkit: pip install tomlkit")
            return
            
    except Exception as e:
        print(f"❌ Error updating settings.toml: {e}")
        print("   File will be left unchanged")
        raise


def update_app_init(context):
    """Update app/__init__.py to remove Redis initialization if not used.
    
    Note: This is mainly for cleanup. The Jinja2 template in app/__init__.py
    is already processed by Cookiecutter, so Redis code is automatically
    removed if use_redis is False. This function is kept for any edge cases.
    """
    # The Jinja2 template handles this automatically, so no action needed
    pass


def copy_env_example() -> None:
    """Copy env.example to .env if it doesn't exist."""
    project_dir = Path("{{ cookiecutter.project_slug }}")
    env_example = project_dir / "env.example"
    env_file = project_dir / ".env"
    
    if not env_example.exists():
        print(f"⚠️  Warning: {env_example} not found, skipping .env creation")
        return
    
    if not env_example.is_file():
        print(f"⚠️  Warning: {env_example} is not a file, skipping .env creation")
        return
    
    if env_file.exists():
        print(f"ℹ️  {env_file} already exists, skipping copy")
        return
    
    try:
        shutil.copy(env_example, env_file)
        print(f"Created .env from env.example")
    except (OSError, PermissionError) as e:
        print(f"⚠️  Warning: Could not create .env: {e}")
    except Exception as e:
        print(f"❌ Error creating .env: {e}")
        raise


def main():
    """Main hook execution."""
    context = {
        "use_redis": "{{ cookiecutter.include_redis }}",
        "use_websocket": "{{ cookiecutter.include_websocket }}",
    }
    
    use_redis = context.get("use_redis", "y").lower() == "y"
    use_websocket = context.get("use_websocket", "y").lower() == "y"
    
    if not use_redis:
        print("Redis not selected. Removing Redis-related files and configurations...")
        remove_redis_files(context)
        print("Redis components removed successfully.")
    else:
        print("Redis selected. Keeping Redis-related files and configurations.")
    
    if not use_websocket:
        print("WebSocket not selected. Removing WebSocket-related files and configurations...")
        remove_websocket_files(context)
        print("WebSocket components removed successfully.")
    else:
        print("WebSocket selected. Keeping WebSocket-related files and configurations.")
    
    # Update configurations
    update_pyproject_toml(context)
    if not use_redis:
        update_env_example(context)
    update_dynaconf_settings(context)
    # app/__init__.py is already processed by Jinja2 template, no need to update
    
    # Copy env.example to .env
    copy_env_example()
    
    # Try to setup frontend (optional - won't fail if Node.js not available)
    try:
        project_dir = Path("{{ cookiecutter.project_slug }}")
        setup_script = Path(__file__).parent / "setup_frontend.py"
        
        if not setup_script.exists():
            print("ℹ️  Frontend setup script not found, skipping")
            return
        
        import subprocess
        result = subprocess.run(
            [sys.executable, str(setup_script), str(project_dir)],
            capture_output=True,
            text=True,
            timeout=300  # 5 minute timeout
        )
        
        if result.returncode == 0:
            if result.stdout:
                print(result.stdout)
        else:
            print("⚠️  Frontend setup skipped (Node.js not available or error occurred)")
            if result.stderr:
                print(f"   Error: {result.stderr[:200]}")  # Limit error message length
            print("   See FRONTEND_SETUP.md for manual setup instructions")
            
    except subprocess.TimeoutExpired:
        print("⚠️  Frontend setup timed out, skipping")
        print("   See FRONTEND_SETUP.md for manual setup instructions")
    except FileNotFoundError:
        print("⚠️  Frontend setup skipped (Python interpreter not found)")
        print("   See FRONTEND_SETUP.md for manual setup instructions")
    except subprocess.SubprocessError as e:
        print(f"⚠️  Frontend setup skipped: {e}")
        print("   See FRONTEND_SETUP.md for manual setup instructions")
    except (OSError, PermissionError) as e:
        print(f"⚠️  Frontend setup skipped (permission error): {e}")
        print("   See FRONTEND_SETUP.md for manual setup instructions")
    except Exception as e:
        print(f"⚠️  Frontend setup skipped (unexpected error): {type(e).__name__}: {e}")
        print("   See FRONTEND_SETUP.md for manual setup instructions")
    
    print("\n✅ Project generated successfully!")
    print(f"📁 Project directory: {{ cookiecutter.project_slug }}/")
    print("\nNext steps:")
    print("1. cd {{ cookiecutter.project_slug }}")
    print("2. poetry install")
    print("3. npm install (para instalar Tailwind CSS e Alpine.js)")
    print("4. npm run build (para compilar assets frontend)")
    print("5. poetry run pre-commit install (instalar hooks de qualidade)")
    print("6. Update .env with your configuration")
    print("7. poetry run flask cli migrate")
    print("8. poetry run flask run")
    print("9. Visit http://localhost:5000 to see the welcome page! 🎉")
    print("\n📚 Important files:")
    print("   - CODE_STANDARDS.md: Padrões de código obrigatórios")
    print("   - .editorconfig: Configuração de formatação")
    print("   - .pre-commit-config.yaml: Hooks de validação")
    print("   - pyproject.toml: Configurações de ferramentas")
    print("\n⚠️  Code quality is enforced by pre-commit hooks!")
    print("   All code must pass linting, type checking, and formatting checks.")


if __name__ == "__main__":
    main()

