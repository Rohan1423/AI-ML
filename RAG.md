Use Cases : Customer Support, Medical Diagnosis, Legal, Finance, Compilance & Research

Benefits of RAG over tradition LLMs :-
i. Reduce Hallucination -> Make up facts, False Info.
ii. Keep Knowledge Up-to-date -> Knowledge Cutoff Date
iii. Cost Effective ->  Train Model / Fine Tune everytime to stay up-to-date
iv. Maintain Data Privacy -> Model can't access entire company DB at a time

-> Complete RAG Pipeline :-
Two main Components :-
1) Ingestion Pipeline
2) Retrieval Pipeline

-> 3 things matters a lot when we implement the pipeline :-
1) Chunking strategies : 1. Fixed Sized Chunking
                         2. Hierarchical Chunking
                         3. Semantic Chunking
2) Embedding Model : 1. OpenAI text-Embedding-3-large
                     2. Gemini embeddings
                     3. Sentence Transformers in HuggingFace Ecosystem (like all-miniLm-L6-V2)

3) Vector DB : 1. ChromaDB
               2. FAISS
               3. Pinecone
               4. Elastic Search