import replicate
import os

import replicate

class ReplicateAPI:
    def __init__(self, model_name, api_token = 'r8_8ROwjFvSoWEMovMBXyyTy1c2HYvYGLM0OxHsO'):
        os.environ['REPLICATE_API_TOKEN'] = api_token
        self.model_name = model_name
        self.input_params = {
            "debug": False,
            "top_p": 0.95,
            "prompt": "",
            "max_length": 30,
            "temperature": 0.8,
            "repetition_penalty": 1,
            "prompt_template": '''
                <s>[INST] {prompt}
                \nWhich of the following classes does the above statement fall into : 
                1. Technology\n 2. Sports\n 3. Science\n 4. Health\n
                ``` Your response should strictly be only one word from above 4 class
                [/INST] 
                '''
        }

    def run_model(self, prompt) -> list:
        self.input_params['prompt'] = prompt
        output = replicate.run(self.model_name, self.input_params)
        return output


if __name__ == '__main__':
    api = ReplicateAPI(model_name='mistralai/mixtral-8x7b-instruct-v0.1')
    output = api.run_model("India won the cricket match yesterday")
    print(output)
