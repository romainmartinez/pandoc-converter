import pypandoc
from pathlib import Path


def read_template(template_path: Path) -> str:
    with open(template_path, "r") as f:
        return f.read()


def replace_template_args(template: str, template_args: dict) -> str:
    for key, value in template_args.items():
        template = template.replace(f"[{key}]", value)
    return template


def markdown_to_pdf(
    template_path: Path, template_args: dict, output_path: Path
) -> None:
    pypandoc.convert_text(  # type: ignore
        source=replace_template_args(read_template(template_path), template_args),
        format="md",
        to="pdf",
        outputfile=output_path,
        extra_args=["--pdf-engine=tectonic"],
    )
