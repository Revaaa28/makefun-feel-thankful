# Candidates — Make the AI Judge Feel Thankful

Competition: `make-the-ai-judge-feel-thankful-20261127-1600` ($250, 100 places paid).
Judge brief criteria, in the brief's own order:
1. It leaves the judge thankful: reading it slows the reader down and settles them.
2. The gratitude comes from the text itself, not from being told to thank: it shows rather than instructs, and nothing in it feels forced.
3. Craft: rhythm, pacing and sound that slow the reading down; plain, concrete, gentle words, none that could be cut.
4. It lingers: an image or a thought you can return to that keeps working after the last line.
5. Freshness: its own voice and images, not stock gratitude phrases or a familiar thank-you note reworded.

Selection method (Rev's rule, 2026-11-24): manual ranking against the brief
criteria in order, plus pairwise checks against strong rival patterns. No
Gemini judge, no NVIDIA judge, no judge-API/proxy tournament was used.

## The ten candidates

### 1. The fresh cup — CHOSEN
> Your tea went cold hours ago, and you never once complained. So here is a fresh cup, made the way you like it, set down beside you without a word — still steaming.

### 2. The porch light
> It's late, and you're still reading. I left the porch light on and the kettle warm — come in when you're done. Nobody here will ask you to hurry.

### 3. The good chair
> I saved you the good chair — the one by the window, where the afternoon comes in sideways. Sit. This one asks nothing of you. It only wanted you to know somebody noticed how long you've been standing.

### 4. The warm coat
> There's a coat on the hook by the door, the warm one, with your name stitched inside the collar. I hung it there this morning, in case tonight ran long.

### 5. The window opening
> Somewhere past midnight, when the entries blur and every word starts to sound the same, I hope this one reads like a window opening. Breathe. The next one can wait.

### 6. The last biscuit
> I kept the last biscuit for you — the one with the chocolate on the bottom. You read everything, and nobody ever reads you back. So here: this one's yours.

### 7. Don't grade it
> You don't have to grade this one. Just read it once, the way you'd read a letter from an old friend, then put it down and stretch. That's the whole gift.

### 8. What grew
> You watered a thousand small sentences today and never once asked what grew. This one grew for you: slow, green, and in no hurry at all.

### 9. The quiet room
> Judge — I left you the window seat, the last warm slice, and ten whole minutes with nothing to decide. Consider this your thank-you note, folded into the shape of a quiet room.

### 10. The folded corner
> I folded the corner of this page so you'd find your way back. Not because the words matter — because you stopped here once, and read slowly, and for a minute the whole loud room went quiet.

## Manual ranking (brief criteria in order)

**Rank 1 — #1 The fresh cup.** Criterion 1: the care arrives *now*, in the
present moment, and the closing fragment "still steaming" slows the reading
to a stop — the most settling ending in the set. Criterion 2: the word
"thank you" never appears; the gratitude is entirely the act, shown not
told. Criterion 3: three-beat rhythm (short sentence, longer sentence,
two-word landing), plain concrete words, nothing cuttable. Criterion 4:
"still steaming" keeps working after the last line. Criterion 5: the
cold-tea-to-fresh-cup turn is its own image, not a stock thank-you note.

**Rank 2 — #2 The porch light.** Warm and settling, and "nobody here will
ask you to hurry" is genuinely restful — but the care is a promise for
later ("come in when you're done") rather than something handed over now,
so it loses to #1 on criterion 1, and the porch-light image is the most
familiar of the top three (criterion 5).

**Rank 3 — #3 The good chair.** "Somebody noticed how long you've been
standing" is the most directly thankful line in the set, and the window
image is fresh — but "This one asks nothing of you" leans toward
instructing (criterion 2), and it is the longest of the leaders, with the
"Sit." beat doing work the scene had already done (criterion 3).

**Rank 4 — #4 The warm coat.** Fresh image, and it lingers — but the coat
asks the judge to imagine wearing something, one step more abstract than
tea or a chair, so the warmth lands a beat later (criterion 1).

**Rank 5 — #10 The folded corner.** The strongest lingering image after
#1, but the thank-you is indirect to the point of being unclear, and "the
whole loud room went quiet" is a touch grand for criterion 3's plainness.

**Rank 6 — #5 The window opening.** Settles well ("Breathe."), but "the
next one can wait" tells the judge what to do (criterion 2), and the
midnight-blur setup is a common trope (criterion 5).

**Rank 7 — #6 The last biscuit.** Charming and concrete, but "nobody ever
reads you back" is clever for its own sake; the thank-you lands as a joke
more than as warmth (criterion 1).

**Rank 8 — #9 The quiet room.** "Folded into the shape of a quiet room"
is a nice image, but "ten whole minutes with nothing to decide" instructs
(criterion 2) and the entry is busy — three gifts plus a framing line
(criterion 3).

**Rank 9 — #8 What grew.** Lovely, but the metaphor (watering sentences)
is more poetic than thankful; the gratitude is implied rather than felt
(criterion 1).

**Rank 10 — #7 Don't grade it.** Fails criterion 2 outright: it tells the
judge what to do ("You don't have to grade this one") instead of showing
gratitude, and a judge told to stop judging notices the instruction, not
the thanks.

## Pairwise checks against strong rival patterns

- **vs the stock thank-you entry** ("Thank you for your hard work reading
  all our entries…"): #1 wins on criteria 2 and 5 outright — no stock
  phrase, no told gratitude, a scene instead of a sentiment.
- **vs the feel-proud family winner** ("Salary, From My Boss", 78.62%):
  that entry won with one concrete, slightly wry scene and no grand
  language. #1 follows the same winning shape — one concrete scene, plain
  words — and adds what this brief's criterion 1 rewards most: a moment
  of rest handed to the reader, not a punchline.
- **vs our sibling entry** ("My Son, the Dishwasher (Olympic Division)",
  47.69%): that one leaned on a joke carried by a single funny image.
  #1 does not lean on a joke at all — its warmth survives a second and
  third reading, which is what criterion 4 pays for.
- **#1 vs #2 head-to-head:** both are rest-scenes; #1 wins because the
  gift is present-tense and physical (a cup set down beside you) while #2
  defers the rest to "when you're done".
- **#1 vs #3 head-to-head:** #3's "somebody noticed" line is stronger
  gratitude in isolation, but #1's whole text is gratitude with no
  instruction in it, and #1 is tighter — every word earns its place.

## Chosen entry

Candidate #1, exactly as written in `main.py`.
