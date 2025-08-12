from robot.llm import init_chain
# from robot.llm import init_chain_with_history


chain = init_chain()
# chain = init_chain_with_history(session_id="20250801")


def extract(user_input: str):
    result = chain.invoke({"user_input": user_input})
    return result


def extract_with_history(user_input: str, session_id: str):
    config = {"configurable": {"session_id": session_id}}
    result = chain.invoke({"user_input": user_input}, config=config)
    return result
