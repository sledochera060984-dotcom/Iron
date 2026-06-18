from pathlib import Path
import base64

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "data" / "raw" / "ossetian_dictionary_sample.xlsx.b64.txt"
target = ROOT / "data" / "raw" / "ossetian_dictionary_sample.xlsx"

text = source.read_text(encoding="utf-8")
# Remove whitespace in case GitHub or an editor wrapped the base64 text.
clean = "".join(text.split())
target.write_bytes(base64.b64decode(clean))

print(f"Written: {target}")
