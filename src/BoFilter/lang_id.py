from pathlib import Path
import shutil
import langid

def filter_tibetan_text_langid(input_dir: Path, output_dir: Path, threshold: float = 0.5):
    """
    Filters files in a directory to keep only those identified as Tibetan using langid.

    Args:
        input_dir (Path): Path to the input directory.
        output_dir (Path): Path to the output directory where Tibetan files will be saved.
        threshold (float): Minimum proportion of Tibetan lines for a file to be considered Tibetan.
    """
    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    print(f"Processing files in '{input_dir}' using langid...")
    for file_path in input_dir.iterdir():
        if file_path.is_file():
            try:
                with file_path.open('r', encoding='utf-8') as f:
                    lines = f.readlines()
                
                if not lines:
                    continue

                tibetan_lines = 0
                total_lines = 0
                for line in lines:
                    stripped_line = line.strip()
                    if stripped_line:
                        total_lines += 1
                        lang, _ = langid.classify(stripped_line)
                        if lang in ['bo', 'dz']:
                            tibetan_lines += 1
                
                if total_lines > 0 and (tibetan_lines / total_lines) >= threshold:
                    output_file_path = output_dir / file_path.name
                    shutil.copy(file_path, output_file_path)
                    print(f"  - Copied '{file_path.name}' to '{output_dir}'")

            except Exception as e:
                print(f"Could not process file {file_path}. Error: {e}")


