from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

# Create app
app = FastAPI()

# Allow frontend to call backend (important for Flutter web/dev)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all origins (ok for dev)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample FAQ data
faq_data = {
    "fees": "The annual fees are ₹50,000 for UG courses.",
    "admission": "Admissions are open from June to August.",
    "hostel": "Yes, hostel facilities are available for both boys and girls.",
    "placement": "Our placement rate is 85% with top companies visiting campus.",
    "scholarship": "We offer merit-based scholarships up to 50% tuition fee.",
}

# Request body model
class UserMessage(BaseModel):
    message: str

# Health check
@app.get("/")
def health():
    return {"status": "ok", "message": "College FAQ Bot is running 🚀"}

# Chat endpoint
@app.post("/chat")
def chat(user_message: UserMessage):
    msg = user_message.message.lower()

    # Simple keyword matching
    for key, answer in faq_data.items():
        if key in msg:
            return {"response": answer}

    # Fallback
    return {"response": "Sorry, I don’t know the answer to that. Please contact the college office."}
