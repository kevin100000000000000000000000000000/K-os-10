#!/usr/bin/python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def require(path):
    target = ROOT / path
    assert target.is_file(), f"Required file missing: {path}"
    return target

def test_required_repository_files():
    for path in [
        "README.md", "INSTALL.md", "BUILD.md", "SECURITY.md",
        "CONTRIBUTING.md", "HARDWARE.md", "CHANGELOG.md",
        "auto/config", ".github/workflows/build-iso.yml",
        "config/package-lists/kos.list.chroot",
        "config/hooks/live/0990-kos.hook.chroot",
        "config/includes.chroot/etc/calamares/settings.conf",
    ]:
        require(path)

def test_amd64_and_stable():
    config = require("auto/config").read_text()
    assert "--distribution bookworm" in config
    assert "--architecture amd64" in config
    assert "--binary-images iso-hybrid" in config
    assert "grub-pc,grub-efi" in config

def test_package_configuration():
    packages = require("config/package-lists/kos.list.chroot").read_text()
    required = [
        "xfce4", "calamares", "firefox-esr", "git", "ufw",
        "mesa-vulkan-drivers", "lutris", "wine", "winetricks",
        "pipewire", "bluez", "cups", "python3-gi",
    ]
    missing = [package for package in required if package not in packages]
    assert not missing, f"Missing package entries: {missing}"

def test_desktop_applications():
    for name in [
        "kos-home", "kos-browser", "kos-ai", "kos-youtube",
        "kos-store", "kos-update", "kos-monitor", "kos-installer",
    ]:
        require(f"config/includes.chroot/usr/share/applications/{name}.desktop")

def test_scripts_are_real_executables():
    for name in ["kos-home", "kos-store", "kos-update", "kos-monitor", "kos-ai"]:
        target = require(f"config/includes.chroot/usr/local/bin/{name}")
        text = target.read_text()
        assert text.startswith("#!/usr/bin/python3") or text.startswith("#!/bin/python3")

def test_installer_has_destructive_boundary():
    partition = require("config/includes.chroot/etc/calamares/modules/partition.conf").read_text()
    settings = require("config/includes.chroot/etc/calamares/settings.conf").read_text()
    assert "allowManualPartitioning: true" in partition
    assert "partition" in settings

if __name__ == "__main__":
    tests = [value for name, value in globals().items() if name.startswith("test_")]
    for test in tests:
        test()
    print(f"PASS: {len(tests)} KOS configuration test groups")
