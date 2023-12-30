import autogen


config_list = [
    {
        'model': 'gp3-3.5-turbo-16k',
        'api_key': 'xxx',
        'base_url': "https://api.openai.azure.com" 

    }
]

#        'base_url': 'https://api-ds.ir-gateway-dev.abbvienet.com/'
llm_config = {
    "seed": 17, 
    "config_list" : config_list,
    "temperature": 0
}

assistant = autogen.AssistantAgent(
    name = 'new app assistant',
    llm_config=llm_config, 
    system_message = "assistant to create a new app"
)

user_proxy = autogen.UserProxyAgent(
    name = "user_proxy",
    human_input_mode = "TERMINATE",
    max_consecutive_auto_reply=10, 
    is_termination_msg = lambda x: x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config = {"work_dir": "web"},
    llm_config = llm_config,
    system_message = """"Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)

task = """
give me a summary of this article: https://www.business.hsbc.com/en-gb/campaigns/sustainability?cid=HBEU:PW:S4B:P1:CMB:L14:GO%20:XTR:14:XX:13:0723:716:S4B_S4B_Google_PPC_Phrase_Climate%20Change&gad_source=1&gclid=CjwKCAiAnL-sBhBnEiwAJRGign1fUeyfg4NzNJl3ERsVnq-vCeDty0VrVZdFcZx3q2v5BqSBlRp-RhoCgIEQAvD_BwE&gclsrc=aw.ds
"""

user_proxy.initiate_chat(
    assistant,
    message = task
)
