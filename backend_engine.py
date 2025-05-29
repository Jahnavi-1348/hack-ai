dsm_rules = {
    "PTSD": [
        "can't sleep", "nightmares", "flashbacks", "hypervigilance", "panic attacks",
        "startled easily", "on edge", "avoid reminders", "feeling detached", "always alert",
        "fear of being followed", "constantly scared", "trouble sleeping", "can't relax"
    ],
    
    "Depression": [
        "feel worthless", "no motivation", "lost interest", "nothing matters", "tired all the time",
        "hopeless", "can't get out of bed", "crying a lot", "sad all the time", "feeling numb",
        "everything feels pointless", "i feel empty", "i don't care anymore"
    ],
    
    "Anxiety": [
        "racing heart", "can't relax", "on edge", "feel shaky", "trouble breathing",
        "constant worry", "overthinking", "anticipatory dread", "muscle tension",
        "restlessness", "fear something bad will happen", "panic", "stressed out"
    ],
    
    "Dissociation": [
        "feel numb", "not really here", "out of body", "disconnected", "floating",
        "watching myself", "detached from reality", "derealization", "depersonalization",
        "lost time", "blackouts", "don't remember", "feel like a robot"
    ],
    
    "Coercive Control": [
        "tracks my phone", "monitors everything", "controls who I see", "won’t let me talk to friends",
        "controls my money", "isolates from family", "gaslighting", "threatens self-harm",
        "financial control", "emotional manipulation", "checks my messages", "uses our child to control me",
        "makes me feel crazy", "blames me for everything", "walk on eggshells"
    ],
    
    "Substance Use Risk": [
        "cravings", "need more to feel it", "withdrawal", "can't stop", "drink too much",
        "use to cope", "get high", "drugs every day", "blacked out", "wake and bake", "drink to sleep"
    ],
    
    "Trauma-related (complex)": [
        "emotional numbness", "can't trust anyone", "i blame myself", "keep reliving it",
        "afraid of intimacy", "can't connect with people", "feel permanently damaged",
        "reckless", "impulsive", "can’t concentrate", "trauma flashbacks", "disconnected from reality"
    ],
    
    "Personality Disorder Traits": [
        "suspicious of others", "i don’t need anyone", "feel nothing", "mood swings", "unusual beliefs",
        "paranoid", "cold toward people", "everyone’s out to get me", "i’m the only one who sees the truth"
    ],
    
    "Somatic Symptom": [
        "constant pain", "no one believes me", "doctor won’t help", "obsessed with symptoms",
        "think i’m dying", "everything hurts", "can’t work because of my body", "always sick", "dizzy all the time"
    ]
}
import spacy
from fuzzywuzzy import fuzz

# Load English NLP model once
nlp = spacy.load("en_core_web_sm")

def lemmatize_text(text):
    doc = nlp(text.lower())
    return " ".join([token.lemma_ for token in doc])

def extract_dsm_flags(text, symptom_dict, threshold=60):
    lemmatized_text = lemmatize_text(text)
    flags = {}

    for cluster, phrases in symptom_dict.items():
        matched = []
        for phrase in phrases:
            phrase_lem = lemmatize_text(phrase)
            score = fuzz.partial_ratio(phrase_lem, lemmatized_text)
            if score >= threshold:
                matched.append(phrase)
        if matched:
            flags[cluster] = {"count": len(matched), "matches": matched}

    return flags
