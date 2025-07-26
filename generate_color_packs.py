#!/usr/bin/env python3
"""
Color Pack Generator for Unraid Animated SVGs (Clean Structure)

This script generates multiple color variations of the SVG icons based on
the color packs defined in color-packs.json for the clean directory structure.
"""

import json
import os
import re
import shutil
from pathlib import Path

def load_color_packs():
    """Load color packs from the configuration file."""
    with open('color-packs.json', 'r') as f:
        return json.load(f)

def get_original_colors():
    """Get the original colors used in the SVGs."""
    return [
        "#D52727",
        "#FE8A30",
        "#F3632D"
    ]

def replace_colors_in_svg(svg_content, new_color):
    """Replace all original colors in SVG content with the new color."""
    original_colors = get_original_colors()

    for old_color in original_colors:
        # Replace the color in fill attributes
        svg_content = re.sub(
            rf'fill="{re.escape(old_color)}"',
            f'fill="{new_color}"',
            svg_content
        )
        # Also replace in stroke attributes if they exist
        svg_content = re.sub(
            rf'stroke="{re.escape(old_color)}"',
            f'stroke="{new_color}"',
            svg_content
        )
    return svg_content

def generate_color_variants():
    """Generate color variants for all SVG files."""
    config = load_color_packs()

    # Get all SVG files from the Original color pack
    original_dir = 'Color Packs/Original'
    svg_files = []

    if os.path.exists(original_dir):
        for file in os.listdir(original_dir):
            if file.endswith('.svg'):
                svg_files.append(file)

    print(f"Found {len(svg_files)} SVG files to process")

    # Process each color pack
    for pack_id, pack_info in config['colorPacks'].items():
        print(f"\nProcessing color pack: {pack_info['name']}")

        # Skip the Original pack as it's our source
        if pack_id == 'original':
            continue

        # Get the single color for this pack
        new_color = pack_info['color']

        # Create output directory for this color pack
        output_dir = f"Color Packs/{pack_info['name']}"
        os.makedirs(output_dir, exist_ok=True)

        # Process each SVG file
        for svg_file in svg_files:
            input_path = os.path.join(original_dir, svg_file)
            output_path = os.path.join(output_dir, svg_file)

            try:
                # Read the original SVG
                with open(input_path, 'r', encoding='utf-8') as f:
                    svg_content = f.read()

                # Replace colors
                new_svg_content = replace_colors_in_svg(svg_content, new_color)

                # Write the new SVG
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(new_svg_content)

                print(f"  Generated: {svg_file}")

            except Exception as e:
                print(f"  Error processing {input_path}: {e}")

def create_color_pack_preview():
    """Create a preview HTML file showing all color packs."""
    config = load_color_packs()

    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unraid Animated SVGs - Color Pack Preview</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            margin: 0;
            padding: 20px;
            background: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        .color-packs {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .color-pack {
            background: white;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .color-pack h2 {
            margin: 0 0 10px 0;
            color: #333;
        }
        .color-pack p {
            margin: 0 0 15px 0;
            color: #666;
            font-size: 14px;
        }
        .color-sample {
            width: 60px;
            height: 40px;
            border-radius: 8px;
            border: 2px solid #ddd;
            margin-bottom: 15px;
        }
        .icon-preview {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }
        .icon-preview img {
            width: 50px;
            height: 50px;
            border-radius: 8px;
            border: 1px solid #ddd;
        }
        .download-link {
            display: inline-block;
            background: #007bff;
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
            margin-top: 10px;
        }
        .download-link:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Unraid Animated SVGs - Color Pack Preview</h1>
        <div class="color-packs">
"""

    for pack_id, pack_info in config['colorPacks'].items():
        color = pack_info['color']
        html_content += f"""
            <div class="color-pack">
                <h2>{pack_info['name']}</h2>
                <p>{pack_info['description']}</p>
                <div class="color-sample" style="background-color: {color}"></div>
                <div class="icon-preview">
                    <img src="Color Packs/{pack_info['name']}/audio_always.svg" alt="Audio icon">
                    <img src="Color Packs/{pack_info['name']}/cloud_always.svg" alt="Cloud icon">
                    <img src="Color Packs/{pack_info['name']}/backup_always.svg" alt="Backup icon">
                </div>
                <a href="Color Packs/{pack_info['name']}/" class="download-link">Download Pack</a>
            </div>
"""

    html_content += """
        </div>
    </div>
</body>
</html>
"""

    with open('color-pack-preview.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Created color pack preview: color-pack-preview.html")

def main():
    """Main function to run the color pack generation."""
    print("Unraid Animated SVGs - Color Pack Generator (Clean Structure)")
    print("=" * 60)

    # Generate color variants
    generate_color_variants()

    # Create preview
    create_color_pack_preview()

    print("\n" + "=" * 60)
    print("Color pack generation complete!")
    print("Check the 'Color Packs' directory for all variants.")
    print("Open 'color-pack-preview.html' to see a preview of all color packs.")

if __name__ == "__main__":
    main()