import httplib2 # install python module - pip install httplib2
import json

def dog_breed_predictor():
	#Neuronal Network
	##Substitute dogRase with the Nueronal Network output
	dogRase = "golden_retriever"

	#Wikipedia 
	wikiApi = 'https://en.wikipedia.org/w/api.php?action=opensearch&format=json&search=' + dogRase
	h = httplib2.Http()
	response, content = h.request(wikiApi, 'GET')
	result = json.loads(content)
	DogRasedescribe = result[2][0]

	result = "Hi, that is a beatiful " + dogRase + "! " + DogRasedescribe

	return result
