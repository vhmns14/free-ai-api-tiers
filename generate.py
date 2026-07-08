#!/usr/bin/env python3
"""Generate the provider table in README.md from data/providers.json.

The table is inserted between <!-- TABLE_START --> and <!-- TABLE_END --> markers,
so the rest of README (intro, contributing) is preserved.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "providers.json")
README = os.path.join(HERE, "README.md")
START = "<!-- TABLE_START -->"
END = "<!-- TABLE_END -->"


def build_table(providers):
    rows = ["| Provider | Category | Free tier | Free models | Promo | Card? | Verified |",
            "| --- | --- | --- | --- | --- | --- | --- |"]
    for p in providers:
        promo = p.get("promo") or "—"
        card = "❌ no" if not p.get("credit_card") else "⚠️ yes"
        fm = ", ".join(p.get("free_models", [])) or "—"
        rows.append(
            f"| [{p['name']}]({p['url']}) | {p['category']} | {p['free_tier']} "
            f"| `{fm}` | {promo} | {card} | {p.get('last_verified','')} |"
        )
    return "\n".join(rows)


def main():
    with open(DATA) as f:
        data = json.load(f)
    providers = data["providers"]
    table = build_table(providers)

    if os.path.exists(README):
        with open(README) as f:
            text = f.read()
        if START in text and END in text:
            before, _ = text.split(START, 1)
            _, after = text.split(END, 1)
            text = f"{before}{START}\n{table}\n{END}{after}"
        else:
            text = f"{text}\n{START}\n{table}\n{END}\n"
    else:
        text = f"# Free AI API Tiers\n\n{START}\n{table}\n{END}\n"

    with open(README, "w") as f:
        f.write(text)
    print(f"wrote table with {len(providers)} providers to README.md")


if __name__ == "__main__":
    main()
