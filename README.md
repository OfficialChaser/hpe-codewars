# Advent of Code Solutions
[](https://github.com/OfficialChaser/advent-of-code#advent-of-code-solutions)
My personal collection of [Advent of Code](https://adventofcode.com/) solutions from previous years, all written in Python. Working through these puzzles has helped me sharpen my problem solving skills and learn to optimize my solutions.

## How it's organized
[](https://github.com/OfficialChaser/advent-of-code#how-its-organized)
Solutions are grouped by year folders like `2020/`, `2021/`, `2023/`, `2024/`, plus beta years `2024_beta/` and `2025_beta/`.

Each year folder contains Python solution scripts and input files. Most scripts follow the naming pattern:

```
probXX.py   # solution script for day/problem XX
```

Puzzle inputs are typically stored as:

```
input.txt
```

Some years include additional input files such as `prob3.in`.

## Running a solution
[](https://github.com/OfficialChaser/advent-of-code#running-a-solution)
Each script reads from stdin and prints to stdout. From the repo root:

**Unix/WSL:**

```
python 2024/prob03.py < 2024/input.txt
```

**Windows PowerShell:**

```
Get-Content 2024\input.txt | python 2024\prob03.py
```

Just Python 3.8+ required, no external packages.

## Repository layout
- `2020/` — Advent of Code 2020 solutions
- `2021/` — Advent of Code 2021 solutions
- `2023/` — Advent of Code 2023 solutions
- `2024/` — Advent of Code 2024 solutions
- `2024_beta/` — beta or in-progress 2024 solutions
- `2025_beta/` — beta or in-progress 2025 solutions

