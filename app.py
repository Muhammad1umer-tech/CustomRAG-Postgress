from helper import  run_query_pgvector_get_response
import chainlit as cl

def get_rag_response(user_input):
    return run_query_pgvector_get_response(user_input)


@cl.on_chat_start
async def on_chat_start():
    welcome_message = """
    **Welcome to Business Dev Custom RAG!** 🚀🤖
    Hi there! 👋 This RAG is designed to include comprehensive information about the projects we’ve worked on, along with detailed insights into our expertise. You can consult Business Dev Custom RAG to accurately address client queries.
    """    
    await cl.Message(content=welcome_message).send()
    
    
    
@cl.on_message
async def on_message(message: cl.Message):
    response = run_query_pgvector_get_response(message.content)
    await cl.Message(response).send()
    