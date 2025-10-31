import shutil
from pathlib import Path
from BoFilter.lang_id import filter_tibetan_text_langid

def test_filter_tibetan_text_langid():
    input_dir = Path("tests/data/input")
    output_dir = Path("tests/data/output")
    filter_tibetan_text_langid(input_dir, output_dir, threshold=0.8)
    assert output_dir.exists()
    assert len(list(output_dir.iterdir())) == 2
    assert (output_dir / "doc1.txt").exists()
    assert (output_dir / "doc3.txt").exists()

    shutil.rmtree(output_dir)