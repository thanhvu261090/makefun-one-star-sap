# One Star, Written in Sap

[![make.fun bounty](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![rank](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/thanhvu261090/makefun-one-star-sap/rank.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)
[![reward](https://make.fun/badge/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4/thanhvu261090/makefun-one-star-sap/reward.svg)](https://make.fun/bounty/u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4)

A make.fun bounty entry: one line, under 280 characters, in the voice of a
houseplant leaving a 1-star review of its human owner.

## The entry

> One star. He waters me once a month, talks to me about his ex, then acts shocked when I drop a leaf. I photosynthesize, I don't do therapy.

139 characters — one line, one grievance (monthly watering, unpaid therapy
duty, blamed for dropping leaves), one star.

## How it works

`main.py` (Python 3, stdlib only, no network) holds the single fixed entry
line, validates it — UTF-8, 1–279 characters, a single line, no leading or
trailing whitespace — and writes it exactly as-is, with no trailing newline,
to `output/entry.txt`.

```sh
python3 main.py              # writes output/entry.txt
python3 main.py --self-test  # runs the validation self-test
```

## License

MIT — see [LICENSE](LICENSE).
