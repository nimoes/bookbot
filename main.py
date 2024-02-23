def main():
    file_path = "books/frankenstein.txt"
    content = read_book(file_path)
    #print(f'Book content: {content}\n')

    num_words = get_num_words(content)
    #print(f'Number of words in this book: {num_words}\n')

    list_of_words = content.split()
    count_per_letter = count_letters(list_of_words)
    #print(f'Frequency of each letter in this book is as follows: {count_per_letter}\n')

    report = generate_report(file_path, num_words, count_per_letter)
    print(report)



def read_book(book):
    with open(book) as f:
        return f.read()

def get_num_words(body):
    words = body.split()
    return len(words)
    
def count_letters(word_list) -> dict:
    letter_count = {}
    for word in word_list:
        for letter in word:
            if letter.lower() not in letter_count:
                letter_count[letter.lower()] = 1
            else:
                letter_count[letter.lower()] += 1
    
    return letter_count

def generate_report(book, word_count, data_dict) -> str:
    output = ""
    output += f'\n--- Begin report of {book} ---\n'
    output += f'{word_count} words found in the document\n\n'

    # creates a list of tuples, sort by x[1] or count in reverse
    sorted_data = sorted(data_dict.items(), key=lambda x:x[1], reverse=True)
   
    for k, v in sorted_data:
        output += f'The \'{k}\' character was found {v} times\n'

    output += '--- End report ---\n'
    return output

if __name__ == '__main__':
    main()