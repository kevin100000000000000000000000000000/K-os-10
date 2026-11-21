# Contributing

## Development workflow

1. Make changes in a focused branch.
2. Run `python3 tests/test_kos_config.py`.
3. Run or review the GitHub Actions ISO build.
4. Report hardware validation only after a tested boot and install.

## Repository rules

- Keep the Debian stable base and AMD64 target reproducible.
- Do not add proprietary game assets or copyrighted media.
- Do not embed API keys or private credentials.
- Use `apt`/APT repositories; do not disable package signature verification.
- Document hardware support based on test evidence, not assumptions.

Pull requests should include build impact, test results, and any new package
dependencies.
