#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 16:10:05 2025

@author: pa_bisgambiglia
"""

import pyagrum as gum
import numpy as np
import re

class reseauBayesien():
    def __init__(self, file_name):
        self._file_name = file_name
        self._nom=""
        self._noeuds=[]
        self._parents=[]
        self._probabilites=[]
        
    def lire_reseau(self):
        with open(self._file_name,'r') as file :
            #Lecture du nom du réseau
            self._nom = file.readline().split()[-1]
            #Lecture différents noeuds
            line=file.readline().split()[3::2]
            self._noeuds=(line[::2],line[1::2])
            file.readline()
            #Indentification des liens er de probabilités
            for line in file :
                #Récupération des différents champs séparés par de |
                seq = line.split('|')
                noeud = seq[0].strip()
                parents = []
                if len(seq[1].strip().split())>0 :
                    #récupération des marents du noeud
                    parents = seq[1].strip().split()
                #Création de deux listes de types (noeud, parents) et (noeud, proabilités)
                self._parents.append((noeud, parents))
                self._probabilites.append((noeud,list(map(float, seq[2].strip().split()))))
    
    def creer_reseau(self):
        rb = gum.BayesNet(self._nom)
        #Création des noeuds
        for nom in self._noeuds[0]:
            rb.add(nom, 2)
        #Ajouter les arcs
        for noeud, parents in self._parents:
            for parent in parents:
                rb.addArc(rb.idFromName(parent), rb.idFromName(noeud))
        #Création des tables de probabilité
        for noeud, probabilites in self._probabilites:
            cpt=rb.cpt(rb.idFromName(noeud))
            cpt[:] = np.array(probabilites).reshape(cpt.shape)
        return rb

    def creer_requette(self, requette):
        #Suppresion des blancs et de P()
        requette = requette.strip()[2:-1].replace(" ", "")
        #Recherche du |
        conditionnel = '|' in requette
        noeuds=[]
        if conditionnel :
            effets, observations = requette.split('|')
            effets=re.split(r'[=,]', effets)
            pos_pipe=int(len(effets)/2)
            noeuds=[(effets[i], effets[i+1]) for i in range(0, len(effets), 2)]
            observations=re.split(r'[=,]', observations)
        else : 
            observations=re.split(r'[=,]', requette)
            pos_pipe=0
        tuples=[(observations[i], observations[i+1]) for i in range(0, len(observations), 2)]
        noeuds.extend(tuples)
        return { "noeuds" : noeuds,
                "conditionnel": conditionnel,
                "pos_pipe":pos_pipe}
        
def estimation(rb, requette):
    inference=gum.LazyPropagation(rb)
    if requette["conditionnel"]:
        debut=requette["pos_pipe"]
        observations={rb.idFromName(noeud): valeur for noeud, valeur in requette["noeuds"][debut:]}
        inference.setEvidence(observations)
        inference.makeInference()
        posteriors={rb.idFromName(noeud[0]) for noeud in requette["noeuds"][0:debut]}
        posterior=inference.jointPosterior(posteriors)
        valeurs=[int(noeud[1]) for noeud in requette["noeuds"][0:debut]]
        print(posterior[*valeurs])

def estimation_simple(rb, requette, nom):
    inference=gum.LazyPropagation(rb)
    observations={rb.idFromName(noeud): valeur for noeud, valeur in requette["noeuds"]}
    inference.setEvidence(observations)
    inference.makeInference()
    posterior=inference.posterior(rb.idFromName(nom))
    print(posterior)
    
nouveauRB=reseauBayesien("Reseau Bayesien.txt")
nouveauRB.lire_reseau()
rb=nouveauRB.creer_reseau()
requette=nouveauRB.creer_requette("P(C=0,A=1)")
estimation_simple(rb, requette, "F")
#estimation(rb, requette)


