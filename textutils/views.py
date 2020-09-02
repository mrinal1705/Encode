#i have created this file
import onetimepad
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def encryptMessage(input_message):
    # inbuilt function to encrypt a message
    x = onetimepad.encrypt(input_message, 'random')
    return x

def decryptMessage(input_encrypted_message):
    # inbuilt function to decrypt a message
    y = onetimepad.decrypt(input_encrypted_message, 'random')
    return y



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')
    encrypt = request.POST.get('encrypt', 'off')
    decrypt = request.POST.get('decrypt', 'off')

    #print(encrypt)
    #print(djtext)
    if encrypt == "on":
        output = encryptMessage(djtext)

        params = {'purpose': 'Encryption Done', 'analyzed_text': output}
        return render(request, 'analyze.html', params)


    elif decrypt == "on":
        output = decryptMessage(djtext)

        params = {'purpose': 'Decryption Done', 'analyzed_text': output}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("<h1>Error!</h1> <br><a href = '/'>back</a>")



#def removepunc(request):
    #return HttpResponse('''<h1> remove punc </h1> <a
    #href = "http://127.0.0.1:8000/ ">
    #Home</a>
    #<br> <h1> button2 </h1>''')









#def removepunc(request):
    #Get the text
    #djtext = request.GET.get('text', 'default')
    #print(djtext)
    #Analyze the text
    #return HttpResponse("remove punc")


#def removepunc(request):
    #return HttpResponse('''<h1> remove punc </h1> <a
    #href = "http://127.0.0.1:8000/ ">
    #Home</a>
    #<br> <h1> button2 </h1>''')

#def capfirst(request):
    #return HttpResponse("capitalize first")

#def newlineremove(request):
    #return HttpResponse("capitalize first")


#def spaceremove(request):
    #return HttpResponse("space remover <a href = '/'>back</a>")

#def charcount(request):
    #return HttpResponse("charcount ")

