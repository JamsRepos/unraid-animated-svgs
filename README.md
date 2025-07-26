# Unraid Animated SVGs

A collection of animated SVG icons designed specifically for the **FolderView plugin** on Unraid server dashboards. Simply paste the URL of any icon to add beautiful animated icons to your FolderView dashboard.

## Features

- **31 Animated Icons**: Covering common server applications and services
- **Two Animation Styles**:
  - **Always Animate**: Icons that continuously animate (suffix: `_always.svg`)
  - **Animate on Hover**: Icons that animate only when hovered over (suffix: `_hover.svg`)
- **10 Color Packs**: Multiple color themes with uniform single-color design
- **High Quality**: Vector graphics that scale perfectly at any size
- **Lightweight**: Small file sizes for fast loading

## Quick Start for FolderView

1. **Choose your preferred color pack** from the examples below
2. **Copy the URL** of any icon you want to use
3. **Paste the URL** into your FolderView plugin configuration
4. **Done!** Your animated icon will appear on your dashboard

## Color Packs

Choose from 10 different color themes, each using a single uniform color for consistency:

### 🎨 Available Color Packs

| Pack | Color | Description | Example Icons |
|------|-------|-------------|---------------|
| **Original** | #D52727 | Classic red theme | ![Audio](Color%20Packs/Original/audio_always.svg) ![Cloud](Color%20Packs/Original/cloud_always.svg) ![Plex](Color%20Packs/Original/plex_always.svg) |
| **Ocean Blue** | #2563EB | Cool blue tones for a modern look | ![Audio](Color%20Packs/Ocean%20Blue/audio_always.svg) ![Cloud](Color%20Packs/Ocean%20Blue/cloud_always.svg) ![Plex](Color%20Packs/Ocean%20Blue/plex_always.svg) |
| **Forest Green** | #059669 | Natural green tones | ![Audio](Color%20Packs/Forest%20Green/audio_always.svg) ![Cloud](Color%20Packs/Forest%20Green/cloud_always.svg) ![Plex](Color%20Packs/Forest%20Green/plex_always.svg) |
| **Royal Purple** | #7C3AED | Elegant purple and violet tones | ![Audio](Color%20Packs/Royal%20Purple/audio_always.svg) ![Cloud](Color%20Packs/Royal%20Purple/cloud_always.svg) ![Plex](Color%20Packs/Royal%20Purple/plex_always.svg) |
| **Teal Ocean** | #0D9488 | Fresh teal and cyan tones | ![Audio](Color%20Packs/Teal%20Ocean/audio_always.svg) ![Cloud](Color%20Packs/Teal%20Ocean/cloud_always.svg) ![Plex](Color%20Packs/Teal%20Ocean/plex_always.svg) |
| **Rose Pink** | #DB2777 | Soft pink and rose tones | ![Audio](Color%20Packs/Rose%20Pink/audio_always.svg) ![Cloud](Color%20Packs/Rose%20Pink/cloud_always.svg) ![Plex](Color%20Packs/Rose%20Pink/plex_always.svg) |
| **Modern Gray** | #374151 | Sophisticated gray tones | ![Audio](Color%20Packs/Modern%20Gray/audio_always.svg) ![Cloud](Color%20Packs/Modern%20Gray/cloud_always.svg) ![Plex](Color%20Packs/Modern%20Gray/plex_always.svg) |
| **Sunny Yellow** | #D97706 | Bright and cheerful yellow tones | ![Audio](Color%20Packs/Sunny%20Yellow/audio_always.svg) ![Cloud](Color%20Packs/Sunny%20Yellow/cloud_always.svg) ![Plex](Color%20Packs/Sunny%20Yellow/plex_always.svg) |
| **Deep Indigo** | #4338CA | Rich indigo and blue tones | ![Audio](Color%20Packs/Deep%20Indigo/audio_always.svg) ![Cloud](Color%20Packs/Deep%20Indigo/cloud_always.svg) ![Plex](Color%20Packs/Deep%20Indigo/plex_always.svg) |
| **Emerald Green** | #047857 | Vibrant emerald green tones | ![Audio](Color%20Packs/Emerald%20Green/audio_always.svg) ![Cloud](Color%20Packs/Emerald%20Green/cloud_always.svg) ![Plex](Color%20Packs/Emerald%20Green/plex_always.svg) |

## 📁 Directory Structure

```
Color Packs/
├── Original/
│   ├── audio_always.svg
│   ├── audio_hover.svg
│   ├── backup_always.svg
│   ├── backup_hover.svg
│   └── ... (all icons with _always and _hover variants)
├── Ocean Blue/
│   ├── audio_always.svg
│   ├── audio_hover.svg
│   └── ... (all icons)
└── ... (other color packs)
```

## Icons Included

### Server Applications
- **Audio** - Audio streaming services
- **Backup** - Backup and sync applications
- **Cloud** - Cloud storage services
- **Database** - Database applications
- **Downloads** - Download managers
- **Network** - Network monitoring tools
- **Security** - Security and firewall applications
- **Settings** - System configuration tools

### Media & Entertainment
- **Multimedia** - General media applications
- **Multimedia Alternate** - Alternative media icon
- **Music** - Music streaming services
- **Plex** - Plex Media Server
- **Gaming** - Gaming applications

### Development & Tools
- **Code** - Development environments
- **Control** - System control panels
- **Dash** - Dashboard applications
- **Dependencies** - Package managers
- **Productivity** - Productivity tools

### Network & Communication
- **Home Automation** - Smart home applications
- **Home WiFi** - WiFi management tools
- **NZB** - Usenet applications
- **Pirate** - Torrent applications
- **Torrent** - BitTorrent clients
- **VPN** - VPN services
- **World** - Web applications

### Monitoring & Analytics
- **Binoculars** - Monitoring tools
- **Books** - Documentation applications
- **Eye** - Surveillance applications
- **Grafana** - Grafana dashboards
- **Search** - Search applications
- **Ship** - Container applications

## Usage Examples

### FolderView Plugin Configuration

Simply copy and paste the URL of any icon into your FolderView plugin:

**Ocean Blue Audio (Always Animate):**
```
https://raw.githubusercontent.com/yourusername/unraid-animated-svgs/main/Color%20Packs/Ocean%20Blue/audio_always.svg
```

**Forest Green Plex (Hover Animate):**
```
https://raw.githubusercontent.com/yourusername/unraid-animated-svgs/main/Color%20Packs/Forest%20Green/plex_hover.svg
```

**Royal Purple Backup (Always Animate):**
```
https://raw.githubusercontent.com/yourusername/unraid-animated-svgs/main/Color%20Packs/Royal%20Purple/backup_always.svg
```

### URL Format

Replace `yourusername` with your actual GitHub username in the URLs above.

## Animation Styles

- **`_always.svg`**: Icons that continuously animate - perfect for active services
- **`_hover.svg`**: Icons that animate only when you hover over them - great for static links

## Customization

### Creating Custom Color Packs

1. **Edit `color-packs.json`** to add your custom color scheme
2. **Run the generator**:
   ```bash
   python generate_color_packs.py
   ```
3. **Your new color pack** will be generated in the `Color Packs/` directory

### Color Pack Configuration

Each color pack defines a single color for uniform appearance:

```json
{
  "name": "Custom Theme",
  "description": "My custom color scheme",
  "color": "#FF0000"
}
```

## Contributing

1. **Fork the repository**
2. **Create a feature branch**
3. **Add your changes**
4. **Submit a pull request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

If you have questions or need help:
- Open an issue on GitHub
- Check the examples above for visual reference
- Review the color pack configuration for customization options

---

**Enjoy your beautifully animated Unraid FolderView dashboard! 🎉**
