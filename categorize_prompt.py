import replicate
import os

os.environ['REPLICATE_API_TOKEN'] = 'r8_8ROwjFvSoWEMovMBXyyTy1c2HYvYGLM0OxHsO'

output = replicate.run(
    # "replicate/flan-t5-xl:7a216605843d87f5426a10d2cc6940485a232336ed04d655ef86b91e020e9210",
    "mistralai/mixtral-8x7b-instruct-v0.1",
    input={
        "debug": False,
        # "top_p": 0.95,
        "prompt": "Boeing improved technical infrastucture by involving internet in a.\nWhich of the following classes does the above statement fall into : \n          1. Technology\n          2. Sports\n          3. Science\n          4. Health\n``` Your response should strictly be only one word from above 4 class",
        "max_length": 50,
        "temperature": 0.7,
        "repetition_penalty": 1
    }
)
for text in output:
    print(text)