---
name: pursuit-plan
description: Designs a pursuit of one named target account before the first touch, covering why now, who has to move, the way in, the first three touches, and when to walk away. Use when a seller says "help me break into this account", "plan my pursuit of", "how do I get into this company", "I want to win this logo", "account plan for a new target", or "hunting plan for". Prevents reaching out before knowing why this account should act now, who actually decides, or what would make the pursuit not worth continuing.
---

# Pursuit Plan

A one-page plan for winning one named account you do not yet sell to.

**The mistake this prevents.** Sellers make the first touch before they know why this company should act now, who has to agree, or what would tell them to stop. The pursuit then runs on hope, and a quarter disappears into an account that was never going to move.

## What you need

| Tier | What it is |
| :--- | :--- |
| **Minimum** | The target company, what the seller sells in a sentence, and why they picked this account |
| **Better with** | Humantic connected. Gives account research, recent buyer signals, and a read on named people |
| **Best with** | Humantic plus CRM, for past touches, old opportunities and existing contacts at the account |

## Steps

1. **Frame the pursuit.** Confirm the company, what the seller is selling into it, and why this account. If the reason is only "they are big", say so plainly and treat fit as untested.

2. **Research the account.** List existing Humantic research first. Use an existing report if it is recent; if it is old, offer to regenerate it. If none exists, start one and say it runs in the background, usually around two minutes and sometimes fifteen to twenty. If the company name is ambiguous, ask the seller for the domain rather than guessing. Pull only the sections needed: the executive summary, leadership, how they evaluate vendors, and current vendors or competitive landscape. Say which questions the research could not answer.

3. **Find why now.** Pull buyer signals for the account and pick the strongest trigger: a new leader, a hiring push, an initiative, a funding event, a vendor change. State the window the signals covered. If there is no trigger, say so and write the why-now as a hypothesis the first conversation has to test.

4. **Work out who has to move.** From the leadership section, the CRM and the seller, list the roles that will decide: economic buyer, likely champion, technical evaluator, users, procurement. Mark each as named or unknown. For named people, get a short read from their Humantic profile, or hand over to the buying-committee skill if the group is already large.

5. **Choose the way in.** Decide who to approach first and why, and by which route: direct outreach, a referral from someone the seller knows, an event, or an existing customer relationship. Name the reason that person will care.

6. **Write the plan.** One page:
   - **Why this account**, in one line
   - **Why now**: the trigger, or the hypothesis to test
   - **Who has to move**: a short table of role, name or unknown, and what each cares about
   - **The way in**: first contact, route, and angle
   - **First three touches**, each with a date and a reason to exist
   - **Three things that must be true by quarter end** for this to be a real pursuit
   - **Walk-away signals**: what would tell the seller to stop and spend the time elsewhere

7. **Offer the next step.** Offer to draft the first touch with the sales-email skill, or to map the group with the buying-committee skill.

## If Humantic is not connected

Say so once and point to the setup guide. Build the plan from the seller's knowledge, the CRM, and public research if the assistant can search the web. Mark what was found and what was inferred.

## Humantic tools this skill uses

Tool names can carry a prefix or a version suffix depending on the assistant. Match on the part shown here.

| Job | Tool |
| :--- | :--- |
| Check what research already exists | `humantic_miia_report_list` |
| Start, track and regenerate research | `humantic_miia_report_create`, `humantic_miia_report_status`, `humantic_miia_report_refresh` where available |
| Read only the sections that matter | `humantic_miia_report_sections_list`, `humantic_miia_report_section_get` |
| Find why now | `humantic_signals_per_account` or `humantic_signals_list` |
| Read named people | `humantic_pi_profile_fetch`, `humantic_pi_profile_create` |

## Rules

- Separate what the research found from what you inferred, every time.
- Buyer signals on one account usually cover only the last couple of months, whatever window is asked for. Report the window you actually got.
- A pursuit without walk-away signals is not a plan. Always include them.
