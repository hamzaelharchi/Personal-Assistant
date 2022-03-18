from django.shortcuts import render

def index(request):
    return render(request, 'Home/index.html')




def recordings(request):
    if request.method == 'POST':
        data = request.get_json()
        print(f">>>>>>>>>>>>>>>{data}")
        answer = 'assistant.bot(str(voice_clip))'
        print(f'answer: {answer}')
        return {"answer": answer}