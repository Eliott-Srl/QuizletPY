import time
import os

def editQuestion(dictionnary):
    variant = 0

    listeQuestions = []

    print('{0} Annulation')

    for key in dictionnary:
        value = dictionnary[key]

        variant += 1

        listeQuestions.append(key)

        print('{', variant, '} ', key, ' : ', value, sep='') #On affiche le nom puis un : puis le numéro de téléphone
    
    time.sleep(1)

    print()

    try:
        suppTerm = int(input("Quelle qestion veut-tu modifier ? "))

    except ValueError:
        print("Donne un chiffre valide !")

        time.sleep(1)

        editQuestion(dictionnary)
        
    if suppTerm <= variant and suppTerm != 0:
        print("Question actuelle : {", key, ' : ', value,"}", sep = '')
        
        time.sleep(1)

        for key2 in dictionnary:
            while key2 == key:
                print("{", key2, "} deviens :", sep = '')

                saisie = input(">>> ")

                if saisie == 'exit':
                    print("Trés bien, annulation !")

                    time.sleep(1)

                    menu_GestionQuestion()

                if saisie == '':
                    pass

                else:
                    del dictionnary[key2] #On supprime le nom avec le numéro
                    dictionnary[saisie] = value #On ajoute le nouveau nom avec le numéro

                print("Trés bien")

                time.sleep(1)

                print()

                print("{",value,"} deviens :",sep='')

                saisie = input(">>> ")

                if saisie == 'exit':
                    print("Trés bien, annulation !")

                    time.sleep(1)

                    menu_GestionQuestion()

                if saisie == '':
                    pass

                else:
                    dictionnary[key2] = saisie

                print("Trés bien")

                with open('liste_questions.json', 'w') as file : #Ouverture/création (w) de annuaire.json
                    file.write(str(dictionnary)) #On met dans le fichier le dictionnaire

                time.sleep(1)

                menu_GestionQuestion()
    
    elif suppTerm == 0:
        print("Trés bien, annulation !")

        time.sleep(1)

        menu_GestionQuestion()

    else:
        print("Réessaye")

        time.sleep(1)

        print()

        suppQuestion(dictionnary)

def revoirTermeOrder(arevoir,dictionnary):
    for key in dictionnary:
        value = dictionnary[key]

        for key2 in arevoir:
            if key == key2:
                learnQuestionOrder_validation(key,value,arevoir)

def termeARevoir(key,value,arevoir):

    arevoir.append(key)

def learnQuestionOrder_question(key,value):
    print(key,'(',value,')')

def learnQuestionOrder_validation(key,value,arevoir):
    learnQuestionOrder_question(key,value)

    saisie = input('>>> ')

    if saisie == value:
        print('Super')
        
        time.sleep(0.5)

        print()

    elif saisie == 'exit':
        print("Arrêt des questions !")

        time.sleep(1)

        index()

    else:
        print('Recommence')

        time.sleep(1)

        print()

        termeARevoir(key,value,arevoir)
    
        learnQuestionOrder_validation(key,value,arevoir)

def learnQuestionOrder(dictionnary):
    arevoir = []

    if dictionnary != {}:
        for key in dictionnary:
            value = dictionnary[key]   
        
            learnQuestionOrder_validation(key,value,arevoir)

        revoirTermeOrder(arevoir,dictionnary)
            
        print("Bravo, tu as fini !")
    else:
        print("Il n'y a pas de questions")

    time.sleep(1)

    print("""
+------------------------------------------------+
| {1} Réapprendre                                |
|                                                |
| {2} Éditer les questions                       |
|                                                |
| {3} Revenir au menu principale                 |
|                                                |
| {99} : Terminer le programme                   |
+------------------------------------------------+
""")

    action = input("action >>> ") #Apparition de l'encadré qui demande les numéros d'actions

    if action == '1': #Si l'action demandé est la 1
        print()

        learnQuestionOrder(db.dicoMain)

    elif action == '2':
        menu_GestionQuestion()

    elif action == '3': #Si l'action demandé est la 1
        index()

    elif action == '99': #Si l'action demandé est la 99
        exit() #On coupe la boucle infini
    
    else:
        print("Commande inexistante !")
        
        time.sleep(1)
        
        index()

def exportJson(dictionnary):
    """
    Fonction qui permet d'exporter un dictionnaire en .json dans un fichier exportation
    """
    chemin = os.getcwd() #Je récupére le chemin de ce fichier : C:\Users\USER\Desktop
    
    chemin = chemin.replace('\\' , '/') #Je replace les \ par des / : C:/Users/USER/Desktop

    chemin = chemin[2:] #Je supprime les deux premiers caractères : /Users/USER/Desktop

    chemin = chemin + '/exportation' #J'ajoute le nom du dossier a chemin : /Users/USER/Desktop/exportation

    if not os.path.isdir(chemin): #Je vérifie que le dossier "exportation" n'existe pas
        os.mkdir(chemin) #Et je le crée
    
    chemin = chemin + '/export_data.json' #Je rajoute le nom du fichier que je veux exporter : /Users/USER/Desktop/exportation/export_data.json

    with open(chemin, 'w') as file : #Ouverture/création (w) de export_data.json
        file.write(str(dictionnary)) #On met dans le fichier le dictionnaire

    time.sleep(1) #On attend un peu

    print('Fichier exporté !') #Et on dit que le fichier est exporté

def importJson():
    """
    Fonction qui permet d'importer un dictionnaire en .json
    """
    if os.path.exists('import_data.json') == True: #On vérifie que le fichier import_data.json existe bien
        with open('import_data.json', 'r') as file :  #Ouverture (rb) de import_data.json
            dico = file.read()  #On récupère le dictionnaire

        db.dico = eval(dico)
        
        time.sleep(1) #On attend un peu

        print('Fichier importé !') #Et on dit que le fichier est exporté

    else: #Et si le fichier existe pas
        print('Fichier introuvable ! Veuillez vérifier que votre fichier s\'appelle bien "import_data.json" ou qu\'il exite !') #On dit que c'est pas bon

def fileExportPath():
    """
    Fonction qui permet d'ouvrir le l'emplacement du fichier
    """
    chemin = os.getcwd() #Je récupére le chemin de ce fichier : C:\Users\USER\Desktop

    chemin = chemin.replace('\\' , '/') #Je replace les \ par des / : C:/Users/USER/Desktop

    chemin = chemin[2:] #Je supprime les deux premiers caractères : /Users/USER/Desktop

    chemin = chemin + '/exportation' #J'ajoute le nom du dossier a chemin : /Users/USER/Desktop/exportation

    if not os.path.isdir(chemin): #Je vérifie que le dossier "exportation" n'existe pas
        exportJson(db.dicoMain)
        os.mkdir(chemin) #Et je le crée
    
        chemin = chemin + '/export_data.json' #Je rajoute le nom du fichier que je veux exporter : /Users/USER/Desktop/exportation/export_data.json

        with open(chemin, 'w') as file : #Ouverture/création (w) de export_data.json
            file.write(str(db.dico)) #On met dans le fichier le dictionnaire

    elif os.path.isdir(chemin):
        chemin = os.getcwd() #Je récupére le chemin de ce fichier : C:\Users\USER\Desktop
    
        chemin = chemin + '\exportation' #Je rajoute le dossier au chemin : C:\Users\USER\Desktop\exportation

        chemin = os.path.realpath(chemin) #Je défini chemin comme le chemin

        os.startfile(chemin) #J'ouvre le chemin
    
    time.sleep(1)

    menu_GestionQuestion()

def addQuestion(dictionnary):
    """
    Fonction qui permet de rajouet des questions
    """
    premierElement = input("premier élément >>> ")

    if premierElement == 'exit':
        time.sleep(1)

        menu_GestionQuestion()
    
    else:
        pass

    deuxiemeElement = input("élément associé >>> ")

    dictionnary.update({premierElement : deuxiemeElement})

    with open('liste_questions.json', 'w') as file : #Ouverture/création (w) de annuaire.json
        file.write(str(dictionnary)) #On met dans le fichier le dictionnaire

    print("""
+------------------------------------------------+
| {1} Rajouter une autre question                |
|                                                |
| {2} Retourner au menu de gestion des questions |
| {3} Retourner au menu principale               |
|                                                |
| {99} : Terminer le programme                   |
+------------------------------------------------+
""")
    action = input("action >>> ") #Apparition de l'encadré qui demande les numéros d'actions

    if action == '1': #Si l'action demandé est la 1
        addQuestion(db.dicoMain)
    
    elif action == '2': #Si l'action demandé est la 4
        menu_GestionQuestion()

    elif action == '3': #Si l'action demandé est la 4
        index()

    elif action == '99': #Si l'action demandé est la 99
        exit() #On coupe la boucle infini

    else:
        print("Commande inexistante !")
        
        time.sleep(1)
        
        index()
    
def suppQuestion(dictionnary):
    variant = 0

    listeQuestions = []

    print('{0} Annulation')

    for key in dictionnary:
        value = dictionnary[key]

        variant += 1

        listeQuestions.append(key)

        print('{', variant, '} ', key, ' : ', value, sep='') #On affiche le nom puis un : puis le numéro de téléphone
    
    time.sleep(1)

    print()

    try:
        suppTerm = int(input("Quelle qestion veut-tu supprimer ? "))

    except ValueError:
        print("Donne un chiffre valide !")

        time.sleep(1)

        suppQuestion(dictionnary)
        
    if suppTerm <= variant and suppTerm != 0:
        suppConfirmation = input("Tu es sûr ? ")
        
        if suppConfirmation == 'oui':
            suppTerm -= 1

            questionChoisie = listeQuestions[suppTerm]

            del dictionnary[questionChoisie]

            print("Question supprimé !")

            with open('liste_questions.json', 'w') as file : #Ouverture/création (w) de annuaire.json
                file.write(str(dictionnary)) #On met dans le fichier le dictionnaire

            time.sleep(1)

            menu_GestionQuestion()
        
        elif suppConfirmation == ' ' or '':
            suppQuestion(dictionnary)
        
        else:
            print("Trés bien, annulation !")

            time.sleep(1)

            menu_GestionQuestion()
    
    elif suppTerm == 0:
        print("Trés bien, annulation !")

        time.sleep(1)

        menu_GestionQuestion()

    else:
        print("Réessaye")

        time.sleep(1)

        print()

        suppQuestion(dictionnary)

def showQuestion(dictionnary):
    """
    Affiche les questions
    """
    variant = 0
    for key in dictionnary:
        value = dictionnary[key]
        print(key,':',value) #On affiche le nom puis un : puis le numéro de téléphone
        variant = 1
    
    if variant == 0:
        print("Il n'y a aucune question")
    
    time.sleep(2)

    menu_GestionQuestion()

def menu_GestionQuestion():
    """
    Fonction qui affiche le menu de gestion des questions
    """
    print("""
+--[ Menu de gestion ]---------------------------+
| {1} Afficher la liste de questions             |
| {2} Supprimer des questions                    |
| {3} Modifier des questions                     |
| {4} Ajouter des questions                      |
| {5} Importer une liste de questions            |
| {6} Exporter la liste de questions actuelle    |
| {7} Ouvrir l'emplacement de l'exportation      |
|                                                |
| {8} Revenir au menu principale                 |
|                                                |
| {99} : Terminer le programme                   |
+------------------------------------------------+
""")
    action = input("action >>> ") #Apparition de l'encadré qui demande les numéros d'actions

    if action == '1': #Si l'action demandé est la 4
        showQuestion(db.dicoMain)

    elif action == '2':
        suppQuestion(db.dicoMain)
    
    elif action == '3':
        editQuestion(db.dicoMain)

    elif action == '4': #Si l'action demandé est la 1
        addQuestion(db.dicoMain)

    elif action == '5': #Si l'action demandé est la 1
        importJson()
    
    elif action == '6': #Si l'action demandé est la 1
        exportJson(db.dicoMain)

    elif action == '7': #Si l'action demandé est la 1
        fileExportPath()

    elif action == '8':
        index()

    elif action == '99': #Si l'action demandé est la 99
        exit() #On coupe la boucle infini
    
    else:
        print("Commande inexistante !")
        
        time.sleep(1)
        
        menu_GestionQuestion()

def index():
    print("""
+--[ Menu principal ]----------------------------+
| {1} Gestion des questions                      |
| {2} Apprendre dans l'ordre                     |
|                                                |
| {99} : Terminer le programme                   |
+------------------------------------------------+
""")
    action = input("action >>> ") #Apparition de l'encadré qui demande les numéros d'actions

    if action == '1': #Si l'action demandé est la 1
        menu_GestionQuestion() # Ouvrir le panel de gestion des questions

    if action == '2': #Si l'action demandé est la 2
        learnQuestionOrder(db.dicoMain) # Ouvrir le panel de gestion des questions

    elif action == '99': #Si l'action demandé est la 99
        exit() #On coupe la boucle infini

    else:
        print("Commande inexistante !")
        
        time.sleep(1)

        index()

#Le programme commence ici

#dico = {'Ouverture des états généraux' : '5 mai 1789','Sacre de Napoléon Bonaparte' : '2 décembre 1804'}

class db: #On crée une classe database pour stocker le dictionnaire
    if not os.path.isdir('/liste_questions.json'):
        dico = {}

        with open('liste_questions.json', 'w') as file : #Ouverture/création (w) de annuaire.json
            file.write(str(dico)) #On met dans le fichier le dictionnaire

    with open('liste_questions.json', 'r') as file : #Ouverture (rb) de import_data.json
        dicoMain = file.read() #On récupère le dictionnaire

    dicoMain = eval(dicoMain)

index()