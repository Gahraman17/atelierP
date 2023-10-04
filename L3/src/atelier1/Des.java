package atelier1;

import java.util.Random;

public class Des {
    protected String nom;
    protected int nbFaces;
    protected static Random r = new Random();
    protected static int nombreDeDesCrees = 0;

    public Des() {
        this.nom = "De";
        this.nbFaces = 6;
    }

    public Des(int nbFaces) {
        if (nbFaces >= 3 && nbFaces <= 120) {
            this.nbFaces = nbFaces;
            this.nom = "De";
        } else {
            System.out.println("Impossible");
        }
    }

    public Des(String nom) {
        this.nom = nom;
        this.nbFaces = 6;
    }

    public int getNbFaces() {
        return nbFaces;
    }

    public void setNbFaces(int nbFaces) {
        if (nbFaces >= 3 && nbFaces <= 120) {
            this.nbFaces = nbFaces;
        } else {
            System.out.println("Impossible");
        }
    }

    public String getNom() {
        return nom;
    }

    public void lancerDe() {
        int nbAleatoire = r.nextInt(this.nbFaces) + 1;
        System.out.println(nbAleatoire);
    }

    public int lancerDe(int nbLances) {
        if (nbLances <= 0) {
            System.out.println("Le nombre de lancers doit être supérieur à zéro.");
            return -1; // Valeur d'erreur
        }

        int meilleurLancer = Integer.MIN_VALUE;

        for (int i = 0; i < nbLances; i++) {
            int lancer = r.nextInt(this.nbFaces) + 1;
            System.out.println("Lancer " + (i + 1) + ": " + lancer);

            if (lancer > meilleurLancer) {
                meilleurLancer = lancer;
            }
        }

        System.out.println("Meilleur lancer: " + meilleurLancer);
        return meilleurLancer;
    }

    public Des(int nombreDeFaces, String nom) {
        if (nom == null || nom.isEmpty()) {
            this.nom = "Dé n°" + (++nombreDeDesCrees);
        } else {
            this.nom = nom;
        }
        this.nbFaces = nombreDeFaces;
    }

    @Override
    public String toString() {
        return "Dé " + nom + " à " + nbFaces + " faces";
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null || getClass() != obj.getClass()) {
            return false;
        }
        Des other = (Des) obj;
        return nbFaces == other.nbFaces && nom.equals(other.nom);
    }


}
