
from typing import Generator
from openai import OpenAI


class DeepSeekAI:
    def __init__(
            self, 
            api_key: str, 
            base_url: str = 'https://api.deepseek.com', 
        ):
        """
        DeepSeekAI
        api_key: str   密钥
        base_url: str   基础url
        """
        self.client = OpenAI(api_key=api_key, base_url=base_url)
        self.models = {
            "chat": "deepseek-chat",
            "reason":"deepseek-reasoner"
        }


    def chat(self, model: str, messages: list[dict]) -> Generator[str, None, None]:
        """
        models:  chat/reason  
        messages: {"role": "user", "content": "Python 写冒泡排序法"}
        """
        try:
            response = self.client.chat.completions.create(
                model=self.models[model],
                messages=messages,
                stream=True
            )
            return response
        except Exception as e:
            print(e)
            return False
        

if __name__ == '__main__':
    # client = DeepSeekAI(api_key="")
    # messages = [
    #     {"role": "system", "content": "你是一个高级资深开发工程师"},
    #     {"role": "user", "content": "冒泡排序的时间复杂度是多少"}
    # ]
    # content = client.chat("chat", messages)
    # print(content)
    # s = ""
    # for chunk in content:
    #     s = s + chunk.choices[0].delta.content

    # print(s)
    pass
