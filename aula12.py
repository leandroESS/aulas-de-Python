import requests
import aula10

def retorna_dados(cep):

 response = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
 print(response.status_code) #se der 200 é pq foi certo , se der 400 é errado (exemplo escrever jsonnn)
 print(response.text)
 print(type(response.text))
 print(response.json())
 print(type(response.json()))
 dados_cep = response.json()
 print(dados_cep['logradouro'])
 print(dados_cep['complemento'])
 return dados_cep

def retorna_dados_pokemon(pokemon):
    response =  requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format((pokemon)))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    retorna_dados('22041001')
    #dados_pokemon = retorna_dados_pokemon('pikachu')
    #print(dados_pokemon)
    #print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://www.last.fm/pt/user/Leandromyplay') #retorna o html do site
    print(response)