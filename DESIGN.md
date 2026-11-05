---
name: סידור עבודה
description: The printed duty roster pinned on the unit board, every shift swiped with its own highlighter.
colors:
  ballpoint-blue: "#2543a8"
  ballpoint-blue-deep: "#1e3a94"
  ballpoint-wash: "rgba(37,67,168,0.09)"
  on-accent: "#ffffff"
  highlighter-yellow: "#ffe14a"
  highlighter-pink: "#ffb2d6"
  highlighter-green: "#a6e3a0"
  holiday-red: "#c8102e"
  holiday-ink: "#b0102a"
  minor-holiday-ochre: "#963e00"
  training-violet: "#5e3ebe"
  warning-amber: "#a64800"
  error-red: "#be122d"
  success-green: "#15733e"
  wall-gray: "#e9ecef"
  sheet-white: "#ffffff"
  sheet-tint: "#f7f8f9"
  sheet-shade: "#eef0f3"
  sheet-shade-deep: "#e2e6ea"
  ink: "#161b22"
  ink-muted: "#454e5a"
  ink-dim: "#59626e"
  hairline: "rgba(23,32,46,0.12)"
  hairline-strong: "rgba(23,32,46,0.2)"
  weekend-band: "rgba(23,32,46,0.055)"
  rail-ink: "#172138"
  rail-ink-raised: "#202c47"
  rail-text: "#eef1f6"
  rail-muted: "#aab4c6"
typography:
  display:
    fontFamily: "Heebo, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "56px"
    fontWeight: 900
    lineHeight: 1
  headline:
    fontFamily: "Heebo, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "27px"
    fontWeight: 900
    lineHeight: 1.15
    letterSpacing: "-0.015em"
  title:
    fontFamily: "Heebo, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "22px"
    fontWeight: 900
    letterSpacing: "-0.01em"
  card-title:
    fontFamily: "Heebo, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "13.5px"
    fontWeight: 800
    lineHeight: 1.25
  figure:
    fontFamily: "Heebo, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "30px"
    fontWeight: 900
    lineHeight: 1.1
    fontFeature: "tnum"
  body:
    fontFamily: "Heebo, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.45
  label:
    fontFamily: "Heebo, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "12px"
    fontWeight: 600
  grid-cell:
    fontFamily: "Heebo, system-ui, -apple-system, 'Segoe UI', sans-serif"
    fontSize: "11px"
    fontWeight: 700
    fontFeature: "tnum"
rounded:
  xs: "5px"
  sm: "7px"
  md: "9px"
  lg: "11px"
  sheet: "20px"
spacing:
  xs: "4px"
  sm: "8px"
  md: "14px"
  lg: "16px"
  xl: "24px"
components:
  button-primary:
    backgroundColor: "{colors.ballpoint-blue}"
    textColor: "{colors.on-accent}"
    rounded: "{rounded.sm}"
    padding: "0 16px"
    height: "42px"
  button-primary-hover:
    backgroundColor: "{colors.ballpoint-blue-deep}"
  button-ghost:
    backgroundColor: "{colors.sheet-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "0 16px"
    height: "42px"
  button-ghost-hover:
    backgroundColor: "{colors.sheet-shade}"
  input:
    backgroundColor: "{colors.sheet-white}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "0 13px"
    height: "44px"
  card:
    backgroundColor: "{colors.sheet-white}"
    rounded: "{rounded.lg}"
    padding: "{spacing.lg}"
  shift-marker-a:
    backgroundColor: "{colors.highlighter-yellow}"
    textColor: "{colors.ink}"
  shift-marker-b:
    backgroundColor: "{colors.highlighter-pink}"
    textColor: "{colors.ink}"
  shift-marker-c:
    backgroundColor: "{colors.highlighter-green}"
    textColor: "{colors.ink}"
  segmented-option-on:
    backgroundColor: "{colors.ballpoint-blue}"
    textColor: "{colors.on-accent}"
    height: "42px"
  nav-rail:
    backgroundColor: "{colors.rail-ink}"
    textColor: "{colors.rail-muted}"
    width: "240px"
  nav-rail-item-active:
    backgroundColor: "{colors.rail-ink-raised}"
    textColor: "{colors.rail-text}"
    rounded: "{rounded.sm}"
  tab-bar-item-active:
    backgroundColor: "{colors.ballpoint-wash}"
    textColor: "{colors.ballpoint-blue-deep}"
    height: "52px"
  month-day-cell:
    backgroundColor: "{colors.sheet-white}"
    rounded: "{rounded.sm}"
    padding: "8px"
  toast:
    backgroundColor: "{colors.sheet-shade}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "11px 18px"
---

# Design System: סידור עבודה

## Overview

**Creative North Star: "The Duty Roster on the Notice Board"**

The schedule is a printed roster: white sheets pinned to a cool light-gray wall, set in black ink, with a ballpoint-blue pen for anything the user acts on and a dark-ink rail at the inline start. The one loud material is the highlighter. Each of the three shifts owns one marker colour (א׳ yellow, ב׳ pink, ג׳ green), and every place a shift appears, from the large "on duty now" letter to each of the 365 cells in the year grid, the letter sits on an irregular, hand-swiped marker stroke. The data is the colour; the chrome stays paper and ink.

Density follows the printed original. The year view is a tight table of 10–11px tabular figures. The phone overview is spacious and answers "whose shift is it" before any reading. Calendar conventions come from a printed Hebrew calendar: holidays in red ink, weekends as a faint gray column band, today framed in black ink. Fairness numbers sit beside the roster as footnote lines, never as coloured alert tiles. The build rejects the dark command-center dashboard it replaced: no glows, background grids, radial spotlights or corner brackets.

The world ships in two themes. "יום" (board, default, light) is the canonical sheet. "לילה" (night) is the same board in light ink on dark sheets, and the highlighters stay.

**Key Characteristics:**
- Three fixed highlighter colours own the shifts, and the letter is always printed on the marker.
- Paper-and-ink chrome: white sheets, hairline rules, small radii, one ballpoint-blue accent.
- Calendar marks are drawn as ink frames and underlines on top of the marker, never as replacement fills.
- RTL Hebrew throughout. One family (Heebo) carries every role, with tabular figures for every number.
- Flat print: one barely-there sheet shadow, and real elevation only for floating layers.

## Colors

Neutral paper and ink, a single ballpoint-blue for action, three highlighters reserved for shifts, and a small set of calendar inks.

### Primary
- **Ballpoint Blue** (#2543a8): the pen. Primary buttons, the selected segment, focus outlines, caret, hover outlines on grid cells, progress bars. (CSS: `--olive`.)
- **Ballpoint Blue Deep** (#1e3a94): pressed and hover state of the primary button, plus link text and active tab text. (CSS: `--olive-2`.)
- **Ballpoint Wash** (rgba(37,67,168,0.09)): the blue tint behind the active bottom tab, link hover and the undo action in the toast.

### Secondary: The Highlighters
- **Highlighter Yellow** (#ffe14a): shift א׳. It is also the app mark in the rail, the rail's active-item tick and text selection.
- **Highlighter Pink** (#ffb2d6): shift ב׳. It also serves as the rail's unread pip.
- **Highlighter Green** (#a6e3a0): shift ג׳.

### Tertiary: Calendar Inks
- **Holiday Red** (#c8102e): the 2px holiday frame drawn around year-grid cells and the holiday dot in legends.
- **Holiday Ink** (#b0102a): holiday names and dates printed in red text on the sheet.
- **Minor-Holiday Ochre** (#963e00): minor-holiday labels and the 2px ochre underline on their cells.
- **Training Violet** (#5e3ebe): the frame and label for training days.
- **Warning Amber** (#a64800), **Error Red** (#be122d), **Success Green** (#15733e): status inks for edited values, coverage gaps and bad fairness numbers, and the live dot. Use them as text or a thin frame, never as large fills.

### Neutral
- **Wall Gray** (#e9ecef): the page background the sheets are pinned to.
- **Sheet White** (#ffffff): cards, cells, inputs and the header bar (at 92% opacity with blur).
- **Sheet Tint** (#f7f8f9) / **Sheet Shade** (#eef0f3) / **Sheet Shade Deep** (#e2e6ea): sheet tints for table heads, hover, the toast and the empty markerless chip.
- **Ink** (#161b22): body text, today's frame, and the text printed on every highlighter.
- **Ink Muted** (#454e5a) / **Ink Dim** (#59626e): secondary text, meta lines and weekday names.
- **Hairline** (rgba(23,32,46,0.12)) / **Hairline Strong** (rgba(23,32,46,0.2)): borders and row rules. Strong is for controls.
- **Weekend Band** (rgba(23,32,46,0.055)): the faint gray fill on Friday and Saturday columns and cells.
- **Rail Ink** (#172138) / **Rail Ink Raised** (#202c47) / **Rail Text** (#eef1f6) / **Rail Muted** (#aab4c6): the dark-ink navigation rail, its active item, and its text.

### Night theme (לילה)
The same roles in light ink on dark sheets: wall #0e1218, sheets #161b24 / #1b212c / #232a37, ink #e9edf3, muted #aeb7c4, pen #7fa2ff with deep #a9c0ff and dark on-accent #0b1020, holiday ink #fca5a5. The highlighters drop very slightly (#f5d33d, #f5a3c9, #94d68e) and keep dark ink on them. The rail stops being a separate dark slab and becomes the first sheet tone with a hairline edge. Card shadows are removed. The full set lives in `.impeccable/design.json` under `extensions.themes.night`.

### Named Rules
**The Highlighter Monopoly Rule.** Yellow, pink and green belong to shifts א׳, ב׳ and ג׳ and to nothing else. Never use them for status, categories, charts or decoration. The only allowed reuse is the app mark and the rail's tick and pip, which are the roster's own pen.

**The Letter-On-Marker Rule.** A shift colour never appears without its letter printed on it in ink (#161b22). Colour is the fast read and the letter is the accessible one.

**The One Pen Rule.** Ballpoint blue is the only accent for action and selection. Status colours mark text and thin frames, never buttons or large fills.

## Typography

**Display Font:** Heebo (with system-ui, -apple-system, Segoe UI, sans-serif)
**Body Font:** Heebo
**Label/Mono Font:** Heebo with `font-variant-numeric: tabular-nums`. There is no separate mono face; numbers keep their column through tabular figures.

**Character:** One Hebrew grotesque in heavy weights, the way a printed roster is set. Hierarchy comes from weight (900 down to 400) and size, not from changing face or using colour.

### Hierarchy
- **Display** (900, 56px; 44px under 900px, 34px in the small ring, 1): the shift letter on its marker in the "now" hero. Nowhere else.
- **Headline** (900, 27px; 22px on phone, 1.15, -0.015em): the hero line ("משמרת ג׳").
- **Title** (900, 22px; 19px under 600px, -0.01em): page headings ("שנת 2026", "סידור 2027").
- **Card title** (800, 13.5px, 1.25): card and dialog headings (dialogs use 16px/800).
- **Figure** (900, 30px; 22px on phone, 1.1, tabular): KPI numbers. Footnote figures are 17px/800.
- **Body** (400, 14px, 1.45): running text. Explanatory copy is 12.5px at line-height 1.55.
- **Label** (600, 12px, no letter-spacing): meta lines, legends, weekday names, hints.
- **Grid cell** (700, 11px, tabular): year-grid shift letters. Grid dates, headers and holiday labels are set at 10px.

### Named Rules
**The Ten-Pixel Floor Rule.** No text is set below 10px. The year grid is the densest surface and stops there.

**The Tabular Everywhere Rule.** Every number (dates, counts, clock, KPIs, totals) uses tabular figures in Heebo, so columns of numbers line up like a printed table.

## Layout

The page is a wall with sheets pinned to it. On desktop (900px and up), a fixed 240px dark-ink rail sits at the inline start (212px between 900 and 1100px). A sticky translucent header runs above a content column capped at 1440px, with 22px/24px padding. Cards sit on a 12-column bento grid with a 14px gap: spans of 3, 5, 6, 7 and 12 collapse to 6 below 1180px and to full width below 1060px.

Below 900px the rail is removed. A fixed bottom tab bar (52px items, safe-area padded) replaces it, the content gutter drops to 12–14px, the bento becomes two columns with a 10px gap, and the header drops the profile and clock caption. Under 600px the month grid tightens (4px gap, 66px cells). Under 380px the clock is hidden.

Rhythm is 4/8-based with 14px and 16px as the working steps: 16px card padding, 14px between stacked cards and under card heads, 8px inside the week strip (5px on phone). The week is always seven equal columns. The year grid is a fixed-layout table with a 960px minimum width that scrolls horizontally inside its sheet on phones.

Dialogs are bottom sheets on phones (20px top corners, rising on the drawer curve) and centred panels at 900px and up (11px corners, offset to clear the rail).

## Elevation & Depth

The system is flat print. Sheets separate from the wall by tone and a hairline, plus a 1px contact shadow that is barely visible. Depth is real only for things that float above the sheet: dialogs, the shift picker and the toast. In the night theme, card shadows are removed entirely and only the floating layers keep a deep shadow. Sticky bars use translucency and blur (header at 92%, tab bar at 96%, blur 16–18px). Under reduced transparency they turn opaque.

### Shadow Vocabulary
- **Sheet contact** (`box-shadow: 0 1px 2px rgba(17,24,39,.06)`): every card at rest, board theme only.
- **Sheet lift** (`box-shadow: 0 4px 14px rgba(17,24,39,.08)`): hover on clickable cards (pointer devices). The card does not move.
- **Floating layer** (`box-shadow: 0 12px 32px rgba(17,24,39,.16), 0 2px 6px rgba(17,24,39,.08)`): dialogs, the shift picker and the toast. Night: `0 18px 44px rgba(0,0,0,.5)`.

### Named Rules
**The No-Glow Rule.** Nothing emits light. No outer glows, inner glows, text shadows, pulsing dots or radial spotlights. A state is shown by an ink frame, a tone change or the pen colour.

## Shapes

Small, quiet radii on all chrome: 5/7/9/11px, with 7px for controls, 9px for week cells and the matrix sheet, 11px for cards, and 20px only for the top of a bottom sheet. Rules are 1px hairlines. Nested content is separated by row rules, not boxes inside boxes.

The one irregular shape in the system is the highlighter stroke. It is an SVG mask (viewBox 120×40, stretched to the element) with a slightly bowed top and bottom edge and jagged, torn-looking ends. There are three fixed variants, one per shift (`--stroke-a`, `--stroke-b`, `--stroke-c`), so each shift keeps the same "hand" everywhere. The stroke bleeds a few pixels past the letter's box on the inline axis (4px on chips, 18px on the hero letter) the way a real swipe overshoots.

Calendar state is drawn with a fixed frame vocabulary on top of the marker, never instead of it:
- today: a 2px ink frame
- holiday: a 2px holiday-red frame
- training: a 2px violet frame
- minor holiday: a 2px ochre underline
- changed in draft: a 3px ink underline
- coverage gap: a 1.5px red frame on an empty sheet cell
- balance day: a small ink dot printed on the marker

## Components

### Buttons
Plain printed controls with a pen-blue primary.
- **Shape:** gently squared (7px), 42px tall, 13px/700 label, 16px inline padding, 16px icons.
- **Primary:** ballpoint blue fill with white text. No shadow.
- **Hover / Focus / Active:** primary deepens to ballpoint blue deep. Ghost moves to sheet shade. Focus is a 2px ballpoint-blue outline with a 2px offset. Press scales to 0.97 on touch and mouse. Disabled drops to 45% opacity.
- **Ghost:** a white sheet with a strong hairline and ink text. This is the default secondary.
- **Header buttons:** 40px square-ish icon buttons, white with a strong hairline and muted ink.

### Chips (shift letters)
- **Style:** the shift letter (800, 12–13px) printed in ink on its highlighter stroke. The box itself is transparent and borderless.
- **State:** no shift means a quiet sheet-shade chip with muted text. In the picker the current choice gets a 2px ink outline. A draft edit adds an ink underline.

### Cards / Containers
- **Corner Style:** 11px.
- **Background:** sheet white on the wall gray.
- **Shadow Strategy:** sheet contact at rest, sheet lift on hover (see Elevation).
- **Border:** 1px hairline.
- **Internal Padding:** 16px. Card heads are a 13.5px/800 title with a plain 18px ink line icon. There are no coloured icon tiles.
- **Rows inside cards:** hairline-ruled rows (holiday list, fairness table), not nested boxes.

### Inputs / Fields
- **Style:** white sheet, strong hairline, 7px, 44px tall, 13px padding, 14px text (16px on touch so the field does not zoom). Caret in ballpoint blue.
- **Focus:** the border turns pen-tinted with a 3px ballpoint wash halo.

### Navigation
- **Rail (desktop):** dark-ink slab, 240px. Items are 14px/600 rail-muted with 18px line icons. Hover is rail-ink-raised. Active is rail-ink-raised with rail text, a yellow icon and a 4px yellow tick at the inline start edge. Group labels are 11.5px/600 rail-muted with no tracking. The app mark is a yellow highlighter stroke with an ink icon. The foot carries a "now" card with the current shift as an inline marker word.
- **Bottom tab bar (phone):** five 52px items with 21px icons and 11.5px/700 labels. Active is ballpoint wash behind blue-deep text with a 3px blue tab on top. An amber pip marks pending work.
- **Segmented control:** a white sheet holding equal options. The active option is filled ballpoint blue.

### The Highlighter (signature)
The irregular marker swipe behind every shift letter, at every scale: the 96px hero swipe, the inline marker word in running text ("משמרת ב׳"), the week and month chips, the legend swatches, the 15px year-grid cells and the app mark. Colour comes from the shift, shape from that shift's stroke variant, and the ink letter always sits on top. It renders as a masked pseudo-element behind the content, so the element keeps its layout and text stays real text.

### Now Hero
The first thing on the overview: a sheet with the on-duty shift letter at display size on its marker, a 27px headline naming the shift, the date in muted ink, and tomorrow's shift as an inline marker word. No tags, rings or brackets.

### Roster Cells (week, month, year)
White sheet cells, with the weekend band on Friday and Saturday, holiday names in holiday ink, today in an ink frame, and the shift chip inside. Month cells are 92px tall (66px on phones). Year cells are 15px marker strips under a 10px date row and a holiday-label row.

### Footnote Line
Fairness totals are written as a single wrapping line of 13px muted label plus 17px/800 tabular figure pairs, each shift's figure beside its marker word. Only a bad value turns error red.

### Toast with Undo
A sheet-shade bar at the bottom, 9px radius, floating-layer shadow. When an action can be reversed it carries a 36px ballpoint-wash "undo" button. It rises from below on a 0.4s ease.

### Motion
Short and physical. State changes take 0.15s, press feedback 0.16s on `cubic-bezier(.23,1,.32,1)`, views fade up 4px in 0.2s, and bottom sheets rise on `cubic-bezier(.32,.72,0,1)` over 0.3–0.44s. Reduced motion keeps short opacity fades and removes slides, scales and loops.

## Do's and Don'ts

### Do:
- **Do** put every shift letter on its own highlighter stroke (א׳ #ffe14a, ב׳ #ffb2d6, ג׳ #a6e3a0) in ink #161b22, at every scale from the hero to the year grid.
- **Do** draw calendar state as ink frames and underlines over the marker: today 2px ink, holiday 2px red, training 2px violet, minor holiday ochre underline, draft change 3px ink underline.
- **Do** keep chrome paper-and-ink: white sheets on wall gray, 1px hairlines, 5–11px radii, ballpoint blue as the single action colour.
- **Do** write status in words and fairness as footnote lines with tabular figures, and turn only the offending number red.
- **Do** separate content inside a sheet with hairline rows rather than boxes inside boxes.
- **Do** keep holidays in red ink and weekends in the faint gray band, like a printed Hebrew calendar.

### Don't:
- **Don't** use glow, pulsing, text-shadow, radial spotlights, background grids or corner brackets. That is the command-center dashboard this world replaced.
- **Don't** use the highlighter colours for anything but the three shifts, and don't show a shift colour without its letter.
- **Don't** fill a holiday or weekend cell with red or gray instead of its shift marker. The marker stays and the calendar mark goes on top.
- **Don't** put coloured icon tiles in card heads or coloured status pills. Icons are plain ink line icons, and status is a word.
- **Don't** set text below 10px.
- **Don't** add decorative gradients. The only radial gradients in the system draw printed dots (the balance-day dot and the holiday legend dot).
