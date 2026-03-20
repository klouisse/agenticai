from typing_extensions import TypedDict,List
from langgraph.graph.message import add_messages
from typing import Annotated


#This statte class defines the structure of the state used in the graph.
#  It uses TypedDict to specify that the state should have a key called "messages" which is a list.
#  The Annotated type is used to associate the add_messages function with the messages key, 
# indicating that this function should be used to add messages to the state. 
# This allows for better type checking and code clarity when working with the state in the graph.

class State(TypedDict):
    """
    Represent the structure of the state used in graph
    """
    messages: Annotated[List,add_messages]