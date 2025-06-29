import requests                                                                                                     
                                                                                                                     
 import streamlit as st                                                                                              
 from langchain.agents import initialize_agent, Tool                                                                 
 from langchain.agents import AgentType                                                                              
 from langchain.llms import OpenAI                                                                                   
 from langchain.utilities import SerpAPIWrapper                                                                      
 import os                                                                                                           
 from reportlab.lib.pagesizes import letter                                                                          
 from reportlab.pdfgen import canvas                                                                                 
 from io import BytesIO  

from langchain_utils import main_agent
                                                                                                                     
st.title("LangChain Search Demo")                                                                                   
                                                                                                                     
# Initialize chat history                                                                                           
 if "messages" not in st.session_state:                                                                              
     st.session_state.messages = []                                                                                  
                                                                                                                     
 # Display chat messages from history                                                                                
 for message in st.session_state.messages:                                                                           
     with st.chat_message(message["role"]):                                                                          
         st.markdown(message["content"])                                                                             
                                                                                                                     
 # React to user input                                                                                               
 if prompt := st.chat_input("What is on your mind?"):                                                                
     # Add user message to chat history                                                                              
     st.session_state.messages.append({"role": "user", "content": prompt})                                           
     # Display user message in chat                                                                                  
     with st.chat_message("user"):                                                                                   
         st.markdown(prompt)                                                                                         
                                                                                                                     
     with st.chat_message("assistant"):                                                                              
         with st.spinner("Thinking..."):                                                                             
             response = agent.run(prompt)  # Assuming 'agent' is your LangChain agent                                
             st.markdown(response)                                                                                   
             # Add assistant message to chat history                                                                 
             st.session_state.messages.append({"role": "assistant", "content": response})  

# Download chat history as PDF                                                                                      
def create_pdf(messages):                                                                                           
    buffer = BytesIO()                                                                                              
    p = canvas.Canvas(buffer, pagesize=letter)                                                                      
    y = 750                                                                                                         
    for message in messages:                                                                                        
        p.drawString(100, y, f"{message['role'].capitalize()}: {message['content']}")                               
        y -= 20  # Adjust spacing as needed                                                                         
    p.save()                                                                                                        
    buffer.seek(0)                                                                                                  
    return buffer                                                                                                   

# download button                                                                                                            
if st.download_button("Download Chat History", data=create_pdf(st.session_state.messages),                          
file_name="chat_history.pdf", mime="application/pdf"):                                                              
    st.success("Chat history downloaded successfully!")    