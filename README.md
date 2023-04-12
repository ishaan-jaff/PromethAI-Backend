# Teenage-AGI-Chef

Teenage-AGI-Chef is a Python-based AGI (artificial general intelligence) project that recommends food choices based on a user's goals and preferences, and can modify its recommendations based on user feedback. The project is built on top of an existing AGI project that uses OpenAI and Pinecone to give memory to the AI agent, and allows it to "think" before making an action (outputting text).

In the modified version, which we can call "Teenage-AGI-Chef", the original project has been adapted to focus on food recommendations. The AI agent now has the ability to suggest meal options based on a user's specified goal, such as a fast meal, a tasty meal, or a healthy meal. It also has the ability to retrieve a list of restaurants from Google Maps and suggest matching food options based on the user's preferences.

Overall, Teenage-AGI-Chef is a practical application of AGI technology that has the potential to help users make informed food choices based on their goals and preferences.

Credits: 
Teenage AGI -> https://github.com/seanpixel/Teenage-AGI
Baby AGI -> https://github.com/yoheinakajima/babyagi


## Objective
Inspired by the several Auto-GPT related Projects (predominently BabyAGI) and the Paper ["Generative Agents: Interactive Simulacra of Human Behavior"](https://arxiv.org/abs/2304.03442), the original python project uses OpenAI and Pinecone to Give memory to an AI agent and also allows it to "think" before making an action (outputting text). Also, just by shutting down the AI, it doesn't forget its memories since it lives on Pinecone and its memory_counter saves the index that its on.

### Sections
- [How it Works](https://github.com/seanpixel/Teenage-AGI/blob/main/README.md#how-it-works)
- [How to Use](https://github.com/seanpixel/Teenage-AGI/blob/main/README.md#how-to-use)
- [Experiments](https://github.com/seanpixel/Teenage-AGI/blob/main/README.md#experiments)
- [More About Project & Me](https://github.com/seanpixel/Teenage-AGI/blob/main/README.md#how-to-use)
- [Credits](https://github.com/seanpixel/Teenage-AGI/blob/main/README.md#credits)

## How it Works
Here is what happens everytime the AI is queried by the user:
1. AI vectorizes the query and stores it in a Pinecone Vector Database
2. AI looks inside its memory and finds memories and past queries that are relevant to the current query
3. AI thinks about what action to take
4. AI stores the thought from Step 3
5. Based on the thought from Step 3 and relevant memories from Step 2, AI generates an output
6. AI stores the current query and its answer in its Pinecone vector database memory

## How to Use
1. Clone the repository via `git clone https://github.com/seanpixel/Teenage-AGI.git` and cd into the cloned repository.
2. Install required packages by doing: pip install -r requirements.txt
3. Set your OpenAI and Pinecone API info in the OPENAI_API_KEY, PINECONE_API_KEY, and PINECONE_API_ENV variables.
4. Run `python main.py` and talk to the AI in the terminal

## Experiments
Currently, using GPT-4, I found that it can remember its name and other characteristics. It also carries on the conversation quite well without a context window (although I might add it soon). I will update this section as I keep playing with it.

## More about the Project & Me
After reading the Simulcra paper, I made this project in my college dorm. I realized that most of the "language" that I generate are inside my head, so I thought maybe it would make sense if AGI does as well. I'm a founder currently runing a startup called [DSNR]([url](https://www.dsnr.ai/)) and also a first-year at USC. Contact me on [twitter](https://twitter.com/sean_pixel) about anything would love to chat.

## Credits
Thank you to [@yoheinakajima](https://twitter.com/yoheinakajima) and the team behind ["Generative Agents: Interactive Simulacra of Human Behavior"](https://arxiv.org/abs/2304.03442) for the idea!
