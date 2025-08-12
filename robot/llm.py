from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import SQLChatMessageHistory
from langchain_deepseek import ChatDeepSeek

from utils.get_api_key import get_deepseek_api_key
from robot.prompt import extract_prompt


def init_llm() -> ChatDeepSeek:
    deepseek_api_key = get_deepseek_api_key()
    if not deepseek_api_key:
        raise ValueError("DEEPSEEK_API_KEY not found in environment variables")
    llm = ChatDeepSeek(
        model="deepseek-reasoner",
        temperature=0,
        max_tokens=2048,
        timeout=None,
        max_retries=2,
        api_key=deepseek_api_key
    )
    return llm


def init_prompt(use_history: bool = False) -> ChatPromptTemplate:
    if use_history:
        prompt = ChatPromptTemplate.from_messages([
            ("system", extract_prompt),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{user_input}")
        ])
    else:
        prompt = ChatPromptTemplate.from_messages([
            ("system", extract_prompt),
            ("human", "{user_input}")
        ])
    return prompt


def init_chain():
    llm = init_llm()
    prompt = init_prompt()
    chain = prompt | llm | StrOutputParser()
    return chain


def init_chain_with_history(session_id: str):
    llm = init_llm()
    prompt = init_prompt()
    chain = prompt | llm | StrOutputParser()
    chain_with_history = RunnableWithMessageHistory(
        runnable=chain,
        message_history=SQLChatMessageHistory(
            session_id=session_id,
            connection_string="sqlite:///chat_history.db"
        ),
        input_key="user_input",
        history_key="history"
    )
    return chain_with_history
