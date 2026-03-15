# Project Ray
```mermaid
graph TD
    User([使用者輸入]) --> Filter1{輸入端偵測}
    
    subgraph Defense_Layer_1 [第一層：前端過濾]
    Filter1 -- "偵測到 Injection" --> Block1[直接攔截]
    style Block1 fill:#f96,stroke:#333,stroke-width:2px
    end

    Filter1 -- 安全 --> RAG[RAG 檢索資料]
    
    subgraph Defense_Layer_2 [第二層：內容分析]
    RAG --> Filter2{檢索內容意圖分類}
    Filter2 -- "發現惡意指令" --> Cleanse[資料清洗與重導向]
    style Cleanse fill:#f96,stroke:#333,stroke-width:2px
    end

    Filter2 -- 安全 --> LLM[LLM 生成回覆]
    LLM --> Output([輸出結果])
## ⚡ AI 輕量化實作 (AI Optimization)
為了確保防禦層不影響 RAG 的回應效率，我們實作了模型量化技術：

| 評估指標 | 基準模型 (Standard LLM) | PromptGuard (我們的輕量化版本) | 優化成果 |
| :--- | :--- | :--- | :--- |
| **參數量** | 7 Billion | **110 Million** | **降低 98%** |
| **記憶體佔用** | ~14 GB | **< 500 MB** | **節省 96%** |
| **偵測延遲** | ~2500 ms | **< 50 ms** | **提升 50 倍** |

>
