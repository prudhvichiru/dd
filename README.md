# Dementia Diagnostics — website

A six-page site built on the DD brand guidelines (v3) and the Storyfolk logo artwork.

## What's here

| File | What it is |
|---|---|
| `index.html` | The whole site. Self-contained: open it in a browser, or drop it on any host. |
| `logo.svg` | The primary logo, single-colour vector. It inherits `currentColor`, so it takes the colour of the surrounding text. |
| `src/` | The generator used to build `index.html`. Run `python3 build_site.py`. |

## Pages

Navigation is hash-based (`#assessment`, `#families`, `#gps`, `#clinicians`, `#privacy`).
When this is rebuilt in the DD React stack these should become real paths. Hash routes
do not rank separately in search, and SEO is the main reason the site is split into
pages at all.

- **Home** — the conversion page, ending in the enquiry form
- **The assessment** — what happens, step by step
- **Families & carers** — including how to raise it with someone
- **For GPs** — referral pathway and what comes back
- **Our clinicians** — the model and the standards
- **Privacy** — draft, plain-language

## Availability

The site states in four places that **video consultations begin mid-2027**: the hero,
the how-it-works step, the consultation section of the assessment page, the enquiry
panel, and the GP page. If that date moves, search `mid-2027` and change all of them.

## Before this goes live

1. **Wire the enquiry form.** It currently shows a confirmation and sends nothing.
   Fields: who, first name, postcode, phone, email, best time, free text, marketing opt-in.
   Keep the marketing consent separate from the clinical enquiry. That separation is a
   privacy requirement, not a design choice.
2. **Legal review of the privacy page.** It is written to be read, not to be complete.
3. **Add contact details** and practitioner registration numbers.
4. **Replace the illustrations.** Every image sits in a `<figure class="shot">` with a
   fixed aspect ratio. Delete the `<svg>` inside and paste an `<img src="..." alt="...">`;
   the frame and crop hold. Shot list: an older person with their adult child (square),
   an older person with a carer (4:3), a clinician with a patient (4:3), someone on a
   video call at home (22:15).
5. **Check the Medicare rebate wording** on the assessment page against the final
   billing position.

## Brand notes

- Type is Halyard Display, which is licensed and not servable from here. The stack asks
  for `"Halyard Display"` first and falls back to Figtree from Google Fonts. Self-host the
  licensed Halyard files on the production server and it will pick them up.
- Colours follow the guidelines: light tints carry backgrounds, full-strength brand colour
  is reserved for buttons, icons and highlighted words.
- Dark mode uses the documented Blue Dark background pairing rather than an inversion.
- The logo deck lists Blue Dark as `#1F146B`; the brand guidelines say `#201371`. This build
  uses the guidelines value. Worth reconciling.

## Compliance points baked in

- No testimonials or patient stories anywhere. Ahpra prohibits them in advertising for
  regulated health services.
- No diagnostic or accuracy claims. The site promotes the clinician-led service, not a
  test or a result.
- The footer states that assessment and diagnosis are carried out by a clinician, not by
  software.
- The illustrations are drawings, not photographs, so no one can be mistaken for a real
  patient. If you swap in photography, don't caption it in a way that implies the people
  shown are patients of the clinic.
