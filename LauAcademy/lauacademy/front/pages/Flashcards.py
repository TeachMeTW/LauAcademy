import streamlit as st
from PIL import Image

from lauacademy.front.pages.data_class.SharedData import SharedData
shared_data = SharedData()

test_questions = {
  "test": [
    {
      "questions": "What is a GenServer in Elixir?",
      "answer": "A GenServer in Elixir is short for 'generic server'. It is an OTP Behaviour that allows creating separate Elixir processes to act as servers, which can manage state and take actions in the system. GenServers provide many benefits of independent services without the usual headaches, and they can be customized to fit specific needs."
    },
    {
      "questions": "What are Agents in Elixir?",
      "answer": "Agents in Elixir are an abstraction that simplifies the management of state with Elixir processes. They are designed to hold state and allow querying and manipulation of that state. Agents are the simplest way to use OTP (Open Telecom Platform) in Elixir, providing an easy-to-use abstraction for spawning processes and handling state."
    },
    {
      "questions": "What is OTP in Elixir?",
      "answer": "OTP stands for Open Telecom Platform, an Erlang super-library and design pattern combination that makes Elixir and Erlang's incredible concurrency, fault tolerance, and distribution possible. Elixir abstracts away most of the OTP patterns, but under the hood, OTP is present, providing the powerful features Elixir is known for."
    },
    {
      "questions": "What are the benefits of using GenServer in Elixir?",
      "answer": "GenServer processes in Elixir provide isolation and encapsulation, allowing applications to be broken down into smaller, focused pieces. They can be spawned as separate processes to address scaling needs, and they can be easily integrated with the rest of the application. GenServers also offer easier configuration, testing, and deployment, and can be supervised for fault tolerance."
    },
    {
      "questions": "What is the main difference between Elixir and most popular Object Oriented languages in terms of state and behavior?",
      "answer": "In Elixir, state and behavior are kept separate. Processes may hold data structures as state, but they never mix state and behavior together. Functions don't automatically have access to state, requiring it to be passed in or fetched by the function. This is a key difference between Elixir and most popular Object Oriented languages, where state and behavior are often combined."
    }
  ]
}