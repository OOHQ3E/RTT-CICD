import sys
from pylint import lint

THRESHOLD = 10
run = lint.Run(["--rcfile=.pylintrc", "main.py"], exit=False)
score = run.linter.stats.global_note

print(f"Score : {score}")

if score < THRESHOLD:
    print(f"Linter failed, Score:{score} < threshold value: {THRESHOLD}")
    sys.exit(1)
sys.exit(0)