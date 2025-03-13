```
                                                                ,     ,
██████╗ ██╗ ██████╗██████╗  █████╗ ███████╗ ██████╗██╗██╗      (\____/)
██╔══██╗██║██╔════╝╚════██╗██╔══██╗██╔════╝██╔════╝██║██║       (_oo_)
██████╔╝██║██║      █████╔╝███████║███████╗██║     ██║██║         (O)
██╔═══╝ ██║██║     ██╔═══╝ ██╔══██║╚════██║██║     ██║██║       __||__    \)
██║     ██║╚██████╗███████╗██║  ██║███████║╚██████╗██║██║    []/______\[] /
╚═╝     ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝    / \______/ \/
---------------------------------------->By Kim Schulz<--   /    /__\
                                                           (\   /____\
```

# Image to ASCII Art Converter

<!--toc:start-->
- [Image to ASCII Art Converter](#image-to-ascii-art-converter)
  - [Features](#features)
  - [Dependencies](#dependencies)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Options:](#options)
    - [Examples](#examples)
      - [Convert an image to ASCII:](#convert-an-image-to-ascii)
      - [Convert an image with color:](#convert-an-image-with-color)
      - [Use block characters for better resolution:](#use-block-characters-for-better-resolution)
      - [Apply edge detection with intensity 50:](#apply-edge-detection-with-intensity-50)
      - [Convert old cp437 formattet ascii art to utf8:](#convert-old-cp437-formattet-ascii-art-to-utf8)
  - [License](#license)
  - [Author](#author)
<!--toc:end-->

A command-line tool to convert images (PNG, JPG, etc.) into ASCII art with
optional color, block characters, and edge detection.

## Features

- Convert images to ASCII art with different character sets
- Supports **color output** in the terminal
- **Block character mode** for improved resolution
- **Edge detection** to highlight image details
- **Invert mode** to reverse brightness mapping
- Convert existing ascii/Ansi art between cp437 and UTF-8 encoding

## Dependencies

Ensure you have the following installed:

- Python 3.7+
- Required Python libraries:

  ```sh
  pip install pillow colorama
  ```

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/ascii-art-tool.git
   cd ascii-art-tool
   ```

2. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the tool:

   ```sh
   python pic2ascii.py path/to/image.jpg -w 100 -c
   ```

## Usage

Run the script with an image file and optional parameters:

```sh
python pic2ascii.py <image_path> [options]
```

### Options

- `-w, --width <int>`        → Set the ASCII output width (default: 100)
- `-c, --color`              → Enable colored ASCII output
- `-b, --block`              → Use block characters instead of normal ASCII
- `-i, --invert`             → Invert brightness mapping
- `-e, --edge <0-100>`       → Apply edge detection (intensity 0-100)
- `-f, --format <direction>` → Select format direction to convert between.\
                             Possible directions are:\
                             `cp437-to-utf8` and `utf8-to-cp437`.\
                             Input file is given as alternative to the `<image>`\
                             and can be in either utf8 or cp437 format.
- `-o, --output <out-file>`   → the output filename if converting between formats

### Examples

#### Convert an image to ASCII

```sh
python pic2ascii.py image.png -w 120
```

#### Convert an image with color

```sh
python pic2ascii.py image.jpg -w 80 -c
```

#### Use block characters for better resolution

```sh
python pic2ascii.py image.png -w 100 -b
```

#### Apply edge detection with intensity 50

```sh
python pic2ascii.py image.jpg -w 100 -e 50
```

#### Convert old cp437 formattet ascii art to utf8

```sh
python pic2ascii.py image.ans -f cp437-to-utf8 -o image.utf8
```

## License

This project is licensed under the MIT License.

## Author

**Kim Schulz** / (<https://schulz.dk>)
