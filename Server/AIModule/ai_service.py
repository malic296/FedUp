from .iai_service import IAIService
from typing import List, Optional
from deep_translator import GoogleTranslator
from Server.DBModule.db_service import DBService
from Server.DBModule.Models import Category, News
from sentence_transformers import SentenceTransformer
from transformers import pipeline
import numpy as np

EMBED_MODEL = SentenceTransformer("all-mpnet-base-v2")
DEVICE_ID = -1 if not hasattr(EMBED_MODEL, "device") else 0
SUMMARIZER = pipeline(
    "text2text-generation",
    model = "Vamsi/T5_Paraphrase_Paws",
    device=DEVICE_ID
)

#outputs 768 dimensions.
def embed_string(text: str) -> np.ndarray:
    vec = EMBED_MODEL.encode(text, normalize_embeddings=True)
    return np.asarray(vec, dtype=np.float32)

def cosine_sim(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b))

def summarize_text(text: str, max_new_tokens: int = 80, temperature: float = 0.7) -> str:
    prompt = f"paraphrase: {text}"
    summary = SUMMARIZER(
        prompt,
        max_new_tokens = max_new_tokens,
        temperature = temperature,
        early_stopping = False,
        do_sample = True
    )
    return summary[0]["generated_text"]

def translate_text(text: str, source: str, destination: str = "en") -> str:
    return GoogleTranslator(source=source, target=destination).translate(text)

class AIService(IAIService):
    def __init__(self):
        self.db_service = DBService()

    def generateNewsDependencies(self, news: List[str]):
        #category -> set category ID

        result: List[News] = []

        for x in news:
            if x["category"] == "":
                categories = self.db_service.get_all_categories()
                news_text = x["title"] + " " + x["description"]
                news_emb = embed_string(news_text)
                best_score = -float("inf") 
                best_id: Optional[int] = None

                for category in categories:
                    category_vec = np.asarray(category.categoryEmbedding, dtype=np.float32)
                    score = cosine_sim(category_vec, news_emb)
                    if score > best_score:
                        best_score = score
                        best_id = category.id
                if best_id is None:
                    news.remove(x)
                    continue
                x["categoryId"] = best_id
                            
            else:
                categoryId = self.db_service.get_category_id(x["category"])
                if categoryId is None:
                    # Create category embedding
                    category_emb = embed_string(x["category"])
                    new_category = Category(category = x["category"], categoryEmbedding = category_emb.tolist())
                    categoryId = self.db_service.create_category(new_category)
                
                x["categoryId"] = categoryId
                    
            
            # Create AI Generated Text
            if x["description"] == None or x["description"].strip() == "" or x["description"].strip().endswith("..."):
                summary = summarize_text(x["title"])
            else:
                summary = summarize_text(x["description"])

            x["aiGeneratedText"] = summary

            # Create news embeddings -> translate to en
            if "en" not in x["language"]:
                title_en = translate_text(x["title"], x["language"])
                desc_en = translate_text(x["description"], x["language"])
                
                news_vec = embed_string(title_en + " " + desc_en)

            else:
                news_vec = embed_string(x["title"] + " " + x["description"])
            
            x["embedding"] = news_vec


            # Save news to DB
            item = News(
                title = x["title"],
                description = x["description"],
                link = x["link"],
                publicationDate = x["publicationDate"],
                aiGeneratedText = x["aiGeneratedText"],
                Embedding = x["embedding"],
                categoryId = x["categoryId"],
                validationText = None,
                author = x["author"],
                language = x["language"]

            )
            result.append(item)


        self.db_service.save_news(result)


        