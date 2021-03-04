from django.shortcuts import render, redirect
import requests

# Create your views here.
from app.forms import DominioForm
from app.models import Dominio


def home(request):
    if request.method == 'POST':
        form = DominioForm(request.POST)
        if form.is_valid():
            dominio = form.save(commit=False)
            dominio.save()
            return redirect('verDominio')
    else:
        form = DominioForm
    return render(request, 'home.html', {'form': form})


def verDominio(request):
    dominio = Dominio.objects.all().order_by('-updated')

    # Passando parâmetros da regra de negócio
    tamanho_max = 26
    tamanho_min = 8
    endurance = "endurance"
    hostgator = "hostgator"
    loja = "loja"
    premium = "premium"

    # Verificando se o domínio é vazio
    # dominio = objeto salvo no model
    # dominio[0] = primeiro objeto salvo no model
    # dominio[0].dominio = domínio salvo pelo usuário do primeiro objeto do model
    if dominio[0].dominio != None:

        # Verificando se o domínio é maior que 26 e maior que 8, pois retiramos o https:// e, caso o dominio tenha
        # tamanho 8 ou menor, o mesmo ficará vazio
        if len(dominio[0].dominio) < tamanho_max and len(dominio[0].dominio) > tamanho_min:

            # Retirando o https:// do domínio
            dominio_sem_https = dominio[0].dominio[8:]

            # Consultando o domínio na API
            api = requests.get(f'https://registro.br/v2/ajax/avail/raw/{dominio_sem_https}').json()

            # Pegando o status do domínio
            status = api["status"]

            # Verificando se o domínio é válido
            if status == 2:
                available = True
                price = 26.99

                # Verificando se o domínio pertence à endurance ou hostgator
                if endurance in dominio[0].dominio or hostgator in dominio[0].dominio:

                    available = False
                    reason = "Registered trademark"

                    # Retorno o context para este caso
                    context = {
                        'dominio': dominio[0].dominio,
                        'available': available,
                        'price': price,
                        'reason': reason,
                    }
                    dominio.delete()
                    return render(request, 'verDominio.html', context)

                # Verificando se o domínio possui premium ou loja
                if loja in dominio[0].dominio or premium in dominio[0].dominio:
                    price = 99.90

                    # Retorno o context para este caso
                    context = {
                        'dominio': dominio[0].dominio,
                        'available': available,
                        'price': price,
                    }
                    dominio.delete()
                    return render(request, 'verDominio.html', context)

            # Caso o domínio seja inválido, de acordo com o status
            else:
                available = False
                reason = "Razão do domínio"

                # Retorno o context para este caso
                context = {
                    'dominio': dominio[0].dominio,
                    'available': available,
                    'reason': reason,
                }
                dominio.delete()
                return render(request, 'verDominio.html', context)

            # Retornando o context para qualquer domínio com status válido e que não entre nas condições acima
            context = {
                'dominio': dominio[0].dominio,
                'available': available,
                'price': price,
                }
            dominio.delete()
            return render(request, 'verDominio.html', context)
        mensagem = "Tamanho de domínio inválido. Por favor, tente outro domínio."
        context = {
            'mensagem': mensagem,
            'dominio': dominio[0].dominio
        }
        dominio.delete()
        return render(request, 'verDominio.html', context)
    dominio.delete()
    mensagem = "Este campo não pode ser vazio. Digite um domínio para visualizar."
    return render(request, 'verDominio.html', {'mensagem': mensagem})