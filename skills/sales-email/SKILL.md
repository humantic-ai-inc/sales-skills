---
name: sales-email
description: Writes or rewrites a sales email matched to the person receiving it, covering first-pitch emails, rewrites of a draft, replies, follow-ups after silence, one message to several stakeholders, and post-meeting notes. Use when a seller says "write a cold email to", "rewrite this for", "help me reply", "they went quiet, write a follow-up", "email the buying group", "follow up after the meeting", or "make this email land". Prevents emails written about the sender instead of the reader, templates that ignore who is reading, and emails that should not be sent at all.
---

# Sales Email

Emails that fit the person reading them, with one idea and one ask.

**The mistake this prevents.** Most sales emails are about the sender, written to a template, and sent because the sequence said so. The reader can tell in one line. The first check is whether this email should exist at all. The second is whether it reads like it was written for this person.

## What you need

| Tier | What it is |
| :--- | :--- |
| **Minimum** | Who the email is for, what the seller wants to happen, and the context: the pain point, the draft, or the earlier thread |
| **Better with** | Humantic connected. Drafts matched to how the recipient responds to messages |
| **Best with** | Humantic plus mail, so the thread comes in without pasting, and meeting notes for post-meeting follow-ups |

## Pick the mode

| Mode | Use it when | Must have |
| :--- | :--- | :--- |
| **First pitch** | Cold outreach | The pain point being led with, and who the seller is and why they are reaching out. Each at least a sentence, neither an essay |
| **Rewrite** | The seller already wrote it | The draft |
| **Reply** | They wrote back | The earlier message and their reply |
| **Follow-up** | They went quiet | The last message sent |
| **Several stakeholders** | Multi-threading one deal | Each person's name, role and one identifier, plus the core message |
| **Post-meeting notes** | After a meeting with several people | Who attended and the key takeaway |

If a must-have is missing, ask for it. A pitch with a blank pain point comes back generic.

## Steps

1. **Check the email should exist.** A follow-up needs a new reason: a signal at the account, a useful insight, an answer to something they asked. If there is none, suggest one or recommend not sending yet. Say this plainly.

2. **Get the reader.** One identifier per person, a LinkedIn URL or a work email, never both. If a Humantic profile exists, fetch it. The personalization tool also works without a pre-built profile.

3. **Draft with the personalization tool** in the matching mode, then apply the craft checks below. For several stakeholders, draft each separately around the same core message, then check the versions do not contradict each other.

4. **Apply the craft checks.**
   - One idea and one ask. Cut everything else.
   - Open with an observation about them, not a claim about the seller.
   - Use their words for their problem, taken from their posts, the thread or the account research.
   - Keep a cold email short enough to read on a phone without scrolling.
   - Make the ask easy to say yes to: a specific time, a yes or no question, one link.
   - Plain subject line. No false familiarity, no "just checking in", no "hope this finds you well".

5. **Deliver.** The subject line and body, one alternative subject line, and one line on why the email is shaped this way for this reader. If mail is connected, offer to save it as a draft. Never send without the seller saying so.

## If Humantic is not connected

Say so once and point to the setup guide. Write from the craft checks, and ask the seller to paste something the recipient wrote so the register can be matched by hand.

## Humantic tools this skill uses

Tool names can carry a prefix or a version suffix depending on the assistant. Match on the part shown here.

| Job | Tool |
| :--- | :--- |
| Write or rewrite matched to the reader, in first pitch, rewrite, reply or follow-up mode | `humantic_content_personalize` |
| Read the recipient first | `humantic_pi_profile_fetch` |

## Rules

- Never put personality labels or the read itself into the email.
- Never guess a recipient's email address.
- Drafts only. The seller sends.
