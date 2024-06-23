# Dataset Idea
The dataset aims to facilitate the comparative analysis of syntactic dependencies in Vladimir Nabokov's works written in Russian and English. The primary objective is to identify differences in syntactic structures and dependencies between the two languages, reflecting Nabokov's bilingualism and stylistic preferences. Each entry in the dataset represents a sentence from the text, along with its syntactic analysis. This includes information about the structure and grammatical relationships within each sentence.

# Structure of the Dataset
The dataset is divided into two subsets to enable a detailed and precise analysis:

- Lolita Subset:
  - This subset includes the original English text of "Lolita" by Vladimir Nabokov, followed by its translation into Russian by Nabokov.
  - Each entry contains the sentence in its respective language and the corresponding syntactic dependencies. 

- Laughter in the Dark Subset: 
  - This subset includes the text of "Laughter in the Dark," which was originally written in Russian and later translated into English by Nabokov.
  - Similar to the Lolita subset, each entry here includes the sentence in both languages and the syntactic dependencies.

# Data Types

| Column          | Data Type | Description                                                                                                                                      |
|-----------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Text_ID         | Integer   | A unique identifier for each text entry.                                                                                                         |
| Sentence_Number | Integer   | A unique identifier for each sentence.                                                                                                           |
| Language        | Character | Indicates the language of the sentence (e.g., "ru" or "en").                                                                                     |
| Sentence        | Character | The actual text of the sentence.                                                                                                                 |
| Tokens          | Character | Tokens (words or punctuation) in the sentence.                                                                                                   |
| Lemmas          | Character | Lemmas (base forms of words) corresponding to the tokens.                                                                                        |
| Dependencies    | Character | Syntactic dependencies for each token.                                                                                                           |
| Heads           | Character | A list of heads for each token, showing which word each token is dependent on. If the token is the root of the sentence, it is marked as 'ROOT'. |

