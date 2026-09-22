---
name: expansion-play
description: Finds what else an existing customer should be buying, who to raise it with, and when, after checking the current deployment is demonstrably working. Use when a seller or account manager says "upsell this account", "cross-sell opportunity", "where can we expand", "whitespace in this account", "grow this customer", "who else in the company could use us", or "is now the time to ask for more". Prevents raising an expansion on a deployment that is struggling, which puts the renewal at risk, and asking for more without a real trigger.
---

# Expansion Play

Finds the next thing this customer should buy, and times the ask to a real reason.

**The mistake this prevents.** Asking an existing customer for more while their current rollout is struggling. It tells them you care about the number more than the result, and it puts the renewal at risk. The second mistake is asking with no trigger, so the request reads like quota season rather than a response to something that changed at their end.

## What you need

| Tier | What it is |
| :--- | :--- |
| **Minimum** | What the customer has today, who uses it, and how the seller thinks it is going |
| **Better with** | Humantic connected. Gives buyer signals at the account, account research on teams and initiatives, and a read on new stakeholders |
| **Best with** | Humantic plus CRM, usage data and support history, so the health check runs on evidence rather than impression |

## Steps

1. **Check the current deployment first.** Establish what the customer has, who uses it, and whether it is working, in evidence rather than feeling: usage, results the customer has named, open issues, sponsor sentiment. Give a verdict: working, mixed, or struggling.
   - **Struggling:** stop. Recommend fixing adoption before any expansion ask and say what would need to be true first.
   - **Mixed:** continue, but name the risk in the output and scope the ask small.
   - **No evidence either way:** say so, and list what the seller needs to confirm before asking.

2. **Find the whitespace.** Where else could value land: other teams, regions, business units, use cases or products. Use the Humantic account research sections on leadership, organisation and initiatives, plus CRM and what the seller knows. Mark each as found or inferred.

3. **Find the trigger.** Pull buyer signals for the account: a new leader, a hiring push, a new initiative, an acquisition, a budget cycle. State the window the signals covered. Pick the one that makes an ask timely. If nothing qualifies, say the ask can wait and name what to watch for.

4. **Find the people.** Who owns the new budget or team, and who arrived since the original sale. Fetch or build Humantic profiles for them. If the original sponsor has changed role, rebuild their profile from current sources. Decide who introduces the seller to the new owner, usually the existing sponsor.

5. **Build the case in their numbers.** The results the current deployment has delivered, stated in the customer's terms, and what the same result would be worth in the new team or use case.

6. **Deliver the expansion brief.**
   - **Health check verdict**, with the evidence
   - **The whitespace**, ranked
   - **The trigger**, and why now
   - **The people**: new owner, sponsor, who makes the introduction, and how to approach each
   - **The ask**: what, to whom, when, and the smaller fallback ask
   - **Risks**, including any risk to the renewal
   - **Next three steps**, each with an owner and a date

7. **Offer the next step.** Offer to draft the introduction request or the ask with the sales-email skill, or to map a new buying group with the buying-committee skill.

## If Humantic is not connected

Say so once and point to the setup guide. Run the health check and whitespace from CRM, usage data and the seller's knowledge, and mark the trigger as a hypothesis.

## Humantic tools this skill uses

Tool names can carry a prefix or a version suffix depending on the assistant. Match on the part shown here.

| Job | Tool |
| :--- | :--- |
| Find the trigger | `humantic_signals_per_account` or `humantic_signals_list` |
| Organisation, leadership and initiatives | `humantic_miia_report_list`, `humantic_miia_report_sections_list`, `humantic_miia_report_section_get`, `humantic_miia_report_refresh` where available |
| Read new stakeholders and a sponsor who moved | `humantic_pi_profile_fetch`, `humantic_pi_profile_create`, `humantic_pi_profile_refresh` where available |

## Rules

- The health check always runs first. No verdict, no ask.
- Separate what was found from what was inferred.
- Never put personality reads into anything the customer might see.
