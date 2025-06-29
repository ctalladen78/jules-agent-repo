
                                                                                                                     
 from fastapi import FastAPI                                                                                         
 from langchain.agents import load_tools                                                                             
 from langchain.agents import initialize_agent                                                                       
 from langchain.agents import AgentType                                                                              
 from langchain.llms import OpenAI                                                                                   
                                                                                                                     
 app = FastAPI()                                                                                                     
                                                                                                                     
 @app.get("/search")                                                                                                 
 async def search(query: str):                                                                                       
     llm = OpenAI(temperature=0)                                                                                     
     tools = load_tools(["serpapi"], llm=llm)                                                                        
     agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)                 
     response = agent.run(query)                                                                                     
     return {"result": response}      