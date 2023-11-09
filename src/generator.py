import pandas as pd
import converter
from pathlib import Path
from rich import print


def main(
    guest_path: Path = Path("guests.csv"),
    template_path: Path = Path("templates/template.md"),
    output_path: Path = Path("output"),
) -> None:
    guests = pd.read_csv(guest_path)["name"]

    for guest in guests:
        print(f"Generating file for [bold green]{guest}[/bold green]")
        converter.markdown_to_pdf(
            template_path, {"name": guest}, output_path / f"{guest}.pdf"
        )


if __name__ == "__main__":
    main()
