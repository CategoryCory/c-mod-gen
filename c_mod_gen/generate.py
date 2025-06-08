import keyword
from pathlib import Path
from c_mod_gen.render import render_header, render_implementation
from c_mod_gen.reserved_keywords import reserved_keywords

def generate_module(name: str) -> None:
    """
    Generates a C module and writes `.h` and `.c` files to disk.

    This function creates a C module (both header and implementation) using the supplied
    name and saves both files to disk.

    :param name: The base name of the module
    :type name: str
    :raises FileExistsError: If the module files already exist
    :raises OSError: If the module files could not be created
    """
    if name in reserved_keywords or not name.isidentifier() or keyword.iskeyword(name):
        raise ValueError(f"Invalid module name: '{name!r}'")

    header_file_path = Path(f"{name}.h")
    impl_file_path = Path(f"{name}.c")

    if header_file_path.exists() or impl_file_path.exists():
        raise FileExistsError(f"{name}.h/.c already exists")

    header = render_header(name)
    implementation = render_implementation(name)

    try:
        header_file_path.write_text(header)
        impl_file_path.write_text(implementation)
    except OSError as e:
        raise OSError(f"Failed to write module '{name!r}' to disk") from e
