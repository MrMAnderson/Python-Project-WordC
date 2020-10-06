# For the purpose of record here is the word list code I made so I could complete my project

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    
    # The words shall be split and formed into a list called werds (The name is weird so I can make I don't get mixed up)
    werds = file_contents.split(" ")
    
    werds_list = []
    
    # New list will be formed because we don't need the uninteresting words
    for werd in werds:
        for uninteresting_word in uninteresting_words:
            if werd is not uninteresting_word:
                werds_list.append(werd)
                
    # Any and all punctuation removed
    for werd in werds_list:
        if not werd.isalpha():
            werd = ''.join([letter for letter in werd if werd.isalpha()])
            
    werds_dict = {}
    
    # Word frequency becomes the values of keys in the dictionary called "werds_dict"
    for werd in werds_list:
        if werd not in werds_dict.keys():
            werds_dict[werd] = werds_list.count(werd)
                            
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(werds_dict)
    return cloud.to_array()
