---
name: buyer-read
description: Works out how one specific person communicates, what drives them and how to approach them before you reach out, call or pitch. Use when a seller says "who is this person", "how should I approach them", "read this prospect", "prep me on this contact", "I have a call with them in two minutes", "this profile came back thin", "they changed jobs", or "this is the wrong person". Prevents pitching everyone the same way, and prevents trusting a profile that is thin, stale or of the wrong person.
---

# Buyer Read

Build an honest read on one person: how they communicate, what they respond to, what puts them off, and what they will worry about in a buying decision.

**The mistake this prevents.** Sellers pitch every buyer the same way, then blame the buyer when it does not land. The second mistake is quieter: trusting a profile that is thin, out of date, or of a different person with the same name, and walking into the call confident and wrong.

## What you need

| Tier | What it is |
| :--- | :--- |
| **Minimum** | The person's name, company and role, plus whatever the seller already knows about them |
| **Better with** | Humantic connected. Gives a personality read built from public information, with a confidence level |
| **Best with** | Humantic plus the seller's meeting notes, emails from this person, or CRM history. Anything they have written sharpens the read |

## Steps

1. **Get one identifier.** Ask for the person's LinkedIn URL or their work email. Use one, never both in the same request. If the seller only has a name and company, ask for the LinkedIn URL. Never guess an email address or a company domain, because a guessed identifier builds a profile of the wrong person.

2. **Check for an existing profile before building one.** Fetch first. Only create a new profile if nothing exists. Ask for the sales view of the profile where the tool offers a choice of lens.

3. **Check it is the right person.** Compare the name, current role and company in the profile with what the seller expects. If it is someone else, record the wrong match with the flag tool, giving the correct identifier, then build the profile for the correct one. Tell the seller you did this.

4. **Check it is good enough to use.** Look at the confidence the profile reports.
   - **Thin or low confidence:** ask the seller for anything the person has written or said: a bio, a recent post, notes from a call, an email thread. Then enrich the profile with that text using the update tool, and say whether the read changed.
   - **Out of date because they changed job or company:** rebuild it from current sources with the refresh tool. If no refresh tool is available in this connection, say so and enrich the profile with the new role details instead.
   - Enriching and rebuilding fix different problems. Pick the one that matches the situation and say which you chose.

5. **Give the read in plain sales language.** No personality-model jargon unless the seller uses it first. Cover:
   - How they communicate: pace, level of detail, how direct to be
   - What to lead with, and what to avoid
   - What drives them, and what they are likely to worry about in a buying decision
   - The kind of question they will answer properly
   - One line on how confident the read is and why

6. **Match the length to the moment.** If the seller is about to join a call, give three points and nothing else. If they want something to paste into notes or share with a manager, give a clean block, or ask the profile tool for HTML or PDF when they want a shareable file.

7. **Close the loop.** Ask whether the read matched the person once they have spoken. If the seller says it was useful, not useful, or inaccurate, record that with the flag tool. It takes seconds and improves every future read.

## If Humantic is not connected

Say so once, in one line, and point to the setup guide. Then build the best read available from what the seller provides and, if the assistant can search the web, from the person's public writing. Label every point as inference. Never infer personality from a job title, age, gender, nationality or photo.

## Humantic tools this skill uses

Tool names can carry a prefix or a version suffix depending on the assistant. Match on the part shown here.

| Job | Tool |
| :--- | :--- |
| Read an existing profile | `humantic_pi_profile_fetch` |
| Build a profile from one identifier | `humantic_pi_profile_create` |
| Enrich a thin profile with supplied text | `humantic_pi_profile_update` |
| Rebuild a profile from current sources | `humantic_pi_profile_refresh`, where available |
| Record a wrong match, or accuracy and usefulness feedback | `humantic_pi_profile_flag` |

## Rules

- A personality read is a guide to approach, not a verdict on the person or the deal.
- Say where each point came from: the Humantic profile, something the seller supplied, or inference.
- Never put personality labels or the read itself into anything the buyer might see.
- Surface low confidence. A weak read presented confidently is worse than no read.
