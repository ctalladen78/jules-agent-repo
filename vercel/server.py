from fastapi import FastAPI                                                                                         
from langchain.agents import initialize_agent, Tool                                                                 
from langchain.agents import AgentType                                                                              
from langchain.llms import OpenAI                                                                                   
from langchain.utilities import SerpAPIWrapper                                                                      
import os                                                                                                           
                                                                                                                     
app = FastAPI()                                                                                                     
                                                                                                                     
 # Replace with your actual SerpAPI key                                                                              
serpapi_api_key = os.environ.get("SERPAPI_API_KEY") or "YOUR_SERPAPI_API_KEY"                                       
                                                                                                                     
search = SerpAPIWrapper(serpapi_api_key=serpapi_api_key)                                                            
llm = OpenAI(temperature=0)                                                                                         
                                                                                                                     
tools = [                                                                                                           
     Tool(                                                                                                           
         name="Search",                                                                                              
         func=search.run,                                                                                            
         description="useful for when you need to answer questions about current events. You should ask targeted questions",                                                                                                         
     )                                                                                                               
]                                                                                                                   
                                                                                                                     
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

                                                                                                                     
@app.get("/search")                                                                                                 
async def search_endpoint(query: str):                                                                              
    result = agent.run(query)                                                                                       
    return {"result": result} 