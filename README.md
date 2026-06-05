# HPE Codewars Solutions

My personal collection of [HPE Codewars](https://codewars.hpe.com/) solutions from my freshman, sophomore, and junior year of high school (I missed senior year for a tennis tournament). All written in Python, and working through these competitions genuinely helped me sharpen my problem solving skills and learn to write more optimized code.

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
