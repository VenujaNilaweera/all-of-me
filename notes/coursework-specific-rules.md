---
type: note
title: Course-Specific Rules (OR, AI, Lab Reports, PCB Wording)
status: ongoing
start:
end:
created: 2026-09-21
updated: 2026-09-21
tags: [coursework, operations-research, ai-course, lab-reports, university-of-jaffna]
links: [[[cs-networking-and-algorithms]]]
---

# Course-Specific Rules

Rules Venuja has set for how to help with specific subjects — apply these
exactly when working on the matching coursework.

## Operations research & CPM
- CPM/AOA: drop redundant predecessors before drawing. Dummy arrows point
  from the "pure/alone" node to the "combined/merge" node — dummies only
  where two activities share some but not all predecessors.
- KKT: convert minimisation to maximisation by multiplying the objective
  by -1. Convert every constraint, including nonnegativity, into <=
  form with its own multiplier (u1, u2, u3...) — don't fold
  nonnegativity into a separate KKT condition. Structure cases around
  primal variables (x1=0, x2=0, both nonzero). Benefit-to-cost ratio
  (objective coefficient over constraint coefficient) decides which
  variable to drop.
- Second-order conditions: if principal minors are all positive, or
  alternate starting negative, skip the tangent-space Z method — use it
  only when the pattern is mixed.
- Simplex: a >= constraint with positive RHS needs a surplus variable
  plus an artificial variable with -M. Big-M: apply Row(0) - M*Row
  (artificial) before iterating. Tableau has no zj-cj row.
- Transportation degeneracy: place epsilon in an independent cell of
  minimum cost to reach m+n-1 occupied cells.
- Network/arrow diagrams: deliver as downloadable HTML with SVG (see
  [[ai-collaboration-preferences]] for the general format preference).

## AI course
- First-order logic: universal quantifiers pair with implication
  (forall x, P(x) => Q(x)); existential quantifiers pair with
  conjunction (exists x, P(x) and Q(x)). Universal-with-conjunction is
  almost always a mistake. Predicate argument order is fixed; only
  transitive verbs take two arguments.
- Goal-stack planning: show the full stack at every step, mark each pop
  as true/discard or false/push-operator, update world state when
  operators apply, end with a PLAN line.
- Submissions: specified font, black text only, real sourced references,
  precise structure.

## Lab reports in Word (EC7091 style)
Figures captioned "Figure 01: short label", size 11, underlined, not
bold, centred, placed below the image. Tables numbered the same way but
captioned above; rows alternate blue header / white / light blue.
Captions are short labels, not full sentences. Keep handout objectives
unchanged. Don't sweep the whole document again on a revision — Venuja
names the specific pages to edit after his own manual review.

## PCB phrasing
"Shunt resistor placed in series" is the correct industry wording for
current-sense resistors — noted specifically for interview phrasing.
