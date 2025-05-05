import runpy
import os

def main():
    script_path = os.path.join(os.path.dirname(__file__), "main.py")
    runpy.run_path(script_path, run_name="__main__")


if __name__ == "__main__":
    main()