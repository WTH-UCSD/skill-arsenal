# Local Project Configuration

The distributable skill does not track a private or host-specific ChatGPT Project. A local installation is configured only when this skill directory contains:

```text
references/project.local.toml
```

with:

```toml
[project]
name = "Visible ChatGPT Project name"
url = "https://chatgpt.com/..."
```

`url` is required. `name` is strongly recommended because it provides an independent visible-identity check in the browser.

## Installation Contract

Installing this skill is one task with two required parts:

1. install or link the tracked skill package;
2. create and validate `references/project.local.toml`.

Obtain the Project URL and visible name from explicit user input or a verified existing host-local configuration. Never infer them. When migrating an older configuration, copy only the `[project]` values; browser connection details and model labels belong to their respective runtime and UI layers.

Use `scripts/configure.py` to create the local reference without exposing its values in repository history. Pass either `--project-url` and `--project-name`, or `--from-toml /path/to/an/existing-config.toml`. The script refuses to replace different existing values unless `--force` is explicit.

Validate that the file parses as TOML, contains a nonempty HTTPS Project URL on `chatgpt.com` or one of its subdomains, and is not tracked by the source repository. When browser access is available during setup, open the URL without submitting a prompt and verify that the signed-in Project identity matches `name`.

The standard skill download step does not supply host-local values. An installer or setup agent must therefore perform the configuration step explicitly and must report the installation as incomplete if it cannot do so.

## Runtime Overrides

An explicit Project target for the current request, followed by the nearest current-project instructions, overrides this installation-wide local default without rewriting it. Broader host instructions are a final fallback when none of those sources resolves a target.
