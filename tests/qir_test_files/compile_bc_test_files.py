from pathlib import Path
import subprocess

test_files_path = Path("./tests/qir_test_files")

test_files = test_files_path / "*.ll"


def compile_to_bc() -> None:
    subprocess.call(test_files_path / "compile.sh")
