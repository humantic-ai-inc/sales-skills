---
name: meeting-prep
description: Prepares a seller for a specific sales meeting around the one outcome it has to produce, covering who is in the room, how each person takes information, what changed at the account, and the ask plus a fallback ask. Use when a seller says "prep me for my meeting", "brief me on the attendees", "I have a discovery call with", "build a pre-call brief", "prepare me for the renewal conversation", "I'm presenting to their team", or "meeting in an hour with". Prevents walking in with a pitch instead of an outcome, and treating a room of different people as one audience.
---

# Meeting Prep

A one-page brief built around what the meeting has to achieve, and around the actual people who will be in the room.

**The mistake this prevents.** Sellers prepare what they want to say and forget what the meeting has to produce. Then they talk to the room as if it were one person, when the finance lead, the technical evaluator and the champion each want something different from the same hour.

## What you need

| Tier | What it is |
| :--- | :--- |
| **Minimum** | The company, the type of meeting, and who is attending |
| **Better with** | Humantic connected. Gives a read on each attendee, the account research, and recent buyer signals |
| **Best with** | Humantic plus the seller's calendar, CRM and meeting notes, so attendees, deal stage and past conversations come in without the seller typing them |

## Steps

1. **Pin the outcome.** Ask what this meeting has to produce: a next meeting booked, a named decision maker, agreement on scope, a signed order. Then ask for the fallback outcome if the first is out of reach. If the seller does not know, suggest one based on the meeting type and say it is a suggestion.

2. **Get the attendees.** If a calendar is connected, pull them from the invite. Otherwise ask. For each person: name, role, and one identifier, either a LinkedIn URL or a work email, never both.

3. **Read each attendee.** Fetch each person's Humantic profile, and build one where none exists. If a profile is clearly the wrong person or comes back thin, follow the fixes in the buyer-read skill: flag a wrong match, enrich a thin profile with text the seller supplies. For each person, capture how they take information, what to lead with and what to avoid.

4. **Add the account picture.** List existing Humantic research first. If a report exists for this company, pull the executive summary and only the sections that matter for this meeting, for example leadership, how they evaluate vendors, or current vendors. Do not pull the whole report. If none exists, offer to start one and say it runs in the background, usually around two minutes and sometimes fifteen to twenty, so it is best started well before the meeting.

5. **Check what changed.** Pull buyer signals for this account from the last few weeks. Pick the one or two that give a reason to raise something in the meeting. State the window the signals actually covered.

6. **Pull deal context if connected.** From CRM, mail or meeting notes: deal stage, last conversation, open issues, anything promised. If nothing is connected, ask the seller for the last thing that happened with this account.

7. **Write the brief.** One page, in this order:
   - **The outcome**, and the fallback outcome
   - **Who is in the room**: one short block per person on role, how to talk to them, and what to watch for
   - **Where they will pull in different directions**, if more than one person is attending
   - **What changed at the account** that is worth using
   - **How to open**
   - **Two to four questions**, each phrased the way the person it is aimed at will answer properly
   - **The landmine**: the objection or topic most likely to come up, and how to handle it
   - **The ask**, and the fallback ask

## Adjust for the meeting type

- **First discovery call:** focus on pace, how much detail they want up front, how direct to be, and questions that surface the problem behind the stated requirement.
- **Renewal conversation:** lead with the value delivered in their terms, surface open issues before the customer raises them, and name what would make this person hesitate.
- **Group meeting where people want different things:** propose a meeting structure that gives each person what they need, in an order that avoids an early clash.
- **Two minutes to go:** skip the brief. Give the outcome, one line per attendee, and the ask.

## After the meeting

Offer to draft follow-up notes with the sales-email skill, one per attendee rather than one group email, each built on what that person said.

## If Humantic is not connected

Say so once and point to the setup guide. Build the brief from the calendar, CRM and what the seller knows, and mark the attendee reads as the seller's own observations.

## Humantic tools this skill uses

Tool names can carry a prefix or a version suffix depending on the assistant. Match on the part shown here.

| Job | Tool |
| :--- | :--- |
| Read or build attendee profiles | `humantic_pi_profile_fetch`, `humantic_pi_profile_create` |
| Fix a wrong or thin profile | `humantic_pi_profile_flag`, `humantic_pi_profile_update` |
| Check what research already exists | `humantic_miia_report_list` |
| Start research and check when it is ready | `humantic_miia_report_create`, `humantic_miia_report_status` |
| Read only the sections that matter | `humantic_miia_report_sections_list`, `humantic_miia_report_section_get` |
| What changed at the account | `humantic_signals_per_account` or `humantic_signals_list` |

## Rules

- Say where each point came from: Humantic, a connected tool, the seller, or inference.
- Keep the brief to one page. A brief nobody reads before the call has failed.
- Never put personality reads into anything the buyer might see.
