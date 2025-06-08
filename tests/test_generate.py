import os
from pathlib import Path
from pytest import MonkeyPatch
from c_mod_gen.generate import generate_module

def test_generate_module_creates_files(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    generate_module("foo")
    assert (tmp_path / f"foo.h").exists()
    assert (tmp_path / f"foo.c").exists()
