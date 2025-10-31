import fasttext
from pathlib import Path
import shutil

# Download the model if it doesn't exist.
# The model 'lid.176.bin' is a pre-trained language identification model from fastText.
MODEL_PATH = "lid.176.bin"

def download_model():
    """Downloads the fastText language identification model if it's not already present."""
    if not Path(MODEL_PATH).exists():
        print(f"Downloading fastText model '{MODEL_PATH}'...")
        import wget
        wget.download("https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin")
        print("Download complete.")

def is_bo(line: str, model: fasttext.FastText):
    """Checks if a line is Tibetan using the fastText model."""
    predictions = model.predict(line, k=1)
    lang_code = predictions[0][0].replace('__label__', '')
    return lang_code == 'bo'

def filter_tibetan_text(input_dir: Path, output_dir: Path, confidence_threshold=0.5):
    """
    Filters files in a directory to keep only those identified as Tibetan.

    Args:
        input_dir (Path): Path to the input directory.
        output_dir (Path): Path to the output directory where Tibetan files will be saved.
        confidence_threshold (float): Minimum proportion of Tibetan lines for a file to be considered Tibetan.
    """
    download_model()
    model = fasttext.load_model(MODEL_PATH)

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    print(f"Processing files in '{input_dir}'...")
    for input_file_path in input_dir.iterdir():
        if input_file_path.is_file():
            print(f"  - Analyzing '{input_file_path.name}'...")
            tibetan_lines = 0
            total_lines = 0
            try:
                with open(input_file_path, 'r', encoding='utf-8') as infile:
                    lines = infile.readlines()
                    total_lines = len(lines)
                    if total_lines == 0:
                        continue

                    for line in lines:
                        line_to_predict = line.strip()
                        if not line_to_predict:
                            continue
                        
                        if is_bo(line_to_predict, model):
                            tibetan_lines += 1
                
                if (tibetan_lines / total_lines) >= confidence_threshold:
                    output_file_path = output_dir / input_file_path.name
                    shutil.copy(input_file_path, output_file_path)
                    print(f"    -> Copied to '{output_file_path}'")
            except Exception as e:
                print(f"Could not process file {input_file_path}. Error: {e}")

    print(f"Tibetan text files have been filtered and saved to '{output_dir}'.")

if __name__ == '__main__':
    line_text_chinese = "我是丹增贡桑，我是地球上最聪明的人。"
    line_text_english = "This is a line in English."
    line_text_tibetan = "བཀྲ་ཤིས་བདེ་ལེགས།"
    line_text_mixed = "བཀྲ་ཤིས་བདེ་ལེགས། This is a line in English."
    download_model()
    model = fasttext.load_model(MODEL_PATH)
    print(is_bo(line_text_chinese, model))
    print(is_bo(line_text_english, model))
    print(is_bo(line_text_tibetan, model))
    print(is_bo(line_text_mixed, model))
