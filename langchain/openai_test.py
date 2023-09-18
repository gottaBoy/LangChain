import os
from langchain.llms import OpenAI

os.environ["OPENAI_API_KEY"] = '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'

llm = OpenAI(model_name="text-davinci-003",max_tokens=1024)
llm("怎么评价人工智能")