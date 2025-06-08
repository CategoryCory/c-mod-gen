import re
from datetime import datetime
from jinja2 import Environment, PackageLoader, select_autoescape, TemplateNotFound, TemplateError

env = Environment(
    loader=PackageLoader("c_mod_gen"),
    autoescape=select_autoescape(["j2", ])
)

def render_header(name: str) -> str:
    """
    Renders a C header file for the given module name using a Jinja2 template.

    This function loads the header template and substitutes placeholders such as the module
    name and header guard. The result is a complete `.h` header file suitable for inclusion
    in a C project. The generated header includes standard header guards and `extern "C"`
    directives for C++ compatibility.

    :param name: The base name of the module
    :type name: str
    :return: The rendered contents of the header file
    :rtype: str
    :raises TemplateNotFound: If the template could not be found
    :raises TemplateError: If the template could not be rendered
    """
    guard = re.sub(r"""\W+\s*""", "_", name.upper(), flags=re.VERBOSE)
    guard = f"{guard}_H"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        return env.get_template('header.j2').render(
            name=name,
            guard=guard,
            timestamp=timestamp,
        )
    except TemplateNotFound:
        raise RuntimeError(f"Template '{name}' not found")
    except TemplateError as e:
        raise RuntimeError(f"Template rendering error '{e}'") from e

def render_implementation(name: str) -> str:
    """
    Renders a C implementation file for the given module name using a Jinja2 template.

    This function loads the implementation template and substitutes placeholders such as the module
    name. The generated implementation file includes a `#include` directive for the corresponding
    header file.

    :param name: The base name of the module
    :type name: str
    :return: The rendered contents of the implementation file
    :rtype: str
    :raises TemplateNotFound: If the template could not be found
    :raises TemplateError: If the template could not be rendered
    """
    try:
        return env.get_template('implementation.j2').render(name=name)
    except TemplateNotFound:
        raise RuntimeError(f"Template '{name}' not found")
    except TemplateError as e:
        raise RuntimeError(f"Template rendering error '{e}'") from e
