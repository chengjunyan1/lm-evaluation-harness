# lm_eval/tasks/smollm_12_5_corpus/utils.py

def process_cosmopedia_v2(doc):
    return f"Audience: {doc['audience']}\n\nPrompt: {doc['prompt']}\n\nResponse: {doc['text']}"

def process_deepmind_math_small(doc):
    return f"Question: {doc['question']}\n\nAnswer: {doc['answer']}"

def process_stackoverflow_clean(doc):
    return doc['content']
