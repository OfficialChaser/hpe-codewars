# HPE Codewars Solutions

My personal collection of [HPE Codewars](https://hpecodewars.org) solutions from my freshman, sophomore, and junior year of high school (I missed senior year for a tennis tournament). During my freshman year, I didn't place in the novice division---it was more about the experience. During my sophomore year, I led a team of 3 to win the novice division. During my junior year, a friend and I competed in the advanced division but unfortunately didn't place. All years, I competed at the competition site in Roseville, California.

HPE Codewars is a regional in-person coding competition designed to test students' coding knowledge in just three hours. Participants score points by solving problems from the problem packet given out at the beginning of the competition. The competition is split into a novice division and an advanced division.

## How it's organized

Solutions are grouped by year (`2020/`, `2021/`, `2023/`, `2024/`), plus `2024_beta/` and `2025_beta/` for in-progress work.

Each year folder contains solution scripts and input files:

```
2024/
  prob03.py   # solution for problem 3
  input.txt   # puzzle input
```

Some years also include additional input files like `prob3.in`.

## Running a solution

Each script reads from stdin and prints to stdout. From the repo root:

**Unix/WSL:**
```bash
python 2024/prob03.py < 2024/input.txt
```

**Windows PowerShell:**
```powershell
Get-Content 2024\input.txt | python 2024\prob03.py
```

Just Python 3.8+ required, no external packages.
