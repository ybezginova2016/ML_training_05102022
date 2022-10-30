# Python: Suffix-stripping Stemmer

# Stemming is the process of extracting the base word from a word.
# For instance, the base for "worked" is "work".

# Use the the following algorithm to stem a word:
# 1) if the word ends in 'ed', 'ly', or 'ing' --> remove the suffix;
# 2) if the resulting word is no longer than 8 letters, keep the first 8 letters

# Implement a function that takes a string of space-separated words and returns its stemmed sounterpart.
# Example text = 'an extremely dangerous dog is barking'

def stemmer(text):
    text_list:list[str] = text.split(' ')
    result_text = ''
    for value in text_list:
        if 'ly' in value:
            res = value.removesuffix('ly')
            if len(res) <= 8:
                result_text += res + ' '
        elif 'ed' in value:
            res = value.removesuffix('ed')
            if len(res) <= 8:
                result_text += res + ' '
        elif 'ing' in value:
            res = value.removesuffix('ing')
            if len(res) <= 8:
                result_text += res + ' '
        else:
            if len(value) > 8:
                diff= len(value) - 8
                res = value[0:8]
                result_text+= res + ' '
            else:
                result_text += value + ' '

    return result_text.strip()

print(stemmer('an extremely dangerous dog is barking'))