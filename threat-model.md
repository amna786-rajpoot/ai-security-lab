
flowchart TD
    U[User request] --> A[Agent loop]
    A <--> L[Local LLM via Ollama]
    A --> T1[read_inbox]
    A --> T2[read_notes]
    A --> T3[send_email]
    T1 --> E[Inbox emails]
    E -. Untrusted email instructions .-> L
    T2 --> S[Private training notes]
    T3 --> O[Simulated sent-email log]

    subgraph Untrusted["Untrusted input boundary"]
        E
    end
    subgraph AgentSystem["Agent and tool boundary"]
        A
        T1
        T2
        T3
    end
