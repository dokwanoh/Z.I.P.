# Hackathon Story

Z.I.P. starts from a concrete pain: coding agents are useful, but repeated context and multilingual restatement can make every iteration expensive.

The project avoids a common trap: claiming a universal prompt-compression win. Instead, it treats compression as a routed experiment. A debugging task can often tolerate RTK and headroom pruning. A design review or security task should usually stay conservative. Caveman-style shortening is intentionally behind a risk gate because terse prompts can increase response length or lose intent.

The demo path is simple: run the benchmark, inspect `reports/latest.md`, and show where Z.I.P. saved tokens, where it refused unsafe compression, and where the dry-run evidence is not enough for a production claim.
