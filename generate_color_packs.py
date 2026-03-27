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
from urllib.parse import quote

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
    original_dir = Path("Color Packs/Original")
    icon_files = sorted([file.name for file in original_dir.glob("*.svg")])
    # Preserve color pack definition order so index matches README ordering.
    sorted_packs = list(config["colorPacks"].items())
    github_raw_base = (
        "https://raw.githubusercontent.com/JamsRepos/unraid-animated-svgs/refs/heads/master"
    )

    packs_payload = [
        {
            "name": pack_info["name"],
            "description": pack_info["description"],
            "color": pack_info["color"],
        }
        for _, pack_info in sorted_packs
    ]

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
            max-width: 1440px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            color: #333;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #666;
            margin-bottom: 30px;
        }
        .color-packs {
            display: grid;
            grid-template-columns: 1fr;
            gap: 16px;
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
        .pack-header {
            display: flex;
            gap: 12px;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }
        .pack-title-group {
            display: flex;
            align-items: center;
            gap: 12px;
        }
        .pack-actions {
            display: flex;
            align-items: center;
            gap: 8px;
        }
        .color-sample {
            width: 60px;
            height: 40px;
            border-radius: 8px;
            border: 2px solid #ddd;
        }
        .icon-preview {
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
            margin-top: 12px;
        }
        .icon-preview.is-empty {
            min-height: 56px;
        }
        .pack-controls {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-top: 10px;
        }
        .load-all-button {
            border: 1px solid #cbd5e1;
            background: #f8fafc;
            color: #1f2937;
            border-radius: 6px;
            padding: 6px 10px;
            font-size: 12px;
            cursor: pointer;
        }
        .load-all-button:hover {
            background: #eef2ff;
        }
        .icon-count {
            color: #6b7280;
            font-size: 12px;
        }
        .loading-hint {
            color: #6b7280;
            font-size: 13px;
            margin-top: 8px;
        }
        .icon-button {
            width: 50px;
            height: 50px;
            border-radius: 8px;
            border: 1px solid #ddd;
            background: #fff;
            padding: 2px;
            cursor: pointer;
            transition: transform 0.1s ease, box-shadow 0.1s ease;
        }
        .icon-button:hover {
            transform: translateY(-1px);
            box-shadow: 0 2px 8px rgba(0,0,0,0.14);
        }
        .icon-button img {
            width: 50px;
            height: 50px;
            pointer-events: none;
        }
        .download-link {
            display: inline-block;
            background: #007bff;
            color: white;
            padding: 8px 16px;
            text-decoration: none;
            border-radius: 5px;
            font-size: 14px;
        }
        .download-link:hover {
            background: #0056b3;
        }
        .copy-hint {
            color: #555;
            font-size: 13px;
            margin-top: 8px;
        }
        .copied-toast {
            position: fixed;
            right: 18px;
            bottom: 18px;
            background: #111827;
            color: #fff;
            padding: 10px 14px;
            border-radius: 8px;
            font-size: 13px;
            opacity: 0;
            transform: translateY(10px);
            transition: opacity 0.15s ease, transform 0.15s ease;
        }
        .copied-toast.visible {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Unraid Animated SVGs - Color Pack Preview</h1>
        <p class="subtitle">Click any icon to copy its raw GitHub URL.</p>
        <div class="color-packs">
"""

    for _, pack_info in sorted_packs:
        color = pack_info["color"]
        pack_name = pack_info["name"]
        encoded_pack_name = quote(pack_name)
        download_url = f"{github_raw_base}/Color%20Packs/{encoded_pack_name}/"
        html_content += f"""
            <div class="color-pack" data-pack-name="{pack_name}">
                <div class="pack-header">
                    <div class="pack-title-group">
                        <div class="color-sample" style="background-color: {color}"></div>
                        <div>
                            <h2>{pack_name}</h2>
                            <p>{pack_info['description']} ({color})</p>
                        </div>
                    </div>
                    <div class="pack-actions">
                        <a href="{download_url}" class="download-link" target="_blank" rel="noopener noreferrer">&#x2B07; Download Pack</a>
                    </div>
                </div>
                <div class="icon-preview is-empty" data-icon-container></div>
                <div class="pack-controls">
                    <button class="load-all-button" data-load-all type="button">Load all icons</button>
                    <span class="icon-count" data-icon-count>0 of 0 loaded</span>
                </div>
                <p class="loading-hint">A small preview loads first for speed.</p>
                <p class="copy-hint">Click any icon to copy its direct URL.</p>
            </div>
"""

    html_content += """
        </div>
    </div>
    <div class="copied-toast" id="copiedToast">Copied icon URL</div>
    <script>
        const GITHUB_RAW_BASE = __GITHUB_RAW_BASE__;
        const ICON_FILES = __ICON_FILES__;
        const PREVIEW_ICON_COUNT = 12;
        const CHUNK_SIZE = 12;
        const copiedToast = document.getElementById('copiedToast');

        function showCopiedToast(message) {
            copiedToast.textContent = message;
            copiedToast.classList.add('visible');
            window.clearTimeout(showCopiedToast._timer);
            showCopiedToast._timer = window.setTimeout(() => {
                copiedToast.classList.remove('visible');
            }, 1400);
        }

        async function copyToClipboard(text) {
            try {
                await navigator.clipboard.writeText(text);
                showCopiedToast('Copied icon URL');
            } catch (err) {
                // Fallback for contexts where clipboard API is unavailable.
                const helper = document.createElement('textarea');
                helper.value = text;
                helper.setAttribute('readonly', '');
                helper.style.position = 'fixed';
                helper.style.opacity = '0';
                document.body.appendChild(helper);
                helper.select();
                document.execCommand('copy');
                document.body.removeChild(helper);
                showCopiedToast('Copied icon URL');
            }
        }

        function buildIconButton(packName, iconFile) {
            const iconLabel = iconFile.replace('.svg', '');
            const encodedPack = encodeURIComponent(packName);
            const encodedIcon = encodeURIComponent(iconFile);
            const rawUrl = `${GITHUB_RAW_BASE}/Color%20Packs/${encodedPack}/${encodedIcon}`;
            const localSrc = `Color Packs/${packName}/${iconFile}`;

            const button = document.createElement('button');
            button.className = 'icon-button';
            button.title = `Copy URL: ${iconLabel}`;
            button.setAttribute('data-url', rawUrl);
            button.addEventListener('click', () => copyToClipboard(rawUrl));

            const img = document.createElement('img');
            img.alt = iconLabel;
            img.loading = 'lazy';
            img.decoding = 'async';
            img.src = localSrc;
            button.appendChild(img);
            return button;
        }

        function updateIconCount(packCard, loadedCount) {
            const countEl = packCard.querySelector('[data-icon-count]');
            if (!countEl) {
                return;
            }
            countEl.textContent = `${loadedCount} of ${ICON_FILES.length} loaded`;
        }

        function renderPackIcons(packCard, limit = PREVIEW_ICON_COUNT) {
            if (packCard.dataset.iconsRendered === 'true' && limit <= Number(packCard.dataset.iconsLoaded || 0)) {
                return;
            }
            const packName = packCard.dataset.packName;
            const container = packCard.querySelector('[data-icon-container]');
            const loadedSoFar = Number(packCard.dataset.iconsLoaded || 0);
            const targetCount = Math.min(limit, ICON_FILES.length);

            if (loadedSoFar >= targetCount) {
                return;
            }

            const fragment = document.createDocumentFragment();
            ICON_FILES.slice(loadedSoFar, targetCount).forEach((iconFile) => {
                fragment.appendChild(buildIconButton(packName, iconFile));
            });
            container.appendChild(fragment);
            container.classList.remove('is-empty');
            packCard.dataset.iconsLoaded = String(targetCount);
            packCard.dataset.iconsRendered = String(targetCount >= ICON_FILES.length);
            updateIconCount(packCard, targetCount);
        }

        function renderAllIcons(packCard) {
            const loadButton = packCard.querySelector('[data-load-all]');
            if (loadButton) {
                loadButton.disabled = true;
                loadButton.textContent = 'Loading...';
            }

            const step = () => {
                const loaded = Number(packCard.dataset.iconsLoaded || 0);
                if (loaded >= ICON_FILES.length) {
                    if (loadButton) {
                        loadButton.textContent = 'All icons loaded';
                    }
                    return;
                }
                renderPackIcons(packCard, loaded + CHUNK_SIZE);
                window.requestAnimationFrame(step);
            };

            step();
        }

        const packCards = Array.from(document.querySelectorAll('.color-pack'));
        const packObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) {
                    return;
                }
                renderPackIcons(entry.target);
                observer.unobserve(entry.target);
            });
        }, { rootMargin: '300px 0px' });

        packCards.forEach((card, index) => {
            updateIconCount(card, 0);
            const loadAllButton = card.querySelector('[data-load-all]');
            if (loadAllButton) {
                loadAllButton.addEventListener('click', () => renderAllIcons(card));
            }
            if (index < 1) {
                renderPackIcons(card, PREVIEW_ICON_COUNT);
                return;
            }
            packObserver.observe(card);
        });
    </script>
</body>
</html>
"""
    html_content = (
        html_content
        .replace("__GITHUB_RAW_BASE__", json.dumps(github_raw_base))
        .replace("__ICON_FILES__", json.dumps(icon_files))
        .replace("__PACKS__", json.dumps(packs_payload))
    )

    # GitHub Pages serves index.html at the repository root by default.
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    print("Created GitHub Pages entry point: index.html")

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
    print("Open 'index.html' to see a preview of all color packs.")

if __name__ == "__main__":
    main()