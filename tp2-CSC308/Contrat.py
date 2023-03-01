from Client import Client
class Contrat:

    def __init__(self, numero, date, client:Client, montantContrat,interventions,nbIntervention):
        self._numero = numero,
        self._date = date,
        self._client = client,
        self._montantContrat = montantContrat
        self._interventions = interventions
        self._nbIntervention = nbIntervention

    def montant(self):
        return self._montantContrat

    def ecart(self):
        for intervention in self._interventions:
            sum(intervention.fraisMo)