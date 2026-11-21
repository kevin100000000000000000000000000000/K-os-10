# Building KOS 1.0

## Reproducible build

KOS uses Debian Live Build, Debian `bookworm` packages, and a custom live-hook.
The canonical build is the GitHub Actions container workflow.

Requirements for an Ubuntu/Debian host:

```sh
sudo apt-get update
sudo apt-get install live-build debootstrap xorriso squashfs-tools \
  grub-pc-bin grub-efi-amd64-bin grub-efi-amd64-signed mtools dosfstools
sudo lb clean
sudo lb config
sudo lb build
```

For a privileged container build:

```sh
docker run --rm --privileged -v "$PWD:/build" -w /build debian:bookworm \
  bash -lc 'apt-get update && apt-get install live-build xorriso \
  grub-pc-bin grub-efi-amd64-bin grub-efi-amd64-signed mtools dosfstools &&
  ./auto/config && lb clean && lb config && lb build'
```

Live Build writes binary-hybrid ISO output into the repository build directory.
Use `sha256sum` to produce and verify `SHA256SUMS`.

## CI

Push or open a pull request to run `.github/workflows/build-iso.yml`. The
workflow validates source configuration, builds an AMD64 ISO, generates
checksums, and uploads the ISO and live-build log as a 30-day artifact.
