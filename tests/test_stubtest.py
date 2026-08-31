import subprocess
import sys
from pathlib import Path
allowlist = Path(__file__).parent.parent / "allowlist.txt"
def test_stubtest():
    result = subprocess.run(
        [sys.executable, "-m", "mypy.stubtest", "pygal", "--allowlist", str(allowlist)],
        capture_output=True, text=True,
    )
    assert result.returncode == 0, result.stdout