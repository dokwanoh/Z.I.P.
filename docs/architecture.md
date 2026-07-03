# Architecture

Z.I.P. is a four-layer adaptive pipeline.

```mermaid
flowchart TD
  A[Task prompt + repo context] --> B[Workload classifier]
  B --> C[Policy router]
  C --> D1[LinguaRoom]
  C --> D2[Headroom]
  C --> D3[RTK]
  C --> D4[Guarded Caveman]
  D1 --> E[Ponytail patch-first code efficiency]
  D2 --> E
  D3 --> E
  D4 --> E
  E --> F[Fablize quality guard]
  F --> G{pass?}
  G -->|yes| H[Measured result]
  G -->|no| I[Rollback or conservative policy]
```

The harness measures baseline and candidate prompt tokens before making any claim. Policies are composable candidates, not global defaults.
