"""Export the root-level bilingual PPTX to both README cover images.

Edit and save the PPTX in PowerPoint, then run:
    python scripts/export_reading_roadmap.py

Requires Windows, Microsoft PowerPoint, and pywin32. The PPTX is opened read-only.
"""

from pathlib import Path
import hashlib
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "reading-roadmap.pptx"
DESTINATIONS = [
    ROOT / "assets" / "readme" / "reading-roadmap.zh.png",
    ROOT / "assets" / "readme" / "reading-roadmap.en.png",
]


def main():
    import win32com.client

    original_hash = hashlib.sha256(SOURCE.read_bytes()).digest()
    DESTINATIONS[0].parent.mkdir(parents=True, exist_ok=True)
    build = ROOT / ".build"
    build.mkdir(exist_ok=True)
    app = win32com.client.DispatchEx("PowerPoint.Application")
    deck = None
    try:
        with tempfile.TemporaryDirectory(prefix="roadmap-", dir=build) as temp:
            deck = app.Presentations.Open(str(SOURCE), -1, 0, 0)
            if deck.Slides.Count != len(DESTINATIONS):
                raise ValueError("Expected two slides: Chinese first, English second.")
            width = 3200
            height = round(width * deck.PageSetup.SlideHeight / deck.PageSetup.SlideWidth)
            previews = []
            for i, destination in enumerate(DESTINATIONS, start=1):
                preview = Path(temp) / destination.name
                deck.Slides(i).Export(str(preview), "PNG", width, height)
                previews.append(preview)
            deck.Close()
            deck = None
            if hashlib.sha256(SOURCE.read_bytes()).digest() != original_hash:
                raise RuntimeError("PPTX changed during export; run again after saving.")
            for preview, destination in zip(previews, DESTINATIONS):
                # Copy into the assets directory so its normal access permissions apply.
                shutil.copyfile(preview, destination)
                print(f"Updated {destination.relative_to(ROOT)} ({width} x {height})")
    finally:
        if deck is not None:
            deck.Close()
        app.Quit()
        if build.exists() and not any(build.iterdir()):
            build.rmdir()


if __name__ == "__main__":
    main()
