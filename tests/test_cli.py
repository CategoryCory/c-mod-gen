from pathlib import Path
from pytest import MonkeyPatch
from typer.testing import CliRunner
from c_mod_gen.cli import app

runner = CliRunner()

def test_scaffold_command(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["bar"])
    assert result.exit_code == 0
    assert (tmp_path / f"bar.h").exists()
    assert (tmp_path / f"bar.c").exists()

def test_scaffold_with_duplicate_file(tmp_path: Path, monkeypatch: MonkeyPatch) -> None:
    monkeypatch.chdir(tmp_path)
    (tmp_path / "dup.h").write_text("// existing file")
    result = runner.invoke(app, ["dup"])
    assert result.exit_code != 0
    assert "already exists" in result.stderr
