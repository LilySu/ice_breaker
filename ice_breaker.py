from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from agents.twitter_lookup_agent import lookup as twitter_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile

from third_parties.twitter import scrape_user_tweets
import os

name = "elon musk"

if __name__ == "__main__":
    print("hello world")

    linkedin_profile_url = linkedin_lookup_agent(name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_profile_url)
    #
    # twitter_username = twitter_lookup_agent(name=name)
    # tweets = scrape_user_tweets(username=name, num_tweets=1) # normally twitter_username if twitter api were working

    summary_template = """
         given the information {linkedin_information} about a person from linkedin.  I want you to create the following.
         If a linkedin profile can't be found, find anyone with a similar name:
         1. a short summary
         2. two interesting facts about them
         3. A topic that may interest them
         4. 2 creative ice breakers to open a conversation with them.
     """

    summary_prompt_template = PromptTemplate(
        input_variables=["linkedin_information"], template=summary_template
    )

    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
        openai_api_key=os.environ.get("OPENAI_API_KEY"),
    )

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(linkedin_information=linkedin_data)) #, twitter_information=tweets

    # scrape_user_tweets(username="@elonmusk")
