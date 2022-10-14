from pathlib import Path
import subprocess

test_files_path = Path("./tests/qir_test_files")


def check_files() -> None:
    subprocess.call(test_files_path / "check.sh")
