# Free AI API Tiers 🆓

> A community-curated list of AI API providers that offer a **genuine free tier** or **active promo credits** — no (or minimal) credit card, usable for prototyping and side projects in 2026.

Free here means a *recurring* free tier that resets daily/monthly, not a one-time $5 coupon that vanishes in 30 days. Promos (e.g. opt-in data sharing) are called out explicitly.

The table below is **generated from `data/providers.json`** — edit that file and run `python generate.py` to rebuild.

<!-- TABLE_START -->
| Provider | Category | Free tier | Promo | Card? | Verified |
| --- | --- | --- | --- | --- | --- |
| [Google AI Studio (Gemini)](https://ai.google.dev/gemini-api/docs/pricing) | api | Gemini 2.5 Flash ~1,500 req/day (15 RPM), 2.5 Pro 25 req/day, 1M-token context. Permanent, no expiry. | — | ❌ no | 2026-07-08 |
| [Groq](https://console.groq.com) | api | Llama 4 / Qwen3 / Gemma at ~30 RPM, up to ~14,400 req/day on small models. Very fast (LPU). | — | ❌ no | 2026-07-08 |
| [OpenRouter](https://openrouter.ai/models) | gateway | 29+ free models (DeepSeek, Llama, Qwen, etc.) via one OpenAI-compatible key. No card. | New accounts get free trial credits. | ❌ no | 2026-07-08 |
| [Hugging Face Inference API](https://huggingface.co/docs/api-inference) | api | Thousands of open models, rate-limited per model. No card. | — | ❌ no | 2026-07-08 |
| [Cloudflare Workers AI](https://developers.cloudflare.com/workers-ai) | api | ~10,000 neurons/day, edge inference (Llama, Mistral, FLUX). No card. | — | ❌ no | 2026-07-08 |
| [Cerebras](https://cerebras.ai/product/cerebras-inference) | api | Up to ~1M tokens/day free, 2,000+ tok/s on Llama 3.3 70B. No card. | — | ❌ no | 2026-07-08 |
| [Mistral AI](https://docs.mistral.ai) | api | Le Chat + API experiment tier, all models incl. Large/Codestral at ~1 req/s. No card. | — | ❌ no | 2026-07-08 |
| [NVIDIA NIM](https://build.nvidia.com) | api | 1,000 free credits, Nemotron / Llama / Mistral. No card. | — | ❌ no | 2026-07-08 |
| [Together AI](https://www.together.ai) | api | $1 signup credit, 200+ models (Llama, Qwen, DeepSeek). No card. | — | ❌ no | 2026-07-08 |
| [Fireworks AI](https://fireworks.ai) | api | $1 free credits, fast LLM + image inference. No card. | — | ❌ no | 2026-07-08 |
| [DeepSeek](https://platform.deepseek.com) | api | Free chat web; API is pay-as-you-go (prepaid balance). | Free chat; some new accounts get trial credits. | ❌ no | 2026-07-08 |
| [xAI Grok](https://x.ai/api) | api | Paid API normally; promo credits via data-sharing opt-in. | Up to ~$175/mo free API credits if you opt into data sharing. | ❌ no | 2026-07-08 |
| [GitHub Models](https://github.com/marketplace/models) | gateway | 100+ models with generous daily limits, OpenAI-compatible. No card (GitHub account). | — | ❌ no | 2026-07-08 |
| [Ollama (self-hosted)](https://ollama.com) | self-host | Run Llama, Qwen3.5, Gemma, Hermes locally. Unlimited, no rate limits, no card — needs your hardware. | — | ❌ no | 2026-07-08 |
| [Replicate](https://replicate.com) | api | Free credits for new users; image/video/audio models. | New-account free credits. | ❌ no | 2026-07-08 |
| [Cohere](https://docs.cohere.com) | api | Free tier with monthly usage (embeddings, chat, rerank). No card. | — | ❌ no | 2026-07-08 |
| [SiliconFlow](https://siliconflow.cn) | api | Free (limited) inference for open models (Qwen, DeepSeek, etc.). No card. | — | ❌ no | 2026-07-08 |
| [Zhipu AI (GLM)](https://open.bigmodel.cn) | api | Free tier for GLM models. No card. | — | ❌ no | 2026-07-08 |
| [Alibaba Cloud Model Studio (Qwen)](https://help.aliyun.com/model-studio) | api | Qwen API free (reduced) tier; chat app fully free. No card for trial. | Trial tokens per model for new accounts. | ❌ no | 2026-07-08 |
| [Modal](https://modal.com) | api | $30/mo free compute credits, great for self-hosted inference. | — | ❌ no | 2026-07-08 |
| [OpenAI](https://platform.openai.com/docs/pricing) | api | Limited free tier (GPT-3.5-class) + ChatGPT free chat. Trial credits largely discontinued. | — | ⚠️ yes | 2026-07-08 |
| [Anthropic Claude](https://www.anthropic.com/api) | api | Claude free chat (~30-100 msgs/day). API: one-time starter credit only. | One-time ~$5 API credit for new accounts. | ⚠️ yes | 2026-07-08 |
<!-- TABLE_END -->

## How to use

- Pick a provider with **❌ no** card requirement for zero-friction prototyping.
- Stack 2–3 providers (e.g. Gemini for context, Groq for speed, OpenRouter for variety) to dodge rate limits.
- Most are OpenAI-compatible — change `base_url` + `api_key` and your existing code works.

## Contributing

Found a dead link, an expired promo, or a new free tier? Open a PR editing `data/providers.json`
(see [CONTRIBUTING.md](CONTRIBUTING.md)). A GitHub Action checks links weekly and refreshes this table.

## Disclaimer

Limits and promos change constantly and may differ by region. Always confirm on the provider's official
pricing page before building production workloads. Free tiers usually have **no SLA** and may use your
data for training — review each provider's terms.

## License

[CC0 1.0](LICENSE) — free for any use.
