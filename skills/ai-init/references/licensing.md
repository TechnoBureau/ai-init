# Licence Guidance

A licence is a legal grant, not a documentation default. `ai-init` never picks
one silently. When no licence is evidenced it asks the owner a single question
— **is this project open source or commercial?** — and generates from the
answer. Existing evidence outranks the question, and the answer is recorded
exactly as the owner gave it.

## The decision to ask

When no licence is evidenced, ask before generating any licence artifact:

> Is this project open source or commercial?

The two answers are mutually exclusive, and each produces a different output:

| Answer | What `ai-init` generates |
|---|---|
| **Open source** | `LICENSE` containing canonical **MIT** text with the confirmed holder, plus the SPDX identifier `MIT` in the README licence section and the manifest, when one exists |
| **Commercial** | **No open-source licence.** No `LICENSE` file carrying an open-source grant and no open-source SPDX identifier anywhere in the repository. Record `Proprietary — all rights reserved` in the README licence section unless the owner supplies specific commercial terms |

A commercial answer never produces MIT, Apache-2.0, or any other open-source
grant. An open-source answer never adds a restrictive commercial clause. If the
owner wants both, that is dual licensing: report it and refer it to legal
review rather than emitting a hybrid file.

### Open source

- MIT is the default answer because it is short, widely understood, and
  requires only the copyright and permission notice. Use it unless the owner
  names a different identifier.
- Ask for the copyright holder when it is not already confirmed. MIT requires
  the notice, so the holder belongs in the licence text, not in a comment.
- Copy the canonical text verbatim and fill only the fields MIT defines: year
  and holder.
- If the owner raises patent exposure, note that Apache-2.0 adds an explicit
  patent grant and NOTICE handling, then let them choose. Do not decide for
  them.

### Commercial

- Do not write an open-source licence. Do not leave an existing permissive
  licence in place while describing the project as commercial; report the
  conflict instead.
- The correct default is **no licence file**. Absent a grant, the work stays
  under default copyright, which is "all rights reserved" in most
  jurisdictions. That is a real legal position, not a gap to paper over.
- Write a proprietary notice only when the owner supplies the actual terms.
  Never draft redistribution limits, warranty disclaimers, indemnities, or
  export controls.
- Refer commercial terms, source-available models such as BUSL or SSPL, dual
  licensing, and relicensing to legal review. `ai-init` records the confirmed
  decision; it does not author it.

## Detection order

1. **Existing `LICENSE`, `LICENCE`, `COPYING`, or `NOTICE` file.** Preserve it
   byte-for-byte unless the user asks for a change. Detect the file name
   case-insensitively. Do not ask the question when a grant already exists;
   report what the file contains instead.
2. **Manifest licence field.** Check `package.json` (`license`),
   `pyproject.toml` (`project.license` as an SPDX expression), `Cargo.toml`
   (`license`), `pom.xml`, `*.gemspec`, `composer.json`, `go.mod` (indirect),
   or the equivalent. An SPDX expression such as `MIT` or `Apache-2.0` is
   evidence. An identifier of `UNLICENSED` is evidence of a commercial project.
3. **The owner's answer to the open source or commercial question.** This is
   the default path for a repository with no licence evidence.
4. **The owner declines or does not answer.** Do not create a licence. Report
   that no licence is documented and that the repository default is therefore
   "all rights reserved" in many jurisdictions. Never guess.

If sources conflict (for example a manifest says MIT and `LICENSE` contains
Apache-2.0, or the owner says commercial while an MIT `LICENSE` is committed),
surface the conflict and stop. Do not silently pick one.

## What to write

- Use the canonical file name `LICENSE` at the repository root.
- Copy the exact, canonical text of the chosen licence. Do not paraphrase,
  shorten, or "improve" legal text.
- Fill only the fields the licence defines, such as copyright year and holder.
  Use the confirmed holder; do not invent a legal entity or a person's name.
- If the licence requires a `NOTICE` file or attribution, create it only when
  the upstream project provides the required content.
- Record the SPDX identifier in the README licence section and, when the
  project has a manifest, align the manifest field with it. For a commercial
  project record `Proprietary — all rights reserved` in prose; `UNLICENSED` is
  the SPDX identifier for a manifest field.

## Common identifiers

| SPDX identifier | Name | Notes |
|---|---|---|
| `MIT` | MIT License | **Default open-source answer.** Permissive; requires the copyright and permission notice |
| `Apache-2.0` | Apache License 2.0 | Permissive; includes a patent grant and NOTICE handling |
| `BSD-2-Clause` | BSD 2-Clause | Permissive; requires the notice |
| `BSD-3-Clause` | BSD 3-Clause | Adds a non-endorsement clause |
| `ISC` | ISC License | Short permissive licence |
| `MPL-2.0` | Mozilla Public License 2.0 | File-level copyleft |
| `LGPL-3.0-only` | GNU Lesser GPL 3.0 | Library copyleft; linking obligations |
| `GPL-3.0-only` | GNU GPL 3.0 | Strong copyleft; distribution obligations |
| `AGPL-3.0-only` | GNU AGPL 3.0 | Network-use copyleft |
| `UNLICENSED` | Proprietary | **Default commercial answer.** Not an open-source grant |
| `CC-BY-4.0` | Creative Commons Attribution 4.0 | Content, not software |
| `CC0-1.0` | Public-domain dedication | Content and data |

SPDX expressions can combine terms, for example `MIT OR Apache-2.0` or
`Apache-2.0 WITH LLVM-exception`. Use the identifiers exactly as published at
<https://spdx.org/licenses/>. Commercial terms such as BUSL, SSPL, and ELv2 are
source-available, not open source; write them only when the owner supplies the
exact text and has had them reviewed.

## Rules

- Ask the open source or commercial question before creating a licence, unless
  a licence is already evidenced.
- Do not apply a licence to third-party code the project does not own.
- Do not change a licence because a dependency uses a different one. Record
  compatibility concerns for review instead.
- Do not claim licence compatibility, legal review, or compliance. Recommend
  legal review for copyleft, dual licensing, relicensing, or commercial terms.
- Do not add a copyright holder without confirmation. "The project
  contributors" is acceptable only when the owner has adopted that convention.
- Do not put a licence header in every source file unless the project already
  uses that convention; document the convention in `docs/style.md` instead.
- Keep `LICENSE` out of generated documentation sets; it is a legal artifact,
  not a project document.
- If the owner asks for a recommendation, present MIT for open source and
  "all rights reserved until reviewed" for commercial, with trade-offs. State
  that the decision belongs to the owner.

## Verification

After creating or updating a licence:

- confirm the open source or commercial answer was given by the owner or is
  evidenced by an existing file;
- confirm the file name is exactly `LICENSE`;
- confirm the SPDX identifier matches the text;
- confirm the copyright line uses a confirmed holder;
- confirm the README licence section matches;
- confirm the manifest licence field matches, when one exists;
- confirm a commercial project contains no open-source grant and no
  open-source SPDX identifier;
- report any conflict or unknown instead of resolving it silently.
