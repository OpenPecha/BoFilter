# BoFilter

## Installation
<details>
  <summary>From pip</summary>

```bash
pip install bofilter
```
</details>

<details>
  <summary>From GitHub</summary>

```bash
pip install git+https://github.com/OpenPecha/BoFilter.git
```
</details>

<details>
  <summary>From source</summary>

```bash
git clone https://github.com/OpenPecha/BoFilter.git
cd BoFilter
pip install -e .
```
</details>

## Usage

This example demonstrates how to filter Tibetan text files from a directory.



### Using `fast_text`
```python
from pathlib import Path
from bofilter.fast_text import filter_tibetan_text

input_dir = Path("input_texts")
output_dir = Path("tibetan_texts")

# Filter the files
filter_tibetan_text(input_dir, output_dir)

print("Files filtered using fast_text are in:", output_dir)
for f in sorted(output_dir.iterdir()):
    print(f"- {f.name}")
```

### Using `langid`
```python
from pathlib import Path
from bofilter.lang_id import filter_tibetan_text_langid

input_dir = Path("input_texts")
output_dir = Path("tibetan_texts")
i

# Filter the files
filter_tibetan_text_langid(input_dir, output_dir)

print("Files filtered using langid are in:", output_dir)
for f in sorted(output_dir.iterdir()):
    print(f"- {f.name}")

```

## Implementation
This package provides two modules for language identification, each using a different library:
- The `fast_text` module uses Facebook's [fastText](https://fasttext.cc/) library.
- The `lang_id` module uses the [langid](https://github.com/saffsd/langid.py) library.

Both modules follow a similar logic: they read a document line by line and identify whether each line is Tibetan. The module then calculates the percentage of Tibetan lines in the entire document. If this percentage exceeds a specified confidence threshold, the document is classified as Tibetan and saved to the output directory.

### Comparison
| Feature      | `fast_text`                                       | `langid`                                    |
|--------------|---------------------------------------------------|---------------------------------------------|
| **Accuracy** | Generally higher, especially on noisy text.       | Good, but can be less accurate on short text. |
| **Speed**    | Slower due to the larger model size.              | Faster and more lightweight.                |
| **Model**    | Requires downloading a large pre-trained model. | Comes with a built-in, lightweight model.   |
| **Use Case** | Ideal for high accuracy on diverse text.          | Suitable for fast, general-purpose filtering. |

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## How to get help
* File an issue.
* Email us at openpecha[at]gmail.com.
* Join our [discord](https://discord.com/invite/7GFpPFSTeA).

## License
[MIT](LICENSE.md)
