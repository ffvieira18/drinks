from django.shortcuts import render
from rest_framework.views import APIView
from .models import ReceiverModel
from .forms import ReceiveForm
import sys
import subprocess
from subprocess import PIPE, Popen



import os
import shutil
import re
# Create your views here.


class ReceiverProt(APIView):
    def post(self, request):
        print (request.POST['folder'], request.POST['amino'])
        

class ReceiverInterfaceView(APIView):
    def get(self, request, format=None):
        return render(request, 'ok.html')
    def post(self, request, format=None):
        print(request.POST)
        nome_da_pasta = request.POST['folder_name']
        print(request.FILES)
        
        folder_path = "c:/Users/ffvie/DjangoProjects/rins_comp/Ring_Files/" + nome_da_pasta
        path = os.makedirs(folder_path)
        nodes_path = folder_path + "/nodes"
        path_nodes = os.makedirs(nodes_path)
        edges_path = folder_path + "/edges"
        path_edges = os.makedirs(edges_path)
        
        
        nome_dos_arquivos = []
        if request.method == "POST":
            form = ReceiveForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            #modelo = ReceiveForm(nome_da_pasta)
            
            for f in request.FILES.getlist('file_received'):
                #modelo = ReceiverModel(nome_da_pasta)
                #modelo.save()
                nome_dos_arquivos.append(f.name)
                ReceiverModel.objects.create(file_received=f)
                #modelo.save()                

            
            edges = 'edges/'
            nodes = 'nodes/'
            
            for arq in nome_dos_arquivos:
                folder_path = "c:/Users/ffvie/DjangoProjects/rins_comp/Ring_Files/"
                
                if re.search(r'_edges', arq):
                    shutil.move(folder_path+arq, folder_path+nome_da_pasta+'/'+edges+arq)            
                else:
                    shutil.move(folder_path+arq, folder_path+nome_da_pasta+'/'+nodes+arq)            

            folder_path = folder_path + nome_da_pasta + '/'
            #print(folder_path)
            pipe = subprocess.Popen(["python", "c:/Users/ffvie/DjangoProjects/rins_comp/Felipe.py", folder_path], stdout = subprocess.PIPE)
            pipe.wait()
            #subprocess.call ("Rscript --vanilla ./Felipe.py", folder_path, shell=True)
            #exec(open('./rins_comp/Felipe.py', folder_path).read())
            files_received = pipe.communicate()[0].decode('utf-8').split('\r\n')
            
            

            print(files_received)
            
            print("terminou")
        return render(request, 'result.html',{'files': files_received[:-1], 'folder' : nome_da_pasta})
        
