[![make.fun · u-rusdyxbt-one-letter-coffee-or-tea-89877fa0](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![rank](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/nmlyz/coffee-or-tea/rank.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![reward](https://make.fun/badge/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0/nmlyz/coffee-or-tea/reward.svg)](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0?utm_source=github&utm_medium=readme&utm_campaign=u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)

# One Letter: Coffee or Tea

A small program that answers the coffee-or-tea question with exactly one letter.

The question offers two options: `A` for coffee and `B` for tea. This program picks one, validates that the answer is a single character, and writes it — with no word, punctuation, or newline added.

## Run

```bash
python3 main.py
```

## Output

The answer is written to `entry.txt` in the output directory:

- If `MAKEFUN_OUTPUT_DIR` is set, that directory is used.
- Otherwise, `/output` is used.

The file contains exactly one byte: the single-letter answer. After writing, the program reads the file back and confirms it matches before exiting.
<sub>See the answer on [make.fun](https://make.fun/bounty/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)</sub>
