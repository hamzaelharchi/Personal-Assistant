#views
import re

from .models import Task, Chat
from .serializer import  TaskSerializer, ChatSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
import speech_recognition as sr


'''
@api_view(['GET', 'POST'])
def user_list_api(request):
    all_users= User.objects.all()
    data=UserSerializer(all_users, many=True).data
    return Response({'data':data})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_detail_api(request, id):
    user_detail=User.objects.get(id=id)
    data=UserSerializer(user_detail).data
    return Response({'data':data})

'''
'''
class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
'''


@api_view(['GET'])
def taskList(request):
	tasks = Task.objects.all().order_by('-id')
	serializer = TaskSerializer(tasks, many=True)
	print(serializer.data)
	return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		print(serializer.data)

	return Response('hi hi hi')

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')






@api_view(['GET'])
def chatList(request):
	chat = Chat.objects.all().order_by('-id')
	serializer = ChatSerializer(chat, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def chatDetail(request, pk):
	chat = Chat.objects.get(id=pk)
	serializer = ChatSerializer(chat, many=False)
	return Response(serializer.data)


import base64

import speech_recognition as sr

@api_view(['POST', 'GET'])
def chatCreate(request):
	r=request.data[22:]
	r=bytes(r, 'utf-8')
	wav_file = open("record.wav", "wb")
	decode_string = base64.b64decode(r)
	wav_file.write(decode_string)
	
	# Initialize recognizer class (for recognizing the speech)
	r = sr.Recognizer()

	# Reading Audio file as source

	with sr.AudioFile('record.wav') as source:
		audio_text = r.listen(source)
		
		try:			
			text = r.recognize_google(audio_text)
			print('Converting audio transcripts into text ...')
			print(text)
		except:
			print('Sorry.. run again...')
		
		print(text)
		res=chat(text)
		print(res)

		return Response(res)	


#######################################################################################

import os
import re

import numpy as np
import yaml
from tensorflow.keras import Input, Model
from tensorflow.keras.activations import softmax
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.text import Tokenizer
#os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

########################################################################################################################
########################################### DATA PREPARATION ###########################################################
########################################################################################################################


dir_path = 'Home/archive/'
#files_list = os.listdir(dir_path + os.sep)
files_list=['health.yml', 'greetings.yml', 'science.yml', 'humor.yml', 'ai.yml', 'food.yml', 'botprofile.yml', 'psychology.yml', 'emotion.yml', 'computers.yml', 'sports.yml']

def clean_text(text_to_clean):
    res = text_to_clean.lower()
    res = re.sub(r"i'm", "i am", res)
    res = re.sub(r"he's", "he is", res)
    res = re.sub(r"she's", "she is", res)
    res = re.sub(r"it's", "it is", res)
    res = re.sub(r"that's", "that is", res)
    res = re.sub(r"what's", "what is", res)
    res = re.sub(r"where's", "where is", res)
    res = re.sub(r"how's", "how is", res)
    res = re.sub(r"\'ll", " will", res)
    res = re.sub(r"\'ve", " have", res)
    res = re.sub(r"\'re", " are", res)
    res = re.sub(r"\'d", " would", res)
    res = re.sub(r"\'re", " are", res)
    res = re.sub(r"won't", "will not", res)
    res = re.sub(r"can't", "cannot", res)
    res = re.sub(r"n't", " not", res)
    res = re.sub(r"n'", "ng", res)
    res = re.sub(r"'bout", "about", res)
    res = re.sub(r"'til", "until", res)
    res = re.sub(r"[-()\"#/@;:<>{}`+=~|.!?,]", "", res)
    return res


questions = list()
answers = list()
for filepath in files_list:
    stream = open(dir_path + os.sep + filepath, 'rb')
    docs = yaml.safe_load(stream)
    conversations = docs['conversations']
    #print(stream)

    for con in conversations:
        if len(con) > 2:
            questions.append(con[0])
            ans = ''
            for rep in con[1:]:
                ans += ' ' + rep
            answers.append(ans)
        elif len(con) > 1:
            questions.append(con[0])
            answers.append(con[1])
answers_with_tags = list()
for i in range(len(answers)):
    if type(answers[i]) == str:
        answers_with_tags.append(answers[i])
    else:
        questions.pop(i)
answers = list()
for i in range(len(answers_with_tags)):
    answers.append('<START> ' + answers_with_tags[i] + ' <END>')
#print(len(questions))
#print(len(answers))


########################################################################################################################
############################################# MODEL TRAINING ###########################################################
########################################################################################################################

target_regex = '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~\t\n\'0123456789'
tokenizer = Tokenizer(filters=target_regex)
tokenizer.fit_on_texts(questions + answers)
VOCAB_SIZE = len(tokenizer.word_index) + 1
#print('Vocabulary size : {}'.format(VOCAB_SIZE))

tokenized_questions = tokenizer.texts_to_sequences(questions)
maxlen_questions = max([len(x) for x in tokenized_questions])
encoder_input_data = pad_sequences(tokenized_questions,
                                   maxlen=maxlen_questions,
                                   padding='post')

#print(encoder_input_data.shape)

tokenized_answers = tokenizer.texts_to_sequences(answers)
maxlen_answers = max([len(x) for x in tokenized_answers])
decoder_input_data = pad_sequences(tokenized_answers,
                                   maxlen=maxlen_answers,
                                   padding='post')
#print(decoder_input_data.shape)

for i in range(len(tokenized_answers)):
    tokenized_answers[i] = tokenized_answers[i][1:]
padded_answers = pad_sequences(tokenized_answers, maxlen=maxlen_answers, padding='post')
decoder_output_data = to_categorical(padded_answers, VOCAB_SIZE)

#print(decoder_output_data.shape)

enc_inputs = Input(shape=(None,))
enc_embedding = Embedding(VOCAB_SIZE, 200, mask_zero=True)(enc_inputs)
_, state_h, state_c = LSTM(200, return_state=True)(enc_embedding)
enc_states = [state_h, state_c]

dec_inputs = Input(shape=(None,))
dec_embedding = Embedding(VOCAB_SIZE, 200, mask_zero=True)(dec_inputs)
dec_lstm = LSTM(200, return_state=True, return_sequences=True)
dec_outputs, _, _ = dec_lstm(dec_embedding, initial_state=enc_states)
dec_dense = Dense(VOCAB_SIZE, activation=softmax)
output = dec_dense(dec_outputs)

#model = Model([enc_inputs, dec_inputs], output)
#model.compile(optimizer=RMSprop(), loss='categorical_crossentropy')

#model.summary()




# model.load_weights('model_small.h5')
from tensorflow.keras.models import load_model

model=load_model('Home\model_small.h5')



def str_to_tokens(sentence: str):
    words = sentence.lower().split()
    tokens_list = list()
    for current_word in words:
        result = tokenizer.word_index.get(current_word, '')
        if result != '':
            tokens_list.append(result)
    return pad_sequences([tokens_list],
                         maxlen=maxlen_questions,
                         padding='post')


enc_model=load_model('Home\enc_model')
dec_model=load_model('Home\dec_model')

def chat(message):
    states_values = enc_model.predict(
        str_to_tokens(message))
    empty_target_seq = np.zeros((1, 1))
    empty_target_seq[0, 0] = tokenizer.word_index['start']
    stop_condition = False
    decoded_translation = ''
    while not stop_condition:
        dec_outputs, h, c = dec_model.predict([empty_target_seq]
                                            + states_values)
        sampled_word_index = np.argmax(dec_outputs[0, -1, :])
        sampled_word = None
        for word, index in tokenizer.word_index.items():
            if sampled_word_index == index:
                if word != 'end':
                    decoded_translation += ' {}'.format(word)
                sampled_word = word

        if sampled_word == 'end' \
                or len(decoded_translation.split()) \
                > maxlen_answers:
            stop_condition = True

        empty_target_seq = np.zeros((1, 1))
        empty_target_seq[0, 0] = sampled_word_index
        states_values = [h, c]

    return decoded_translation
print('++++++++++++++++++++++++++++++++++++++++++++++++')
print('++++++++++++++++++++++++++++++++++++++++++++++++')
