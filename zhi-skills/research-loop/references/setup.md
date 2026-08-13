# Setup — search backends

The loop needs two backends. Only one requires a key.

## OpenAlex — no key required
Fully open API (`https://api.openalex.org/works`). Nothing to sign up for. The only optional step: enter the "polite pool" for faster, more consistent rate limits by attaching your email to requests.

- Set once: `export OPENALEX_MAILTO="you@example.com"` (add to `~/.zshrc` / `~/.bashrc` / project `.env`).
- Requests then append `&mailto=$OPENALEX_MAILTO`. If unset, OpenAlex still works on the common pool — this is a courtesy, not a requirement. You may ask for email.

## Valyu — API key required
Semantic search; needs an account and key.

1. Sign up at valyu.ai and create an API key from the dashboard. (The exact dashboard path changes — if unsure, check the current docs at docs.valyu.ai rather than guessing.)
2. Set it: `export VALYU_API_KEY="sk-..."` (persist it in your shell profile or project `.env`; don't hardcode it into the skill or any committed file).
3. Verify: `[ -n "$VALYU_API_KEY" ] && echo ok`.

## Guiding the user (agent instructions)
When the setup gate reports Valyu missing:
- Explain plainly that OpenAlex is keyless and Valyu needs one free key, so setup is a single step. But if the user has an OpenAlex API key, use that.
- Ask whether they've already got a Valyu account/key. If yes, have them export `VALYU_API_KEY` and re-verify. If no, point them to valyu.ai to create the key, then export it.
- Prefer not to ask the user to paste the key into the chat. If they do paste one, do not echo it, do not put it in shell history, and do not hardcode it into files; ask them to export it locally or use a secure MCP/secret mechanism, then only confirm presence via the `[ -n "$VALYU_API_KEY" ]` check.
- If the user says to proceed without fixing the missing key, state the degraded search mode explicitly. Do not silently replace semantic recall with generic web search and then present the result as a complete research-loop pass.
- Once verified, proceed to Frame. Do not re-run setup on later invocations.

## MCP alternative
If the user has installed Valyu / OpenAlex / arXiv **MCP servers**, prefer those tools over raw HTTP — they handle auth and pagination. In that case the env-var checks above may be unnecessary; confirm the MCP tools are listed and reachable instead, and skip the key export.
