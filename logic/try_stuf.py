with open("engish_teaching_app/filies/song_words",'r') as song_file:
    song_words=song_file.read()
    
with open('engish_teaching_app/filies/words to know','r') as word_file:
    word_to_study=word_file.read()    
list_word_to_study=word_to_study.strip(')').strip('(').lower().split('\n')
    
        
song_words_list=song_words.lower().replace('\n',' ').split(' ')
print(song_words_list.index('code_flag'))
song_name_dict={}
a=0
for i in song_words_list:
    a=a+1
    if i =='code_flag':
        song_name_index=song_words_list.index(i)+a
        song_name=song_words_list[song_name_index]
        song_name_dict[song_name]=song_name_index
print(song_name_dict)