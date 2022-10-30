# Python: Suffix-stripping Stemmer

# Stemming is the process of extracting the base word from a word.
# For instance, the base for "worked" is "work".

# Use the the following algorithm to stem a word:
# 1) if the word ends in 'ed', 'ly', or 'ing' --> remove the suffix;
# 2) if the resulting word is no longer than 8 letters, keep the first 8 letters

# Implement a function that takes a string of space-separated words and returns its stemmed sounterpart.
# Example text = 'an extremely dangerous dog is barking'

def stemmer(text):
    # splitting one given string into several strings
    # text_list = []
    text_list:list[str] = text.split(' ')
    # creating a list for collecting new words without suffixes
    result_text = ''
    for value in text_list:
        if value.endswith('ly'):
            res = value.removesuffix('ly')
            if len(res) > 8:
                res = res[0:8]
                result_text += res + ' '
            else:
                result_text += res + ' '
        elif value.endswith('ed'):
            res = value.removesuffix('ed')
            if len(res) > 8:
                res = res[0:8]
                result_text += res + ' '
            else:
                result_text += res + ' '
        elif value.endswith('ing'):
            res = value.removesuffix('ing')
            if len(res) > 8:
                res = res[0:8]
                result_text += res + ' '
            else:
                result_text += res + ' '
        else:
            if len(value) > 8:
                res = value[0:8]
                result_text += res + ' '
            else:
                result_text += value + ' '
    # strip - a function, which deletes spaces at the beginning and the end of the sentence
    return result_text.strip()

print(stemmer('an extremely dangerous dog is barking'))