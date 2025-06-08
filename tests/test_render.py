from c_mod_gen.render import render_header, render_implementation

def test_render_header_basic() -> None:
    content = render_header("foo")
    assert "#ifndef FOO_H" in content
    assert 'extern "C"' in content

def test_render_header_with_complex_name() -> None:
    content = render_header("foo.bar.baz")
    assert "#ifndef FOO_BAR_BAZ_H" in content

def test_render_implementation_basic() -> None:
    content = render_implementation("foo")
    assert '#include "foo.h"' in content

def test_render_implementation_with_complex_name() -> None:
    content = render_implementation("foo.bar.baz")
    assert '#include "foo.bar.baz.h"' in content
