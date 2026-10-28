import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')


données['ca'] = données['prix'] * données['qte']
#print(données.sum('ca'))
#6a
print("--- 6a ----")
#I
print("Moyenne ca par produit/ventes")
print(données.groupby('produit')[['ca', 'qte']].mean())
#II
print("Médiane par produit")
print(données.groupby('produit')[['ca', 'qte']].median())
#6b
print("--- 6b ----")
#I
print("Ecart-type ventes par produit")
print(données.groupby('produit')['qte'].std())
#II
print("Variance ventes par produit")
print(données.groupby('produit')['qte'].var())
#7
print("--- 7 ----")
lignes = données.to_dict('records')
#print(lignes)
produits = set(ligne['produit'] for ligne in lignes)
#print(produits)
totaux = []
for produit in produits:
    total = sum(ligne['qte'] for ligne in lignes if ligne['produit'] == produit)
    totaux.append((total, produit))

print("Produit le plus vendu :", max(totaux))
print("Produit le moins vendu :", min(totaux))

#8a
figure = px.pie(données, values='qte', names='produit', title='Ventes par produit')
figure.write_html('ventes-par-produit.html')
#8b
figure = px.pie(données, values='ca', names='produit', title='Ca par produit')
figure.write_html('ca-par-produit.html')

print("Code exécuté")
