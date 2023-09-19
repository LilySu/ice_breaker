from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List


class PersonIntel(BaseModel):  # represents answers we get from AI application.
    # will have summary, facts and list of ice breakers
    summary: str = Field(description="Summary of the person")
    facts: List[str] = Field(description="Interesting facts about the person")
    topics_of_interest: List[str] = Field(
        description="Topics that may interest the person"
    )
    ice_breakers: List[str] = Field(
        description="Create ice breakers to open a conversation with the person"
    )

    # receives object and returns dictionary representing object.
    # for serializing code
    # server answers with a response, taking the result into a dictionary serialized to a json object so that the server can respond.
    # schema describes the output we want
    def to_dict(self):
        return {
            "summary": self.summary,
            "facts": self.facts,
            "topics_of_interest": self.topics_of_interest,
            "ice_breakers": self.ice_breakers,
        }


# output parser object is used for prompt template, telling LLM format of how we want our answer to be returned. json, xml, parquet

person_intel_parser: PydanticOutputParser = PydanticOutputParser(
    pydantic_object=PersonIntel
)  # object of class PydandicOutputParser, requires key in the format of a Pydantic object
