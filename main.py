import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

load_dotenv()


def main():
    print("Hello from langchain-course!")
    print("Gemini API Key: " + os.getenv("GEMINI_API_KEY"))

    information = """
Iron Man is a 2008 American superhero film based on the Marvel Comics character of the same name. Produced by Marvel Studios and distributed by Paramount Pictures,[a] it is the first film in the Marvel Cinematic Universe (MCU). Directed by Jon Favreau from a screenplay by the writing teams of Mark Fergus and Hawk Ostby, and Art Marcum and Matt Holloway, the film stars Robert Downey Jr. as Tony Stark / Iron Man alongside Terrence Howard, Jeff Bridges, Gwyneth Paltrow, Leslie Bibb, and Shaun Toub. In the film, following his escape from captivity by a terrorist group, world-famous industrialist and master engineer Stark builds a mechanized suit of armor and becomes the superhero Iron Man.

A film featuring Iron Man was in development at Universal Pictures, 20th Century Fox, and New Line Cinema at various times since 1990 before Marvel Studios reacquired the rights in 2005. Marvel put the project in production as its first self-financed film, with Paramount Pictures distributing. Favreau signed on as director in April 2006 and faced opposition from Marvel when trying to cast Downey in the title role; the actor was signed in September. Filming took place from March to June 2007, primarily in California to differentiate the film from numerous other superhero stories that are set in New York City. During filming, the actors were free to create their own dialogue because pre-production was focused on the story and action. Rubber and metal versions of the armor, created by Stan Winston's company, were mixed with computer-generated imagery to create the title character.

Iron Man premiered in Sydney on April 14, 2008, and was released in the United States on May 2, as the first film in Phase One of the MCU. It grossed over $585 million, becoming the eighth-highest grossing film of 2008, and received praise from critics, especially for Downey's performance as well as Favreau's direction, the visual effects, action sequences, and writing. The American Film Institute selected it as one of the ten best films of 2008. It received two nominations at the 81st Academy Awards for Best Sound Editing and Best Visual Effects. In 2022, the Library of Congress selected the film for preservation in the United States National Film Registry for being "culturally, historically, or aesthetically significant". Two sequels have been released: Iron Man 2 (2010) and Iron Man 3 (2013).
    """

    general_prompt_template = """
    Given the information {information} about a movie, I want you to:
    1. create short summary of the movie
    2. make up a short funny mem about the movie
    """

    prompt_template = PromptTemplate(input_variables=["information"], template=general_prompt_template)

    llm = ChatGoogleGenerativeAI(temperature=0.7, model="gemini-2.5-flash", api_key=os.getenv("GEMINI_API_KEY"))

    chain = prompt_template | llm

    output = chain.invoke({"information": information})

    print(output.content)

if __name__ == "__main__":
    main()
