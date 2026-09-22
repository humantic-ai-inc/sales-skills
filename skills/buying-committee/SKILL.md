---
name: buying-committee
description: Maps and manages the group of people who decide on a deal, covering how each person thinks, where they will agree and clash, who to approach in what order, how to equip a champion, and who is missing. Use when a seller says "map the buying committee", "who should I talk to first", "multi-thread this deal", "who is my champion", "one stakeholder is skeptical", "I'm presenting to their whole team", or "my champion is being overruled". Prevents single-threaded deals, treating the committee as a list instead of a group, and a champion who gets outranked.
---

# Buying Committee

Maps the people who decide, then works out how to move them as a group.

**The mistake this prevents.** Deals die with one contact who liked the demo. Mapping the names is not enough either. The real work is knowing who moves first, where the group will split, what your champion needs to carry the deal when you are not in the room, and what happens when your champion is outranked.

## What you need

| Tier | What it is |
| :--- | :--- |
| **Minimum** | The deal, and the people the seller knows are involved, with their roles |
| **Better with** | Humantic connected. Gives a read on each member and the account's leadership picture |
| **Best with** | Humantic plus CRM and meeting notes, for who holds which role and who has pushed back on what |

## Steps

1. **List the group.** For each person: name, role, one identifier (a LinkedIn URL or a work email, never both), and known stance: for, against, or unknown. Pull from CRM and meeting notes if connected.

2. **Find who is missing.** Check the list against the roles a deal like this needs: economic buyer, champion, technical evaluator, the lead for the users, procurement or legal. Name every gap. A missing economic buyer is the most important gap to raise.

3. **Read each person.** Fetch or build each Humantic profile. Flag wrong matches with the correct identifier and enrich thin profiles with text the seller supplies, as in the buyer-read skill.

4. **Add the account context.** If Humantic research exists, pull the leadership section and how they evaluate vendors. This shows who really holds authority and what the proposal will be judged against.

5. **Read the group, not just the people.**
   - Where they are likely to agree
   - Where they will pull in different directions, and on what
   - Who influences whom
   - Who will move fast and who needs more convincing

6. **Set the sequence.** Who to approach first, second and third, and why that order.

7. **Plan the champion.** Name the most likely champion and what they need to sell it internally: a one-page summary in their own words, and an answer to the objection their boss will raise. Check whether the champion has enough standing with the economic buyer. If not, plan how to use the champion to get a meeting with the economic buyer rather than relying on them to carry it alone.

8. **Plan for the skeptic.** For each skeptical person, an approach built for them specifically, different from what is working with the rest.

9. **Structure the group meeting**, if one is coming: an order of topics that gives each person what they need without an early clash.

10. **Deliver.** A committee table (Name, Role, Stance, How to approach, What they need), then the fault lines, the sequence, the champion plan, the missing people, and the next three actions, each with an owner and a date.

## If Humantic is not connected

Say so once and point to the setup guide. Map roles, stances and relationships from CRM, notes and what the seller knows, and mark every read of a person as the seller's observation.

## Humantic tools this skill uses

Tool names can carry a prefix or a version suffix depending on the assistant. Match on the part shown here.

| Job | Tool |
| :--- | :--- |
| Read or build each member's profile | `humantic_pi_profile_fetch`, `humantic_pi_profile_create` |
| Fix wrong or thin profiles | `humantic_pi_profile_flag`, `humantic_pi_profile_update` |
| Leadership and vendor evaluation | `humantic_miia_report_list`, `humantic_miia_report_sections_list`, `humantic_miia_report_section_get` |
| Draft one message for several stakeholders | `humantic_content_personalize`, through the sales-email skill |

## Rules

- Treat every read as a starting point to check against what the seller has seen, not a verdict.
- Never put personality reads into anything the buyer might see, including a champion one-pager.
- Say where each point came from: Humantic, a connected tool, the seller, or inference.
