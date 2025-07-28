import typer
from c_mod_gen.generate import generate_module

app = typer.Typer()

@app.command()
def scaffold(name: str) -> None:
    """
    Generate a new C module with header and implementation files.

    This command produces a pair of files named ``<name>.h`` and ``<name>.c`` in the
    current working directory, using predefined templates. If files with the same name
    already exist, the operation will fail.

    :param name: The base name of the module to generate
    :type name: str
    :raises typer.Exit: If file generation fails due to invalid input or IO errors
    """
    try:
        generate_module(name)
    except (FileExistsError, OSError, RuntimeError, ValueError) as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)


def main() -> None:
    """The application entry point."""
    app()

if __name__ == "__main__":
    main()
