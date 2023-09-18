# LangChain

## 建立自己的ChatGPT
- [申请API_KEY](https://openai.com/blog/openai-api)
- [免费的](http://www.chatnext.top/)
- [免费的1](http://www.taodudu.cc/news/show-6118048.html?action=onClick)

```shell
www.chatnext.top
greengpt.app/chat

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
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
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
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
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
```

## LangChain介绍、安装和入门教程

- [LangChain](https://python.langchain.com/)

```
1、工具 (tools)：负责决定下一步要采取的步骤的类，由语言模型和提示提供支持。这个prompt可以包括代理的个性（有助于使其以某种方式做出反应）、代理的背景上下文（有助于为其提供有关要求它执行的任务类型的更多上下文）、提示策略以调用更好的推理。

2、代理 (agents)：介绍不同代理类型的概述。

3、工具包 (toolkits)：通代理可以访问的工具集比单个工具更重要。为此，LangChain提供了工具包的概念——实现特定目标所需的工具组。工具包中通常有大约 3-5 个工具 作者：西二旗马斯克LLM https://www.bilibili.com/read/cv25695459/ 出处：bilibili
```

### LangChain安装
```shell
pip install langchain

pip install openai
```

设置密钥
```python
import os
import openai os.environ["OPENAI_API_KEY"] = 'your_openai_key'
os.environ['OPENAI_API_BASE'] = ''
```

导入库
```python
from langchain.chat_models import ChatOpenAI
from langchain.agents import tool
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent
from langchain.agents import AgentExecutor
from langchain.prompts import MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
import os
```

### 模型
- [llama](https://github.com/ggerganov/llama.cpp/releases)
## 相关链接
- [LLama](https://www.zhihu.com/question/612806085/answer/3125008901)
- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [Langchain-Chatchat](https://github.com/gottaBoy/Langchain-Chatchat)
- [awesome-chatgpt-zh](https://github.com/yzfly/awesome-chatgpt-zh)
- [LangChain-Chinese-Getting-Started-Guide](https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide)
- [Chinese-LangChain](https://github.com/yanqiangmiffy/Chinese-LangChain)
- [LangChain-ChatGLM-Webui](https://github.com/thomas-yanxin/LangChain-ChatGLM-Webui)
- [LangChain-ChatGLM](https://datawhaler.feishu.cn/file/L3D0b6PUUoEnmux5aBUcU6HunHf)
- [gpt4all](https://github.com/nomic-ai/gpt4all)
- [gpt4all](https://gpt4all.io/index.html)
- [chatgpt_all](https://github.com/qq31682216/chatgpt_all)
- [使用Python在Windows上使用Llama + Vicuna进行本地GPT](https://zhuanlan.zhihu.com/p/621430028)
- [LangChain](https://www.utheme.cn/aigc/28721.html)
- [ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B)