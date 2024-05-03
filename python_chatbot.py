import re


def message_probablity(user_msg,recon_words,single_responses = False, required_words=[]):
    message_certainity=0
    has_required_words= True
    
    for word in user_msg:
        if word in recon_words:
            message_certainity+=1
            
    percentage= float(message_certainity)/float(len(recon_words))
    
    for word in required_words:
        if word not in user_msg:
            has_required_words= False
            break
        
    if has_required_words or single_responses:
        return int(percentage*100)
    else:
        return 0
    
def check_all_messages(message):
    highest_prob_list={}
    
    def response(bot_response,list_of_words,single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response]=message_probablity(message,list_of_words,single_response)    
        
#response------------------

    response("hello!",["hey","hello",'hi'],single_response=True)
    response('I am doing fine!',['how','are','you','doing'],required_words='how')
    response('thank you',['good','love','amazing','you','are'],required_words=['you','are'])
    
    best_match=max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)
    
    return best_match
    
    

def get_response(user_input):
    split_message=re.split(r'\s+|[,./?;!-]\s*',user_input.lower())
    response=check_all_messages(split_message)


while True:
    print('Bot: ',get_response(input('You: ')))