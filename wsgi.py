import os
import importlib.util
from pathlib import Path

def load_app():
    root = Path(__file__).parent
    candidates = []
    # search for python files in repo (exclude venv and hidden dirs)
    for p in root.rglob('*.py'):
        if any(part.startswith('.') or part in ('venv', 'env', '.venv') for part in p.parts):
            continue
        if p.name in ('wsgi.py', 'setup.py'):
            continue
        candidates.append(p)

    for p in candidates:
        try:
            spec = importlib.util.spec_from_file_location(p.stem, str(p))
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            # Prefer an exposed WSGI 'application' or Flask 'app' or factory 'create_app'
            if hasattr(mod, 'application'):
                return getattr(mod, 'application')
            if hasattr(mod, 'app'):
                return getattr(mod, 'app')
            if hasattr(mod, 'create_app'):
                return mod.create_app()
        except Exception:
            # ignore errors while probing files
            continue

    raise RuntimeError(
        "Could not find a Flask app automatically. Edit wsgi.py to import your app directly, e.g. from app import app"
    )


application = load_app()