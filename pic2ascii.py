import argparse
import os
from PIL import Image, ImageFilter
from colorama import init

# ASCII character sets
ASCII_CHARS = "@%#*+=-:. "
BLOCK_CHARS = "█▓▒░ ▄▀"  # Includes half-block characters


# Initialize colorama
init(autoreset=True)


def resize_image(image, new_width=100):
    """Resize image to maintain aspect ratio in ASCII."""
    width, height = image.size
    aspect_ratio = height / width * 0.55  # Adjust for font aspect ratio
    new_height = int(new_width * aspect_ratio)
    return image.resize((new_width, new_height))


def image_to_grayscale(image):
    """Convert image to grayscale."""
    return image.convert("L")


def map_pixels_to_ascii(image, char_set, invert):
    """Convert image pixels to ASCII characters."""
    pixels = list(image.getdata())

    # Reverse character set if invert mode is enabled
    if invert:
        char_set = char_set[::-1]

    # Ensure Unicode characters provide a proper gradient
    if len(char_set) < 10:
        print("Warning: Character set might not provide a good gradient.")

    ascii_chars = [
        char_set[int((pixel / 255) * (len(char_set) - 1))] for pixel in pixels
    ]
    return ascii_chars


def format_ascii(ascii_chars, width):
    """Format ASCII characters into a 2D list for proper indexing."""
    return [ascii_chars[i : i + width] for i in range(0, len(ascii_chars), width)]


def add_color(image, ascii_grid):
    """Add color to ASCII output using terminal colors."""
    colored_ascii = []
    for y, row in enumerate(ascii_grid):
        colored_row = []
        for x, char in enumerate(row):
            r, g, b = image.convert("RGB").getpixel((x, y))
            color = f"\033[38;2;{r};{g};{b}m"
            colored_row.append(color + char)
        colored_ascii.append("".join(colored_row))
    return "\n".join(colored_ascii)


def apply_edge_detection(image, intensity):
    """Apply edge detection to the image based on the given intensity."""
    # Normalize intensity to a range suitable for edge detection
    factor = intensity / 100.0
    return image.filter(ImageFilter.FIND_EDGES).point(lambda p: p * factor)


def convert_image_to_ascii(
    image_path,
    width=100,
    use_color=False,
    block_mode=False,
    invert=False,
    edge_intensity=0,
):
    """Main function to process image and return ASCII output."""
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error loading image: {e}")
        return

    image = resize_image(image, width)
    if edge_intensity > 0:
        image = apply_edge_detection(image, edge_intensity)
    gray_image = image_to_grayscale(image)

    if block_mode:
        char_set = BLOCK_CHARS
    else:
        char_set = ASCII_CHARS

    ascii_chars = map_pixels_to_ascii(gray_image, char_set, invert)
    ascii_grid = format_ascii(ascii_chars, width)

    if use_color:
        ascii_output = add_color(image, ascii_grid)
    else:
        ascii_output = "\n".join("".join(row) for row in ascii_grid)

    print(ascii_output.encode("utf-8", "replace").decode("utf-8"))


class CustomArgumentParser(argparse.ArgumentParser):
    def format_help(self):
        ascii_header = r"""
                                                                ,     ,
██████╗ ██╗ ██████╗██████╗  █████╗ ███████╗ ██████╗██╗██╗      (\____/)
██╔══██╗██║██╔════╝╚════██╗██╔══██╗██╔════╝██╔════╝██║██║       (_oo_)
██████╔╝██║██║      █████╔╝███████║███████╗██║     ██║██║         (O)
██╔═══╝ ██║██║     ██╔═══╝ ██╔══██║╚════██║██║     ██║██║       __||__    \)
██║     ██║╚██████╗███████╗██║  ██║███████║╚██████╗██║██║    []/______\[] /
╚═╝     ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝╚═╝    / \______/ \/
---------------------------------------->By Kim Schulz<--   /    /__\
                                                           (\   /____\
"""
        return ascii_header + "\n" + super().format_help()


def main():
    """Parse command-line arguments and run the conversion."""
    parser = CustomArgumentParser(description="Convert an image to ASCII art.")
    parser.add_argument("image", help="Path to the input image file")
    parser.add_argument(
        "-w",
        "--width",
        type=int,
        default=100,
        help="Width of ASCII output (default: 100)",
    )
    parser.add_argument(
        "-e",
        "--edge",
        type=int,
        choices=range(0, 101),
        metavar="[0-100]",
        default=0,
        help="Apply edge detection with intensity from 0 to 100 (default: 0)",
    )
    parser.add_argument(
        "-c", "--color", action="store_true", help="Enable color output"
    )
    parser.add_argument(
        "-b",
        "--block",
        action="store_true",
        help="Use block characters instead of normal ASCII",
    )

    parser.add_argument(
        "-i", "--invert", action="store_true", help="Invert ASCII brightness mapping"
    )

    args = parser.parse_args()

    if not os.path.exists(args.image):
        print("Error: File not found.")
        return

    convert_image_to_ascii(args.image, args.width, args.color, args.block, args.invert)


if __name__ == "__main__":
    main()
