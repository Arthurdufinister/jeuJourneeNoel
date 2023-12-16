import tkinter as tk
import socket
import threading
import csv
from customtkinter import *


def extractionDonnees(nomFichier, separateur):
    '''
    précondition : nomFichier est du type str et doit être le nom d'un fichier csv.
                   separateur est de type str et doit être soit une virgule ou un point virgule.
    postcondition: Cette fonction récupère les données d'un fichier csv et renvoie un tableau contenant
    des dictionnaires dont les clés sont les descripteurs associés :
    La liste des descripteurs et la liste de toutes les données
    '''
    if nomFichier[-4:] != ".csv":
        return "Erreur : Ce fichier n'est pas un fichier CSV"
    else:
        tab = []
        with open(nomFichier, newline='', encoding='utf-8-sig') as csvfile:
            fichier = csv.DictReader(csvfile, delimiter=separateur)
    # pour remplir notre tableau, une boucle for parcourant chaque ligne du fichier csv sera utilisée
            for ligne in fichier:
                tab.append(dict(ligne))
        return tab


questions = {}
joueurs = {}
indice = 0


def charger_emission(fichier):
    global questions
    envoi.configure(state="normal")
    questions = extractionDonnees(fichier, ";")
    print(questions)


window = CTk()
window.title("Serveur")
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(1, weight=1)

# boutons démarrage et arrêt du serveur
topFrame = CTkFrame(window)
btnStart = CTkButton(topFrame, text="Connect", command=lambda: start_server())
btnStart.grid(row=0, column=0, padx=5, pady=5)
btnStop = CTkButton(topFrame, text="Stop",
                    command=lambda: stop_server(), state="disabled")
btnStop.grid(row=0, column=1, padx=5, pady=5)

# bouton suivant pour passer à la question suivante
suivant = CTkButton(topFrame, text="Quest.Suivante", command=lambda: next(), state="disabled")
suivant.grid(row=0, column=2, padx=5, pady=5)

envoi_score = CTkButton(topFrame, text="affiche score",
                        command=lambda: envoi_score_(), state="disabled")
envoi_score.grid(row=0, column=3, padx=5, pady=5)

envoi_rep = CTkButton(topFrame, text="affiche réponse",
                      command=lambda: envoi_reponse(), state="disabled")
envoi_rep.grid(row=0, column=4, padx=5, pady=5)

# boutons pour envoyer des infos aux clients (propositions ou score - il manque le bouton envoi_score)
envoi = CTkButton(topFrame, text="Envoi", command=lambda: envoi_question(), state="disabled")
envoi.grid(row=0, column=5, padx=5, pady=5)
###Ordre : connect stop quest suivante afficher score affich rep envoi emission 1

# bouton pour charger les émissions (il en faut 5)
charge_emission = CTkButton(
    topFrame, text="Emission 1", command=lambda: charger_emission("questions.csv"), state="disabled")
charge_emission.grid(row=1, column=0, padx=5, pady=5)

charge_emission2=CTkButton(topFrame, text="Emission 2", command=lambda : charger_emission("questions.csv"), state="disabled")
charge_emission2.grid(row=1, column=1, padx=5, pady=5)

charge_emission3=CTkButton(topFrame, text="Emission 3", command=lambda : charger_emission("questions.csv"), state="disabled") 
charge_emission3.grid(row=1, column=2, padx=5, pady=5)

charge_emission4=CTkButton(topFrame, text="Emission 4", command=lambda : charger_emission("questions.csv"), state="disabled") 
charge_emission4.grid(row=1, column=3, padx=5, pady=5)

charge_emission5=CTkButton(topFrame, text="Emission 5", command=lambda : charger_emission("questions.csv"), state="disabled") 
charge_emission5.grid(row=1, column=4, padx=5, pady=5)


topFrame.grid(row=0, column=0, pady=(5, 0), sticky="nsew")

# Affichage des infos de connexions
middleFrame = CTkFrame(window)
lblHost = CTkLabel(middleFrame, text="Host: X.X.X.X")
lblHost.grid(row=0, column=0, padx=(5, 0))
lblPort = CTkLabel(middleFrame, text="Port:XXXX")
lblPort.grid(row=0, column=1, padx=(5, 0))
middleFrame.grid(row=1, column=0, pady=(5, 0), sticky="nsew")

# fenêtre J1
cadre_J1 = CTkFrame(window)
joueur1_display = CTkTextbox(cadre_J1, width=400, height=150)
joueur1_display.grid(row=0, column=0, padx=(5, 0))
cadre_J1.grid(row=2, column=0, pady=(5, 5), sticky="nsew")

# boutons score J1
j1_1 = CTkButton(cadre_J1, text="+1", command=lambda: plus_un_j1(), state="disabled")
j1_1.grid(row=0, column=1, padx=(5, 0))

j1_3 = CTkButton(cadre_J1, text="+3", command=lambda: plus_trois_j1(), state="disabled")
j1_3.grid(row=0, column=2, padx=(5, 0))

j1_5 = CTkButton(cadre_J1, text="+5", command=lambda: plus_cinq_j1(), state="disabled")
j1_5.grid(row=0, column=3, padx=(5, 0))

# fenêtre J2
cadre_J2 = CTkFrame(window)
joueur2_display = CTkTextbox(cadre_J2, width=400, height=150)
joueur2_display.grid(row=0, column=0, padx=(5, 0))
cadre_J2.grid(row=3, column=0, pady=(5, 5), sticky="nsew")

# boutons score J2
j2_1 = CTkButton(cadre_J2, text="+1", command=lambda: plus_un_j2(), state="disabled")
j2_1.grid(row=0, column=1, padx=(5, 0))

j2_3 = CTkButton(cadre_J2, text="+3", command=lambda: plus_trois_j2(), state="disabled")
j2_3.grid(row=0, column=2, padx=(5, 0))

j2_5 = CTkButton(cadre_J2, text="+5", command=lambda: plus_cinq_j2(), state="disabled")
j2_5.grid(row=0, column=3, padx=(5, 0))

# fenêtre J3
cadre_J3 = CTkFrame(window)
joueur3_display = CTkTextbox(cadre_J3, width=400, height=150)
joueur3_display.grid(row=0, column=0, padx=(5, 0))
cadre_J3.grid(row=4, column=0, pady=(5, 5), sticky="nsew")

# boutons score J3
j3_1 = CTkButton(cadre_J3, text="+1", command=lambda: plus_un_j3(), state="disabled")
j3_1.grid(row=0, column=1, padx=(5, 0))

j3_3 = CTkButton(cadre_J3, text="+3", command=lambda: plus_trois_j3(), state="disabled")
j3_3.grid(row=0, column=2, padx=(5, 0))

j3_5 = CTkButton(cadre_J3, text="+5", command=lambda: plus_cinq_j3(), state="disabled")
j3_5.grid(row=0, column=3, padx=(5, 0))

# fenêtre J4
cadre_J4 = CTkFrame(window)
joueur4_display = CTkTextbox(cadre_J4, width=400, height=150)
joueur4_display.grid(row=0, column=0, padx=(5, 0))
cadre_J4.grid(row=5, column=0, pady=(5, 5), sticky="nsew")

# boutons score J4
j4_1 = CTkButton(cadre_J4, text="+1", command=lambda: plus_un_j4(), state="disabled")
j4_1.grid(row=0, column=1, padx=(5, 0))

j4_3 = CTkButton(cadre_J4, text="+3", command=lambda: plus_trois_j4(), state="disabled")
j4_3.grid(row=0, column=2, padx=(5, 0))

j4_5 = CTkButton(cadre_J4, text="+5", command=lambda: plus_cinq_j4(), state="disabled")
j4_5.grid(row=0, column=3, padx=(5, 0))

# fenêtre J5
cadre_J5 = CTkFrame(window)
joueur5_display = CTkTextbox(cadre_J5, width=400, height=150)
joueur5_display.grid(row=0, column=0, padx=(5, 0))
cadre_J5.grid(row=6, column=0, pady=(5, 5), sticky="nsew")

# boutons score J5
j5_1 = CTkButton(cadre_J5, text="+1", command=lambda: plus_un_j5(), state="disabled")
j5_1.grid(row=0, column=1, padx=(5, 0))

j5_3 = CTkButton(cadre_J5, text="+3", command=lambda: plus_trois_j5(), state="disabled")
j5_3.grid(row=0, column=2, padx=(5, 0))

j5_5 = CTkButton(cadre_J5, text="+5", command=lambda: plus_cinq_j5(), state="disabled")
j5_5.grid(row=0, column=3, padx=(5, 0))
###################################################################
server = None
HOST_ADDR = "192.168.1.62"
HOST_PORT = 59000
client_name = " "
clients = []
clients_names = []


# Start server function
def start_server():
    global server, HOST_ADDR, HOST_PORT  # code is fine without this
    btnStart.configure(state="disabled")
    btnStop.configure(state="normal")
    charge_emission.configure(state="normal")
    charge_emission2.configure(state="normal")
    charge_emission3.configure(state="normal")
    charge_emission4.configure(state="normal")
    charge_emission5.configure(state="normal")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

    server.bind((HOST_ADDR, HOST_PORT))
    server.listen(5)  # server is listening for client connection

    threading._start_new_thread(accept_clients, (server, " "))

    lblHost.configure(text="Host: " + HOST_ADDR)
    lblPort.configure(text="Port: " + str(HOST_PORT))



# Stop server function
def stop_server():
    global server
    btnStart.configure(state="normal")
    btnStop.configure(state="disabled")


def accept_clients(the_server, y):
    while True:
        client, addr = the_server.accept()
        clients.append(client)

        # use a thread so as not to clog the gui thread
        threading._start_new_thread(
            send_receive_client_message, (client, addr))


# Function to receive message from current client AND
# Send that message to other clients
def send_receive_client_message(client_connection, client_ip_addr):
    global server, client_name, clients, clients_addr, joueurs
    client_msg = " "

    # send welcome message to client
    client_name = client_connection.recv(4096).decode()
    joueurs[client_name] = {}
    joueurs[client_name]['socket'] = client_connection

    welcome_msg = "Welcome " + client_name + ". Use 'exit' to quit"
    client_connection.send(welcome_msg.encode())

    clients_names.append(client_name)

    update_client_names_display(clients_names)  # update client names display

    while True:
        data = client_connection.recv(4096).decode()
        if not data:
            break
        if data == "exit":
            break

        client_msg = data

        idx = get_client_index(clients, client_connection)
        sending_client_name = clients_names[idx]
        joueurs[sending_client_name]['affichage'].configure(state="normal")

        joueurs[sending_client_name]['message'] = client_msg
        joueurs[sending_client_name]['affichage'].insert(
            "end", "\n"+sending_client_name + " a dit "+client_msg)
        joueurs[sending_client_name]['affichage'].configure(state="disabled")
        print(joueurs)
        # for c in clients:
        #   if c != client_connection:
        #       server_msg = str(client_msg)
        #       c.send(server_msg.encode())

    # find the client index then remove from both lists(client name list and connection list)
    idx = get_client_index(clients, client_connection)
    del clients_names[idx]
    del clients[idx]
    server_msg = "BYE!"
    client_connection.send(server_msg.encode())
    client_connection.close()

    update_client_names_display(clients_names)  # update client names display


def envoi_question():
    global questions, joueurs, indice
    envoi.configure(state="disabled")
    j1_1.configure(state="normal")
    j1_3.configure(state="normal")
    j1_5.configure(state="normal")
    j2_1.configure(state="normal")
    j2_3.configure(state="normal")
    j2_5.configure(state="normal")
    j3_1.configure(state="normal")  
    j3_3.configure(state="normal")
    j3_5.configure(state="normal")
    j4_1.configure(state="normal")
    j4_3.configure(state="normal")
    j4_5.configure(state="normal")
    j5_1.configure(state="normal")
    j5_3.configure(state="normal")
    j5_5.configure(state="normal")
    envoi_rep.configure(state="normal")
    print(questions[indice]['A'], questions[indice]['B'])
    for joueur in joueurs:
        match questions[indice]["Type"]:
            case "Duo":
                question = str(
                    questions[indice]["Type"]+";A;"+questions[indice]['A']+";B;"+questions[indice]['B'])
            case "Carré":
                question = str(questions[indice]["Type"]+";A;"+questions[indice]['A']+";B;" +
                               questions[indice]['B']+";C;"+questions[indice]['C']+";D;"+questions[indice]['D'])
            case "Cash":
                question = str(questions[indice]["Type"])
        print(question[0:7])
        joueurs[joueur]['socket'].send(question.encode())


def envoi_reponse():
    global clients, joueurs
    envoi_rep.configure(state="disabled")
    envoi_score.configure(state="normal")
    for joueur in joueurs:
        print(type(joueurs[joueur]['message']))
        reponse_joueur = joueurs[joueur]['message']
        joueurs[joueur]['socket'].send(("reponse;"+reponse_joueur).encode())


def envoi_score_():
    global clients, joueurs
    j1_1.configure(state="disabled")
    j1_3.configure(state="disabled")
    j1_5.configure(state="disabled")
    j2_1.configure(state="disabled")
    j2_3.configure(state="disabled")
    j2_5.configure(state="disabled")
    j3_1.configure(state="disabled")
    j3_3.configure(state="disabled")
    j3_5.configure(state="disabled")
    j4_1.configure(state="disabled")
    j4_3.configure(state="disabled")
    j4_5.configure(state="disabled")
    j5_1.configure(state="disabled")
    j5_3.configure(state="disabled")
    j5_5.configure(state="disabled")
    envoi_score.configure(state="disabled")
    suivant.configure(state="normal")
    for joueur in joueurs:
        print(type(joueurs[joueur]['score']))
        score_joueur = joueurs[joueur]['score']
        joueurs[joueur]['socket'].send(("score;"+str(score_joueur)).encode())


def next():
    global indice
    suivant.configure(state="disabled")
    envoi.configure(state="normal")
    indice += 1
    return indice

############################# Score du joueur 1 #################################


def plus_un_j1():
    global joueurs, clients_names
    joueurs[clients_names[0]]['score'] += 1
    print(joueurs)


def plus_trois_j1():
    global joueurs, clients_names
    joueurs[clients_names[0]]['score'] += 3
    print(joueurs)


def plus_cinq_j1():
    global joueurs, clients_names
    joueurs[clients_names[0]]['score'] += 5
    print(joueurs)

############################# Score du joueur 2 #################################


def plus_un_j2():
    global joueurs, clients_names
    joueurs[clients_names[1]]['score'] += 1
    print(joueurs)


def plus_trois_j2():
    global joueurs, clients_names
    joueurs[clients_names[1]]['score'] += 3
    print(joueurs)


def plus_cinq_j2():
    global joueurs, clients_names
    joueurs[clients_names[1]]['score'] += 5
    print(joueurs)

############################# Score du joueur 3 #################################


def plus_un_j3():
    global joueurs, clients_names
    joueurs[clients_names[2]]['score'] += 1
    print(joueurs)


def plus_trois_j3():
    global joueurs, clients_names
    joueurs[clients_names[2]]['score'] += 3
    print(joueurs)


def plus_cinq_j3():
    global joueurs, clients_names
    joueurs[clients_names[2]]['score'] += 5
    print(joueurs)

############################# Score du joueur 4 #################################


def plus_un_j4():
    global joueurs, clients_names
    joueurs[clients_names[3]]['score'] += 1
    print(joueurs)


def plus_trois_j4():
    global joueurs, clients_names
    joueurs[clients_names[3]]['score'] += 3
    print(joueurs)


def plus_cinq_j4():
    global joueurs, clients_names
    joueurs[clients_names[3]]['score'] += 5
    print(joueurs)


############################# Score du joueur 5 #################################
def plus_un_j5():
    global joueurs, clients_names
    joueurs[clients_names[4]]['score'] += 1
    print(joueurs)


def plus_trois_j5():
    global joueurs, clients_names
    joueurs[clients_names[4]]['score'] += 3
    print(joueurs)


def plus_cinq_j5():
    global joueurs, clients_names
    joueurs[clients_names[4]]['score'] += 5
    print(joueurs)

# Return the index of the current client in the list of clients


def get_client_index(client_list, curr_client):
    idx = 0
    for conn in client_list:
        if conn == curr_client:
            break
        idx = idx + 1

    return idx


# Update client name display when a new client connects OR
# When a connected client disconnects

def update_client_names_display(name_list):
    global joueurs
    affichage = [joueur1_display, joueur2_display,
                 joueur3_display, joueur4_display, joueur5_display]
    for i in range(len(name_list)):

        joueurs[name_list[i]]['affichage'] = affichage[i]
        joueurs[name_list[i]]['score'] = 0
    print(joueurs)


window.mainloop()
