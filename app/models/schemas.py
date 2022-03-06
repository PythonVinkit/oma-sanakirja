from typing import List, Optional
from pydantic import BaseModel, EmailStr

class Language(BaseModel):
    id: int
    name: str

class User(BaseModel):

    id: int
    name: str
    email: EmailStr

class Word(BaseModel):

    id: int
    language: Language
    name: str
    kuva: Optional[bytes] = None
    aani: Optional[bytes] = None

class WordDictionary(BaseModel):

    id: int
    name: str
    original_language: Language
    super_user: Optional[User] = None
    users: List[User] = []

class TranslationMap(BaseModel):

    id: int
    language_to: Language
    word_from: Word
    word_to: Word
    word_dictionary: WordDictionary