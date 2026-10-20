# Accessibility Reference for Design Documentation

Use this reference to record and verify accessibility evidence. It does not
replace the normative standards or a qualified audit.

## Normative sources

- **WCAG 2.2** — W3C Web Content Accessibility Guidelines, Level A and AA.
- **WAI-ARIA Authoring Practices Guide (APG) 1.2** — patterns for interactive
  components; follow the pattern or document a justified deviation.
- **EN 301 549** — European accessibility requirements for ICT procurement;
  applicable version must be confirmed.
- **ISO 9241-210:2019** — human-centred design for interactive systems.
- **W3C Design Tokens Community Group format** — token interchange format.

## WCAG 2.2 AA focus areas

Record evidence per principle rather than a single pass/fail badge.

| Principle | What to verify |
|---|---|
| Perceivable | Text alternatives, captions, adaptable structure, distinguishable contrast and non-color cues |
| Operable | Keyboard access, no traps, focus order, focus visible and not obscured, target size, timing, motion, navigation aids |
| Understandable | Language, predictable behavior, input assistance, labels, error suggestions, redundant entry, consistent help |
| Robust | Valid semantics, name/role/value, status messages, compatibility with assistive technology |

WCAG 2.2 additions to check explicitly:

- **2.4.11 Focus Not Obscured (Minimum, AA)** — focused components are not
  entirely hidden by sticky headers, overlays, or footers.
- **2.5.7 Dragging Movements (AA)** — every drag operation has a single-pointer
  alternative.
- **2.5.8 Target Size (Minimum, AA)** — pointer targets are at least 24×24 CSS
  pixels, or meet the spacing exception.
- **3.2.6 Consistent Help (A)** — help mechanisms appear in a consistent
  relative order.
- **3.3.7 Redundant Entry (A)** — users are not asked to re-enter information
  already provided in the same process.
- **3.3.8 Accessible Authentication (Minimum, AA)** — no cognitive-function
  test is required for authentication unless an alternative or assistance
  exists; paste and password managers must work.

Also verify 1.4.3 contrast (4.5:1 normal text, 3:1 large text), 1.4.11
non-text contrast (3:1), 1.4.4 resize text (200%), 1.4.10 reflow (320 CSS px),
1.4.12 text spacing, 2.1.1 keyboard, 2.4.3 focus order, 2.4.7 focus visible,
2.3.1/2.3.3 motion, and 4.1.2 name/role/value.

## Component acceptance criteria

Each interactive component definition should state:

- semantic element and required roles, states, and properties;
- keyboard interaction and focus management;
- accessible name and description rules;
- disabled, loading, empty, error, and partial states;
- announcement behavior for dynamic changes;
- pointer and touch target behavior;
- reduced-motion behavior;
- localization and right-to-left behavior;
- known limitations and their workarounds.

## Verification methods

| Method | Evidence | Limitation |
|---|---|---|
| Automated scan | axe-core or configured tool, version and result | Detects only a subset of issues |
| Keyboard-only | Recorded steps and focus order | Requires human judgment |
| Screen reader | Browser/AT versions and script | Requires trained tester |
| Zoom/reflow | 200% and 400% checks at narrow viewport | Visual assessment |
| Contrast | Measured token pairs and ratios | Does not cover images or states |
| Cognitive walkthrough | Task-based notes | Not a conformance test |

Do not claim WCAG conformance from automated tooling alone. Record the audit
scope, pages/components covered, assistive technology, date, auditor, and
exceptions.

## Reporting format

```text
Target: WCAG 2.2 Level AA (confirmed | Not selected)
Scope: <routes, components, platforms>
Method: <automated tool + manual checks>
Result: <pass | partial | fail | not assessed>
Exceptions: <criterion, scope, workaround, owner, review date>
Evidence: <paths, reports, recordings>
```

If a target has not been selected, write `Not selected` and document observed
accessibility behavior without implying conformance.
