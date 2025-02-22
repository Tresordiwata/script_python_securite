import os

def trouver_fichiers_logs(dossier,extension=".log"):
    """
        Parcourt un dossier et renvoie une liste de fichiers de logs avec l'extension specifié
    """
    fichiers_logs=[]
    try:
        for fichier in os.listdir(dossier):
            if fichier.endswith(extension):
                fichiers_logs.append(os.path.join(dossier,fichier))
        return fichiers_logs
    except FileNotFoundError:
        return []