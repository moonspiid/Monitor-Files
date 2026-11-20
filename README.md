# Monitor-Files 📁

<p>
  <img alt="python, 3" src="https://img.shields.io/badge/python-3-3776ab?labelColor=30363d">
  <img alt="dependencies, none" src="https://img.shields.io/badge/dependencies-none-2ea043?labelColor=30363d">
  <img alt="sorts files by extension" src="https://img.shields.io/badge/sorts-by%20file%20type-ff2d8f?labelColor=30363d">
  <img alt="install, none" src="https://img.shields.io/badge/install-none-2ea043?labelColor=30363d">
  <br>
  <img alt="single-file script" src="https://img.shields.io/badge/code-single%20file-1f6feb?labelColor=30363d">
  <img alt="MIT license" src="https://img.shields.io/badge/license-MIT-ea7a15?labelColor=30363d">
</p>

**Point it at a messy folder: every file is moved into a subfolder named after its extension — one Python file, nothing to install.**

<h3 align="center">
  <a href="main.py">→ Download main.py</a>
</h3>

<p align="center">
  One file, standard library only, no package manager and no config.
  <br>
  Works on any folder you own, on any system with Python 3.
</p>

## Contents

- [Why](#why)
- [Quick start](#quick-start)
- [What it does](#what-it-does)
- [How it works](#how-it-works)
- [Good to know](#good-to-know)
- [License](#license)

## Why

Downloads folders fill up with a flat pile of PDFs, screenshots, installers and stray archives. The
usual answer is a big file manager or a subscription app that watches your folders and indexes your
disk. The smaller answer is: sort them once, by type, and be done.

This script does exactly that, in thirty lines you can read before you run it. Nothing runs in the
background, nothing watches anything, nothing is installed.

## Quick start

1. Save [`main.py`](main.py) next to the folder you want to sort.
2. Run it with the folder path: `python main.py /path/to/folder`
3. Open the folder: your files are now grouped in `pdf/`, `jpg/`, `zip/` and so on.

Use `python main.py -h` to see the help.

## What it does

Every file directly inside that folder is moved into a subfolder named after its extension, so
`report.pdf` ends up in `pdf/` and `photo.jpg` in `jpg/`. Subfolders are created when they do not
exist yet, and folders are left alone.

```
Downloads/                    Downloads/
  report.pdf          →           pdf/report.pdf
  photo.jpg                       jpg/photo.jpg
  backup.zip                      zip/backup.zip
  notes.txt                       txt/notes.txt
```

A file whose name has no dot is sorted into a folder named after its whole name, because that is what
splitting on the last dot gives — check the list before running it on something precious.

## How it works

- `os.listdir` walks the folder once.
- `os.path.isfile` skips anything that is already a directory.
- The extension is taken from the last dot in the name; the target folder is created with
  `os.makedirs(..., exist_ok=True)`.
- `shutil.move` puts the file there. No content is read, nothing is rewritten.

That is the whole program: list, test, make the folder, move.

## Good to know

- It only touches the folder you name — one level deep, not recursive. Point it at a parent folder
  and it will only sort the files sitting directly inside it.
- Existing files are never overwritten silently by the script's own logic: `shutil.move` fails on a
  name clash rather than replacing the file, so you will see an error instead of losing data.
- Because it is destructive by nature (files change place), try it on a copy of an important folder
  the first time. There is no undo.
- Nothing is installed and nothing is sent anywhere; it is standard-library Python, start to finish.

## License

[MIT](LICENSE) © 2026 moonspiid — use it, modify it, ship it.
