"""Write the long-roast entry to /output/entry.txt.

One sentence, 203 characters (limit 320) -- no trailing newline."""

from pathlib import Path

ENTRY = "They want to write the laws for artificial intelligence, cryptocurrency, and the entire internet, but their own office just emailed me a photo of a printed PDF and asked me to convert it back into a PDF."

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
