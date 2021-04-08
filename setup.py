import subprocess
import sys


def install_mongo_client():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymongo"])


if __name__ == "__main__":
    install_mongo_client()
