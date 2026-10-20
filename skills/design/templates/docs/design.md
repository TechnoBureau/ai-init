# Design System — {{PROJECT_NAME}}

> **Applicability:** ONLY for projects with a UI/UX surface (web, mobile,
> desktop apps). Not applicable to CLIs, APIs, CI/CD pipelines, scripts,
> or libraries without a visual interface. If not applicable, delete this
> file and note it in `README.md` ("Not applicable: docs/design.md — no UI
> surface").

## Summary

{{PLAIN_LANGUAGE_DESCRIPTION_OF_THE_UI_AND_ITS_VERIFIED_DESIGN_STATUS}}

Distinguish what is implemented from decisions that are confirmed but not yet
implemented. Mark unknowns `Not documented` or `Not selected`. Record the
paths examined so the review can be repeated.

## 1. Chosen Design System

**System:** {{VERIFIED_DESIGN_SYSTEM_OR_NOT_SELECTED}}

**Version / package:** {{VERIFIED_VERSION_OR_NOT_DOCUMENTED}}

**Why this system:** {{CONFIRMED_RATIONALE_OR_NOT_DOCUMENTED}}

**Adopt as-is vs. adapt:**

| Aspect | Adopt / Adapt | Notes |
|---|---|---|
| Color tokens | | |
| Typography scale | | |
| Spacing/grid | | |
| Components | | |
| Iconography | | |
| Motion | | |
| Localization/RTL | | |

## 2. Design Tokens

Prefer the W3C Design Tokens Community Group (DTCG) format (`$value`, `$type`,
`$description`). If the project uses another format, state the mapping. Record
the token source path and generation process.

### Color

| Token | Value | Usage | Contrast pairing |
|---|---|---|---|
| {{OBSERVED_TOKEN_NAME}} | {{OBSERVED_VALUE_OR_NOT_DOCUMENTED}} | {{USAGE}} | {{VERIFIED_RATIO_OR_NOT_TESTED}} |

### Typography

| Token | Font / Size / Weight / Line height | Usage |
|---|---|---|
| {{OBSERVED_TOKEN_NAME}} | {{OBSERVED_VALUE_OR_NOT_DOCUMENTED}} | {{USAGE}} |

### Spacing, Radius, and Elevation

| Token | Value | Usage |
|---|---|---|
| {{OBSERVED_TOKEN_NAME}} | {{OBSERVED_VALUE_OR_NOT_DOCUMENTED}} | {{USAGE}} |

### Motion

| Token | Duration / Easing | Usage | Reduced-motion behavior |
|---|---|---|---|
| {{OBSERVED_TOKEN_NAME}} | {{OBSERVED_VALUE_OR_NOT_DOCUMENTED}} | {{USAGE}} | {{VERIFIED_OR_NOT_DOCUMENTED}} |

## 3. Core Components

| Component | Source system reference | Variants / states | Accessibility notes | Customization |
|---|---|---|---|---|
| {{COMPONENT}} | {{SYSTEM_OR_LOCAL_PATH}} | {{STATES}} | {{KEYBOARD_SEMANTICS_FOCUS}} | {{NOTES}} |

Document default, hover, focus, active, disabled, loading, empty, error, and
success states where they exist. Do not invent component variants.

## 4. Accessibility

- Target conformance: {{CONFIRMED_TARGET_OR_NOT_SELECTED}}
- Audit scope and date: {{SCOPE_AND_DATE_OR_NOT_ASSESSED}}
- Automated checks and tool versions: {{VERIFIED_OR_NOT_CONFIGURED}}
- Manual keyboard, focus, zoom, and screen-reader evidence:
  {{VERIFIED_OR_NOT_ASSESSED}}
- Known exceptions: {{CRITERION_SCOPE_WORKAROUND_OWNER_REVIEW_DATE_OR_NONE}}

Apply WCAG 2.2 Level AA criteria when selected, including focus not obscured,
dragging alternatives, target size, consistent help, redundant entry, and
accessible authentication. Do not claim conformance without a completed audit.

## 5. Layout and Responsiveness

| Breakpoint / range | Layout behavior | Navigation behavior |
|---|---|---|
| {{VERIFIED_RANGE}} | {{GRID_OR_STACKING}} | {{NAV_PATTERN}} |

- Grid and spacing system: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Reflow and 400% zoom behavior: {{VERIFIED_OR_NOT_ASSESSED}}
- Safe areas and platform insets: {{VERIFIED_OR_NOT_DOCUMENTED}}

## 6. Content Design

- Voice and tone: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Error message pattern: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Empty-state pattern: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Confirmation and destructive-action copy: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Localization and pluralization rules: {{VERIFIED_OR_NOT_DOCUMENTED}}

## 7. Localization and Internationalization

| Concern | Current behavior |
|---|---|
| Supported locales | {{CONFIRMED_LIST_OR_NOT_DOCUMENTED}} |
| Right-to-left support | {{VERIFIED_OR_NOT_IMPLEMENTED}} |
| Text expansion tolerance | {{VERIFIED_OR_NOT_TESTED}} |
| Date/number/currency formatting | {{VERIFIED_OR_NOT_DOCUMENTED}} |

## 8. Motion and Interaction

{{GUIDELINES}}

Document reduced-motion behavior, animation purpose, and any interaction that
is hover-only, drag-only, or gesture-only. Each must have an accessible
alternative.

## 9. Design Assets

- Figma / source files: {{LINK_OR_NOT_DOCUMENTED}}
- Icon set and licence: {{LINK_AND_LICENCE_OR_NOT_DOCUMENTED}}
- Fonts and licence: {{LINK_AND_LICENCE_OR_NOT_DOCUMENTED}}
- Screenshots / prototype: {{LINK_OR_NOT_DOCUMENTED}}

## 10. Governance and Quality Gates

- Design owner: {{OWNER_OR_UNKNOWN}}
- Change and review process: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Deprecation policy: {{VERIFIED_OR_NOT_DOCUMENTED}}
- Design QA criteria: {{VERIFIED_CHECKLIST_OR_NOT_DOCUMENTED}}
- Component acceptance requires: states, accessibility, localization, and
  documentation.

______________________________________________________________________

### Related Docs

[README](../README.md) · [PRD](./PRD.md) · [Architecture](./architecture.md) · [Style](./style.md)
