# Licence Guidance

A licence is a legal grant, not a documentation default. `ai-init` must never
choose one on the user's behalf, invent terms, or copy a licence it cannot
verify. This reference explains how to detect, confirm, and record a licence.

## Detection order

1. **Existing `LICENSE`, `LICENCE`, `COPYING`, or `NOTICE` file.** Preserve it
   byte-for-byte unless the user asks for a change. Detect the file name
   case-insensitively.
2. **Manifest licence field.** Check `package.json` (`license`), `pyproject.toml`
   (`project.license` as an SPDX expression), `Cargo.toml` (`license`),
   `pom.xml`, `*.gemspec`, `composer.json`, `go.mod` (indirect), or the
   equivalent. An SPDX expression such as `MIT` or `Apache-2.0` is evidence.
3. **Explicit user instruction.** A named licence with a confirmed copyright
   holder is sufficient.
4. **No evidence.** Do not create a licence. Report that no licence is
   documented and that the repository default is therefore "all rights
   reserved" in many jurisdictions. Never guess.

If sources conflict (for example a manifest says MIT and `LICENSE` contains
Apache-2.0), surface the conflict and stop. Do not silently pick one.

## What to write

- Use the canonical file name `LICENSE` at the repository root.
- Copy the exact, canonical text of the chosen licence. Do not paraphrase,
  shorten, or "improve" legal text.
- Fill only the fields the licence defines, such as copyright year and holder.
  Use the confirmed holder; do not invent a legal entity or a person's name.
- If the licence requires a `NOTICE` file or attribution, create it only when
  the upstream project provides the required content.
- Record the SPDX identifier in the README licence section and, when the
  project has a manifest, align the manifest field with it.

## Common identifiers

| SPDX identifier | Name | Notes |
|---|---|---|
| `MIT` | MIT License | Permissive; requires the copyright and permission notice |
| `Apache-2.0` | Apache License 2.0 | Permissive; includes a patent grant and NOTICE handling |
| `BSD-2-Clause` | BSD 2-Clause | Permissive; requires the notice |
| `BSD-3-Clause` | BSD 3-Clause | Adds a non-endorsement clause |
| `ISC` | ISC License | Short permissive licence |
| `MPL-2.0` | Mozilla Public License 2.0 | File-level copyleft |
| `LGPL-3.0-only` | GNU Lesser GPL 3.0 | Library copyleft; linking obligations |
| `GPL-3.0-only` | GNU GPL 3.0 | Strong copyleft; distribution obligations |
| `AGPL-3.0-only` | GNU AGPL 3.0 | Network-use copyleft |
| `UNLICENSED` | Proprietary | Use for private code; not an open-source grant |
| `CC-BY-4.0` | Creative Commons Attribution 4.0 | Content, not software |
| `CC0-1.0` | Public-domain dedication | Content and data |

SPDX expressions can combine terms, for example `MIT OR Apache-2.0` or
`Apache-2.0 WITH LLVM-exception`. Use the identifiers exactly as published at
<https://spdx.org/licenses/>.

## Rules

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
- If the user asks for a licence recommendation, list options with trade-offs
  and state that the decision belongs to the owner. Do not pick silently.

## Verification

After creating or updating a licence:

- confirm the file name is exactly `LICENSE`;
- confirm the SPDX identifier matches the text;
- confirm the copyright line uses a confirmed holder;
- confirm the README licence section matches;
- confirm the manifest licence field matches, when one exists;
- report any conflict or unknown instead of resolving it silently.
