from langchain.tools import BaseTool                                                                                                              
 from langchain.utilities import GoogleSearchAPIWrapper  # Or other APIs/utilities                                                                 
                                                                                                                                                   
 # Example custom tools                                                                                                                            
 def get_current_weather(query: str) -> str:                                                                                                       
     """Gets the current weather for a given location."""                                                                                          
     search = GoogleSearchAPIWrapper()  # Replace with your actual weather API call                                                                
     weather = search.results(f"current weather in {query}")                                                                                       
     return weather[0]  # Or process the results as needed                                                                                         
                                                                                                                                                   
 def get_stock_price(ticker: str) -> str:                                                                                                          
     """Gets the current stock price for a given ticker symbol."""                                                                                 
     # Replace with your actual stock API call                                                                                                     
     # ... (Your code to fetch stock price) ...                                                                                                    
     return f"The current price of {ticker} is $XX.XX"                                                                                             
                                                                                                                                                   
 # Wrap tools as LangChain tools (optional but recommended)                                                                                        
 class GetCurrentWeatherTool(BaseTool):                                                                                                            
     name = "get_current_weather"                                                                                                                  
     description = "useful for when you need to find out the current weather in a given location."                                                 
                                                                                                                                                   
     def _run(self, location: str) -> str:                                                                                                         
         return get_current_weather(location)                                                                                                      
                                                                                                                                                   
     async def _arun(self, location: str) -> str:                                                                                                  
         raise NotImplementedError("This tool does not support async")                                                                             
                                                                                                                                                   
 class GetStockPriceTool(BaseTool):                                                                                                                
     name = "get_stock_price"                                                                                                                      
     description = "useful for when you need to find out the current stock price for a given ticker symbol."                                       
                                                                                                                                                   
     def _run(self, ticker: str) -> str:                                                                                                           
         return get_stock_price(ticker)                                                                                                            
                                                                                                                                                   
     async def _arun(self, ticker: str) -> str:                                                                                                    
         raise NotImplementedError("This tool does not support async")   