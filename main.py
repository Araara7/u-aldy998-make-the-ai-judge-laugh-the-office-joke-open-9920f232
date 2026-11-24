"""Write one line of office comedy to /output/entry.txt.

Entry: a printer gag -- the machine that proves you wrong by printing.
The turn lands in the last words: the printer's "proof" is a 40-page
error report, so the complaint about the printer becomes the printer's
own punchline.
"""

import os

ENTRY = "I told the printer it was out of paper, so it printed a 40-page error report to prove me wrong."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
