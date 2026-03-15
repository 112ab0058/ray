graph LR
    User([User Prompt]) --> Filter1{Input Guard}
    Filter1 -- Malicious --> Block[Block/Log]
    Filter1 -- Clean --> RAG[RAG Retrieval]
    RAG --> Filter2{Context Guard}
    Filter2 -- Poisoned --> Cleanse[Data Cleansing]
    Filter2 -- Safe --> LLM[Final LLM Generation]
