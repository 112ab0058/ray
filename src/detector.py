import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class PromptGuardDetector:
    """多層次提示注入偵測器 - 智慧創新大賞參賽版本"""
    def __init__(self, model_path="bert-base-uncased"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        # 這裡可以強調輕量化 (Quantization)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_path)
        
    def check_injection(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.model(**inputs)
        return torch.softmax(outputs.logits, dim=1)

# TODO: 整合至 RAG 流水線
