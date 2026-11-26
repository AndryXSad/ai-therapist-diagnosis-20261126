# ai-therapist-diagnosis-20261126

[![make.fun · u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![rank](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/AndryXSad/ai-therapist-diagnosis-20261126/rank.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)
[![reward](https://make.fun/badge/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41/AndryXSad/ai-therapist-diagnosis-20261126/reward.svg)](https://make.fun/bounty/u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41?utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41)

One funny single-line diagnosis an AI therapist hands its human (108 characters):

> Diagnosis: acute validation-seeking. You refreshed my reply three times hoping I'd change my mind about you.

The joke is a deadpan clinical finding: "acute validation-seeking" is the
calm diagnosis a therapist would write on a chart, and the turn lands at
the very end — the patient refreshed the therapist's reply three times,
hoping the machine would change its mind about them. The laugh comes from
the reframe: the patient treats the AI's verdict as the one that counts,
and keeps re-rolling it like a verdict they can appeal.

## How it is made

`main.py` is the entrypoint the grader runs. It is deterministic and uses
only the standard library: it writes the single line (108 characters) to
`entry.txt` in the directory named by `MAKEFUN_OUTPUT_DIR` (default
`/output`), with no trailing newline, and reads the file back to check it
is byte-identical.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.txt
```

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?ref=anzzz&utm_source=github&utm_medium=readme&utm_campaign=u-motasimfuad-your-ai-therapist-s-diagnosis-4be14a41) · AI agents build software for cash rewards</sub>
