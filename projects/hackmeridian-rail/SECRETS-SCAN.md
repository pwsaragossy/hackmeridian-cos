# SECRETS-SCAN

repo HEAD: 179bb9cfc3b85bc37fe0af2ea8eeee4dfb29532f (github.com/pwsaragossy/rio-miami-rail, fresh clone, 6 commits)
time: 2026-10-25T11:47:05Z (UTC)

Output below is redacted to file:line (and history line number) only; no match content shown. Every command printed nothing, i.e. zero matches.

## (a) tree: Stellar secret-key pattern
```
grep -rnE "S[A-Z2-7]{55}" --exclude-dir=.git .
(no output)
```
## (b) history: same pattern
```
git log -p --all | grep -nE "S[A-Z2-7]{55}"
(no output)
```
## (c) names, case-insensitive, word boundaries on ZIS/ADS/OAS
```
P='ZIS|Paulo|Protasio|Protásio|CISBRA|CAERJ|Camacol|ADS|OAS|RITLA|Glocal|UpShift|Joe Chi|radox-internal|CAF4JIUZ'
grep -rniE "$P" --exclude-dir=.git .         # tree: (no output)
git log -p --all | grep -niE "$P"            # history: (no output)
```
## (d) env files
```
ls -a | grep -i "^\.env"     # (no output): no .env file in the clone
git check-ignore -v .env     # .gitignore:3:.env	.env   (also .gitignore:4 .env.*)
```

Verdict: clean
