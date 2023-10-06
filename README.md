# Nmap Automation Tool

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)

Ce script Python simple utilise la bibliothèque Nmap pour automatiser la numérisation de ports sur un hôte distant. Il permet à l'utilisateur de choisir le type de scan, l'adresse IP cible et la plage de ports à scanner.

## Prérequis

- Python 3.x
- La bibliothèque Nmap (`python-nmap`). Vous pouvez l'installer en utilisant `pip` :

  ```
  pip install python-nmap
  ```

## Utilisation

1. Clonez ce référentiel ou téléchargez le fichier `scan.py`.

2. Exécutez le script en utilisant Python 3 :

   ```
   python scan.py
   ```

3. Suivez les invites pour spécifier l'adresse IP cible, le type de scan (SYN ACK, UDP ou Comprehensive) et la plage de ports personnalisée.

4. Le script effectuera la numérisation et affichera les résultats.

## Options de Scan

- SYN ACK Scan : Un scan SYN ACK standard.
- UDP Scan : Un scan des ports UDP.
- Comprehensive Scan : Un scan complet avec détection de service, détection de version, détection de script, etc.

## Avertissement

Ce script est destiné à des fins éducatives et de test. N'utilisez-le que sur des systèmes pour lesquels vous avez l'autorisation d'effectuer des scans de ports.

## Licence

Ce projet est sous licence [Licence]. Pour plus d'informations, consultez le fichier [LICENSE.md].
