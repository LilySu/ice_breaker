from third_parties.linkedin import xml_extract_arxiv

if __name__ == "__main__":
    print("hello world")

    # summary_template = """
    #      given the information {information} about a person from linkedin.  I want you to create:
    #      1. a short summary
    #      2. two interesting facts about them
    #  """

    # summary_prompt_template = PromptTemplate(
    #     input_variables=["information"], template=summary_template
    # )
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo", openai_api_key = os.environ.get('OPENAI_API_KEY'))

    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    # print(chain.run(information=["elon musk", "doja cat"]))

    linkedin_data = xml_extract_arxiv(
        linkedin_profile_url="https://www.linkedin.com/in/harrison-chase-961287118/"
    )
    # print(linkedin_data.json())
    print(linkedin_data.json())
