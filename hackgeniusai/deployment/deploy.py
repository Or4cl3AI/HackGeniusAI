```python
import os
import subprocess

def install_requirements():
    """Install required packages."""
    subprocess.check_call(["python", '-m', 'pip', 'install', '-r', 'requirements.txt'])

def setup_database():
    """Set up the database."""
    from hackgeniusai.dynamic_learning_path import setup_db
    setup_db()

def start_server():
    """Start the Flask server."""
    os.chdir("../")
    os.system("python web_app.py")

def main():
    install_requirements()
    setup_database()
    start_server()

if __name__ == "__main__":
    main()
```