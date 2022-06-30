# Python Imports
This code is set up so that `main.py` works without any problems. However, I'd also like to be able to run each of the modules on their own to debug outputs. Running any of the modules with (e.g.) `python3 scripts/script.py` causes errors with the import. It turns out that the solution is to use `python3 -m scripts.script` instead, which magically works without problems.
