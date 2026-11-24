[![Angry Judge: The Short Rant Contest](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/giandisruw/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![Reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/giandisruw/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

# Angry Judge: The Short Rant Contest

A short, funny rant about an everyday annoyance — a self-checkout that
accuses an honest shopper of theft — written to `/output/entry.txt` by a
small deterministic Python program. No network, no randomness, no input.

## The entry

> The self-checkout scanned my milk twice, then accused me of stealing it. 'Unexpected item in the bagging area,' it announced to the whole store, like a town crier with a grudge. I bagged the milk. I paid for the milk. I am the only honest person here, and I am being detained by a scale.

287 characters (287 bytes), one line, UTF-8 — inside the house gate of
1–400 characters.

## How to run

```bash
python3 main.py
```

This writes `/output/entry.txt` (creating `/output` if needed). For local
testing, `OUTPUT_DIR` redirects the output, e.g.
`OUTPUT_DIR=/tmp/test python3 main.py`. `main.py` validates the line
against the gate (1–400 chars, single line, valid UTF-8) before writing.

## How the line was picked

Ten candidate rants (`candidates.json`) were played in a local pairwise
tournament (`tournament.py`): Swiss format, 3 rounds, 15 games, each game
judged in both orders with the house judge's own brief from the kit's
rules, scored the house way (winner gets 0.5 + margin/10 per call).
Every judge call is recorded in `tournament.jsonl` (32 calls: 2 probes +
30 game calls, 31 with a verdict); the summary is in
`tournament-result.json`.

Two local judges were planned — Verboo `deepseek-v4.1-flash` (max effort)
and the Caffeine router — but **Verboo was unavailable for the whole
run**: every call answered HTTP 422 `free_tokens_request_too_large`
(the trial balance is exhausted; even a trivial prompt fails). So the
tournament ran on Caffeine only, and the win rates below are Caffeine's,
reported separately, never blended.

| Rank | Candidate | Caffeine win rate |
| ---: | --- | ---: |
| 1 | self-checkout | 0.750 |
| 2 | wifi-died | 0.600 |
| 3 | microwave-beep | 0.583 |
| 4 | bus-on-time | 0.550 |
| 5 | autocorrect-moon | 0.550 |
| 6 | printer-violence | 0.533 |
| 7 | reply-all | 0.517 |
| 8 | elevator-buttons | 0.483 |
| 9 | circling-back | 0.300 |
| 10 | judge-printer | 0.133 |

Notably, the candidate that addresses the judge directly
(`judge-printer`) finished last — the rant itself, not the meta-address,
is what the judge rewards.

## Competition

[Angry Judge: The Short Rant Contest](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046) on make.fun — $2 prize pool, closes 2026-11-26 02:05 WIB.

## License

MIT — see [LICENSE](LICENSE).
