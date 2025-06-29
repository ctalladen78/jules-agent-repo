# langchain tools, agents                                                                                                                         
 from langchain.agents import create_csv_agent                                                                                                     
 from langchain.llms import OpenAI                                                                                                                 
 import pandas as pd                                                                                                                               
                                                                                                                                                   
 class MainAgent:                                                                                                                                  
     def __init__(self, csv_url, openai_temperature=0, verbose=True):                                                                              
         """                                                                                                                                       
         Initializes the MainAgent with a CSV URL and optional parameters.                                                                         
                                                                                                                                                   
         Args:                                                                                                                                     
             csv_url (str): The URL of the CSV file.                                                                                               
             openai_temperature (float, optional): Temperature for OpenAI model. Defaults to 0.                                                    
             verbose (bool, optional): Verbose output for the agent. Defaults to True.                                                             
         """                                                                                                                                       
         self.csv_url = csv_url                                                                                                                    
         self.openai_temperature = openai_temperature                                                                                              
         self.verbose = verbose                                                                                                                    
         self.agent = None  # Initialize agent as None                                                                                             
                                                                                                                                                   
         self._load_data()                                                                                                                         
         self._create_agent()                                                                                                                      
                                                                                                                                                   
                                                                                                                                                   
  def _load_data(self):                                                                                                                         
         """Loads the CSV data and creates the CSV tool."""                                                                                        
         try:                                                                                                                                      
             self.df = pd.read_csv(self.csv_url)                                                                                                   
             self.csv_tool = create_csv_agent(OpenAI(temperature=self.openai_temperature), self.df, verbose=self.verbose)                          
         except Exception as e:                                                                                                                    
             raise RuntimeError(f"Error loading CSV: {e}")                                                                                    
                                                                                                                                                   
                                                                                                                                                   
    def _create_agent(self):                                                                                                                      
         """Creates the CSV agent with custom tools."""                                                                                            
         try:                                                                                                                                      
             tools = [                                                                                                                             
                 get_current_weather,  # Add your custom tool functions here                                                                       
                 get_stock_price,                                                                                                                  
             ]                                                                                                                                     
             tool_names = [tool.__name__ for tool in tools]                                                                                        
             self.agent = initialize_agent(                                                                                                        
                 tools + [self.csv_tool],  # Combine custom tools with the CSV tool                                                                
                 OpenAI(temperature=self.openai_temperature),                                                                                      
                 agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,                                                                                      
                 verbose=self.verbose                                                                                                              
             )                                                                                                                                     
         except Exception as e:                                                                                                                    
             raise RuntimeError(f"Error creating agent: {e}")                                                                                             
                                                                                                                                                   
     def run(self, query):                                                                                                                         
         """                                                                                                                                       
         Runs the agent with a given query.                                                                                                        
                                                                                                                                                   
         Args:                                                                                                                                     
             query (str): The query to run.                                                                                                        
                                                                                                                                                   
         Returns:                                                                                                                                  
             str: The agent's response.                                                                                                            
         """                                                                                                                                       
         if self.agent is None:                                                                                                                    
             raise RuntimeError("Agent not initialized. Please call _create_agent() first.")                                                       
         try:                                                                                                                                      
             response = self.agent.run(query)                                                                                                      
             return response                                                                                                                       
         except Exception as e:                                                                                                                    
             raise RuntimeError(f"Error running agent: {e}")                                                                                       
                                                                                                                                                   
                                                                                                                                                   
                                                                                                                                                   
 # Example usage (in a separate script or main block):                                                                                             
 if __name__ == "__main__":                                                                                                                        
     csv_url = "https://raw.githubusercontent.com/<username>/<repository>/<branch>/<path_to_csv_file>.csv"  # Replace with your actual URL         
                                                                                                                                                   
     try:                                                                                                                                          
         main_agent = MainAgent(csv_url)                                                                                                           
         response = main_agent.run("What is the average value of <column_name>?")  # Replace <column_name>                                         
         print(response)                                                                                                                           
                                                                                                                                                   
         response = main_agent.run("How many rows have a <column_name> greater than <value>?")  # Replace <column_name> and <value>                
         print(response)                                                                                                                           
                                                                                                                                                   
     except RuntimeError as e:                                                                                                                     
         print(f"Error: {e}")    