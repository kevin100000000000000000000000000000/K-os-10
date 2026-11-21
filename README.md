# KOS 1.0

**KOS** is a Debian Stable-based, AMD64 desktop Linux distribution for Intel and AMD
desktop computers. It provides a custom XFCE desktop with a cyan liquid-glass
theme, Calamares graphical installation, everyday desktop applications, gaming
compatibility tools, and reproducible Live ISO builds.

## Status

This repository contains the complete source/configuration needed to build KOS
1.0. It does not claim physical-hardware validation that has not been performed.

## Downloads

GitHub Actions builds `KOS-1.0-amd64.iso` and publishes it as a workflow artifact.
Each build also publishes `SHA256SUMS`.

## Highlights

- Debian Stable/AMD64 Live and installation system
- UEFI and legacy BIOS boot
- Calamares graphical installer
- XFCE desktop with custom KOS appearance
- Firefox, LibreOffice, media/PDF tools, archives, development tools
- KOS Store and Update Center
- Wine, Lutris, Winetricks, Steam installer support, Vulkan and Mesa
- Configurable OpenAI-compatible and local AI interface
- UFW firewall, sudo, credential-safe application storage

See [INSTALL.md](INSTALL.md), [BUILD.md](BUILD.md), [HARDWARE.md](HARDWARE.md),
and [SECURITY.md](SECURITY.md).