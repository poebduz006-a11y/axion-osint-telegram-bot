#!/usr/bin/env python3
from pathlib import Path
import runpy, tempfile, sys
base = Path(__file__).parent
code = (base / "bot_part1.py").read_text() + (base / "bot_part2.py").read_text()
tmp = Path(tempfile.gettempdir()) / "axion_osint_bot_run.py"
tmp.write_text(code)
sys.argv[0] = str(tmp)
runpy.run_path(str(tmp), run_name="__main__")
