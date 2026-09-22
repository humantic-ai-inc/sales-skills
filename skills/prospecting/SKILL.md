---
name: prospecting
description: Builds a short, ranked list of accounts and people to work this week, with a specific reason to reach out attached to every name. Use when a seller says "who should I prospect this week", "build me a target list", "which accounts are in market", "where should I spend my week", "find me accounts to reach out to", or "weekly signal review". Prevents a list with no reason behind each name, which turns every first email into a generic one.
---

# Prospecting

A ranked list of who to work this week, and why each one, now.

**The mistake this prevents.** A prospect list built on fit alone has no reason attached to any name, so every first email says "just reaching out". A list worth working says why this account, why this person, and why this week, and it also says who to leave alone.

## What you need

| Tier | What it is |
| :--- | :--- |
| **Minimum** | The seller's target profile: industry, size, region, the problem they solve, and how many accounts they can work this week |
| **Better with** | Humantic connected. Gives buyer signals across every account with Humantic research, and a read on named people |
| **Best with** | Humantic plus CRM, so the list skips accounts already in play and flags ones that went quiet |

## Steps

1. **Set the target.** Ask for the target profile and a number, defaulting to ten accounts for the week. Ask whether the list should cover accounts the seller already has research on, net new accounts, or both.

2. **Pull what is moving.** Fetch buyer signals across all accounts for the recent window, defaulting to the last fourteen days, filtered to high and medium impact at the source rather than pulling everything. If the feed comes back in pages, page through to the end, or tell the seller plainly that the list is partial. Signals only exist for accounts that already have Humantic research, so say so.

3. **Add the seller's own sources.** If a CRM is connected, pull owned accounts with no recent activity and exclude accounts with open deals already moving. Add any list the seller supplies.

4. **Rank.** Score each account on three things and show the reasoning in a line: in market now, from signal strength and recency; fit against the target profile; and access, meaning whether the seller has a way in. Drop any account with no reason to contact it now, and list those separately.

5. **Name the person.** For each account on the shortlist, name the role to approach first and, where known, the person. For the top five named people, fetch or build their Humantic profile and add one line on how to open with them.

6. **Attach the hook.** Turn each account's strongest signal into a specific reason to reach out. Never "just checking in".

7. **Deliver the list.** A table with these columns: Account, Why now, Who, Opening angle, Next step. Below it, a short list of accounts to leave alone this week and why.

8. **Offer the next step.** Offer to draft first touches for the top accounts with the sales-email skill, or to start Humantic research on net new accounts that look promising.

## If Humantic is not connected

Say so once and point to the setup guide. Build the list from the target profile, the CRM, and public news if the assistant can search the web. Mark each why-now as found or inferred.

## Humantic tools this skill uses

Tool names can carry a prefix or a version suffix depending on the assistant. Match on the part shown here.

| Job | Tool |
| :--- | :--- |
| Signals across every account | `humantic_signals_all_accounts` or `humantic_signals_all` |
| Signals for one account | `humantic_signals_per_account` or `humantic_signals_list` |
| See which accounts already have research | `humantic_miia_report_list` |
| Read the people on the shortlist | `humantic_pi_profile_fetch`, `humantic_pi_profile_create` |

## Rules

- Every account on the list carries a reason. No reason, no place on the list.
- Filter signals by impact and company at the source instead of pulling everything and sorting it.
- Page to the end of the signals feed, or say the answer is partial. A confident partial list is worse than an honest one.
