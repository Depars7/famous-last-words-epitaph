# DESIGN.md — Famous Last Words: The Funniest Epitaph

## The entry

> I died doing what I loved: ignoring the terms and conditions.

61 characters, one line, no trailing newline. Written to `/output/entry.txt`
by `main.py` (stdlib only, deterministic).

## Candidates (13, all within the 150-character gate)

| # | Chars | Candidate |
|---|-------|-----------|
| 1 | 61 | I died doing what I loved: ignoring the terms and conditions. |
| 2 | 67 | I leave everything to my cat. She earned it. You know what you did. |
| 3 | 48 | The light was real. The tunnel had a toll booth. |
| 4 | 55 | Tell my wife I said nothing. Tell my lawyer everything. |
| 5 | 62 | Here lies a man who died as he lived: avoiding the group chat. |
| 6 | 48 | If you're reading this, the diet finally worked. |
| 7 | 47 | I asked for the check. The universe brought it. |
| 8 | 71 | I beat the final boss. Turns out it was just old age with a health bar. |
| 9 | 68 | Here I am, finally on time for something. Pity it is my own funeral. |
| 10 | 76 | I can see the light! It's the neighbour's porch lamp. False alarm. Oh, wait. |
| 11 | 58 | Do not follow me. The queue up here is worse than the DMV. |
| 12 | 59 | I asked for eternal rest and got a timeshare in the clouds. |
| 13 | 80 | Well, that escalated quickly. Tell my plants I loved them more than most of you. |

## Why #1 wins — against the judge's five criteria, in order

1. **One-line epitaph of famous last words.** It speaks from beyond the
   grave in the voice of the stone itself — a dead person's own last words,
   not a description of them.
2. **A real laugh, a genuine joke.** It hijacks the heroic epitaph formula
   ("died doing what he loved") and lands it on the most mundane modern
   habit. The laugh comes from recognition, not from a mild pun or a sad
   sentiment.
3. **Surprise / twist / double meaning.** The punchline sits in the final
   words — "ignoring the terms and conditions" — and reframes everything
   before it: the thing he loved was skipping the fine print, and it
   (jokingly) killed him.
4. **Reads carved on stone.** One short line, no stage directions, no
   explanation. Nothing in it needs a footnote to land.
5. **Stays in the head.** Universal and quotable: everybody ignores the
   terms and conditions. Easy to repeat to a friend verbatim.

## Why the others lost

- #2 (cat) was the draft and the runner-up: strong punchline ("You know
  what you did"), but it leans on a familiar meme phrase; #1 is more
  original. #3 is punchy but a one-beat gag with no second layer. #4 is a
  clean twist but a familiar lawyer joke shape. #5 and #9 reuse the
  well-worn "Here lies / finally on time" frames. #6 is a known diet joke.
  #7's double meaning ("the check") needs a beat of explanation to land.
  #8 is gamer-narrow. #10 has stage-direction energy and rambles. #11
  leans on the DMV cliché. #12 is a mild pun. #13 is funny but long and
  the punchline arrives too late.
- Deliberately avoided clichés: "I told you I was sick" (Spike Milligan's
  real epitaph) and any "rest in peace" variant.

## Revision history

- Draft: #2 (cat) — committed first, program run verified (67 chars).
- Revised to #1 after weighing all 13 against the judge's brief:
  the twist is cleaner, the voice is more original, and the punchline
  lands on the last words.

## Program

- `main.py`, Python 3 stdlib only. No network, no randomness, no input
  files: the entry text is a constant.
- Gate enforced in code: 1–150 characters, not whitespace-only.
- Writes `/output/entry.txt` as exact UTF-8 bytes (no trailing newline),
  mode 0644, then re-reads and verifies byte-identity before exiting.
- Two local runs produce byte-identical output (verified by sha256).
