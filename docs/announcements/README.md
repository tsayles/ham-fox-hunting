# Fox Hunt Email Announcements

This directory contains Thunderbird-compatible `.eml` draft files for
publicizing M&K ARDF fox hunt events on the club mailing lists.

---

## Mailing List Recipients

All emails go to both lists:

- **FoxHunting@mkarc.groups.io** — fox hunt dedicated list
- **MKARC@mkarc.groups.io** — general Mike & Key club list

---

## How to Use the .eml Files

Each `.eml` file is formatted as a Thunderbird draft message. To use:

1. Open **Thunderbird**.
2. Go to **File > Open Saved Message** and select the `.eml` file.
3. In the message view, choose **Edit > Edit as New Message**
   (or press **Ctrl+E** / **Cmd+Shift+E** on macOS) to open a
   compose window with the email ready to send.
4. Review all content, fill in or remove any remaining
   `[bracketed placeholders]`, and verify dates before sending.
5. Add yourself to the `From:` field if Thunderbird does not
   auto-populate it from your account.

Alternatively, copy an `.eml` file into your Thunderbird **Drafts**
mail folder. Files that include the `X-Mozilla-Draft-Info` header
will then open directly in compose mode when double-clicked inside
Thunderbird.

---

## 2026 Sending Schedule

All 2026 event dates are **tentative**. Confirm each date at least
one week before the scheduled send, and update the email body if
the event date changes.

### Season Kickoff

| File | Recommended Send Date | Purpose |
|------|-----------------------|---------|
| `2026/2026-07-20-season-kickoff.eml` | Mon Jul&nbsp;20, 2026 | Announce the remaining 2026 hunt schedule |

### August Hunt — Marymoor Park, Redmond (Sat Aug 22)

| File | Recommended Send Date | Purpose |
|------|-----------------------|---------|
| `2026/2026-08-08-august-hunt-announcement.eml` | Sat Aug&nbsp;8, 2026 | Two-week announcement |
| `2026/2026-08-15-august-hunt-reminder.eml` | Sat Aug&nbsp;15, 2026 | One-week reminder |
| `2026/2026-08-21-august-hunt-day-before.eml` | Fri Aug&nbsp;21, 2026 | Day-before details |

### September Hunt — West Snohomish County Mobile Hunt (Sun Sep 20)

| File | Recommended Send Date | Purpose |
|------|-----------------------|---------|
| `2026/2026-09-05-september-hunt-announcement.eml` | Sat Sep&nbsp;5, 2026 | Two-week announcement |
| `2026/2026-09-13-september-hunt-reminder.eml` | Sun Sep&nbsp;13, 2026 | One-week reminder |
| `2026/2026-09-19-september-hunt-day-before.eml` | Sat Sep&nbsp;19, 2026 | Day-before details |

---

## Generic Templates

The `templates/` directory contains reusable templates for future
seasons. Replace every `[BRACKETED PLACEHOLDER]` before sending.

| File | Purpose |
|------|---------|
| `templates/season-kickoff.eml` | Announce a new hunt season |
| `templates/hunt-announcement.eml` | Announce a hunt 2–3 weeks out |
| `templates/hunt-reminder.eml` | One-week-before reminder |
| `templates/hunt-day-before.eml` | Day-before final details |
| `templates/post-hunt-summary.eml` | Post-hunt thank-you and recap |

---

## Notes

- Update `[TOM-EMAIL]` in all 2026 emails with Tom's actual address
  before sending, or remove the email address and keep only the
  callsign.
- For multi-fox hunts or format changes, update the hunt-type
  description and the "What to Bring" section accordingly.
- The August hunt at Marymoor Park must wrap by **2:30 PM** —
  Marymoor Live concerts begin setup at 4 PM.
- The September regional mobile hunt uses the defined west Snohomish
  County hunt area; start/finish specifics are sent closer to hunt day.
