# Contributing to Free AI API Tiers

Thanks for keeping the list accurate! All data lives in `data/providers.json`.

## Adding / updating a provider

1. Fork and create a branch.
2. Edit `data/providers.json`. Each entry:
   ```json
   {
     "name": "Provider Name",
     "url": "https://official-pricing-page",
     "category": "api | gateway | self-host | chat",
     "free_tier": "What you get for free, with rough limits.",
     "promo": "Active promo description, or null if none.",
     "credit_card": false,
     "last_verified": "YYYY-MM-DD"
   }
   ```
3. Run `python generate.py` to rebuild the README table.
4. Set `last_verified` to today's date when you confirm the info.
5. Open a PR with a clear title.

## Rules

- Only include **genuine** free tiers or active promos — not expired trials.
- `credit_card: false` means no card is needed for the free tier.
- Use official pricing/landing pages as `url`.
- Keep descriptions factual and short.

## Code of Conduct

Be respectful; we follow the [Contributor Covenant](https://www.contributor-covenant.org).
