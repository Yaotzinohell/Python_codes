from pathlib import Path
path = Path("PYTHON_CODES")
for file in path.glob('*'):
    print(file)