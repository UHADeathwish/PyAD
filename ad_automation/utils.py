import subprocess


def run_powershell(command: str):
    """Run a PowerShell command and return output."""
    return subprocess.run([
        "powershell",
        "-NoProfile",
        "-Command",
        command
    ], capture_output=True, text=True, check=False)
